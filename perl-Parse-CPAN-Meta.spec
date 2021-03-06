#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Parse
%define	pnam	CPAN-Meta
Summary:	Parse::CPAN::Meta - parse META.yml and other similar CPAN metadata files
Summary(pl.UTF-8):	Parse::CPAN::Meta - analiza META.yml i innych podobnych plików z metadanymi CPAN
Name:		perl-Parse-CPAN-Meta
Version:	1.4422
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Parse/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	71d52f680b19b3ef36e9a0152e8a3e93
URL:		http://search.cpan.org/dist/Parse-CPAN-Meta/
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.30
BuildRequires:	perl-devel >= 1:5.8.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl(File::Spec) >= 0.80
BuildRequires:	perl-CPAN-Meta-YAML >= 0.011
BuildRequires:	perl-JSON-PP >= 2.27300
BuildRequires:	perl-Test-Simple >= 0.47
%endif
Requires:	perl-CPAN-Meta-YAML >= 0.011
Requires:	perl-JSON-PP >= 2.27300
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

%description -l pl.UTF-8
Parse::CPAN::Meta jest analizatorem plików META.yml opartym na części
analizującej modułu YAML::Tiny.

Obsługuje podstawowy podzbiór pełnej specyfikacji YAML, wystarczający
do analizy typowych plików META.yml i innych podobnie prostych plików
YAML.

Jeżeli potrzebne jest coś o większych możliwościach, należy użyć
pełnego analizatora YAML-a - np. z modułu YAML, YAML::Syck lub
YAML::LibYAML.

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
%{perl_vendorlib}/Parse/CPAN/Meta.pm
%{_mandir}/man3/Parse::CPAN::Meta.3pm*
