#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Parse
%define	pnam	CPAN-Meta
Summary:	Parse::CPAN::Meta - Parse META.yml and other similar CPAN metadata files
Summary(pl.UTF-8):	Parse::CPAN::Meta - Parsuje META.yml i inne podobne pliki z metadanymi CPAN
Name:		perl-Parse-CPAN-Meta
Version:	1.4401
Release:	2
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/D/DA/DAGOLDEN/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	32c8b2ba97887b526a0948706c546eba
URL:		http://search.cpan.org/dist/Parse-CPAN-Meta/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-JSON-PP >= 2.27103
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Parse::CPAN::Meta is a parser for META.yml files, based on the parser
half of YAML::Tiny.

It supports a basic subset of the full YAML specification, enough to
implement parsing of typical META.yml files, and other similarly
simple YAML files.

If you need something with more power, move up to a full YAML parser
such as YAML, YAML::Syck or YAML::LibYAML.

Parse::CPAN::Meta provides a very simply API of only two functions,
based on the YAML functions of the same name. Wherever possible,
identical calling semantics are used.

All error reporting is done with exceptions (die'ing).

%description -l pl.UTF-8
Parse::CPAN::Meta jest parserem plików META.yml opartym na części
parsującej YAML::Tiny.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%dir %{perl_vendorlib}/Parse/CPAN
%{_mandir}/man3/Parse::CPAN::Meta.3pm*
%{perl_vendorlib}/Parse/CPAN/Meta.pm
