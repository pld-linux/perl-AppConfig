#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	AppConfig
Summary:	AppConfig - Perl5 module for reading configuration files and parsing command line arguments
Summary(pl.UTF-8):	AppConfig - moduł Perla 5 do czytania plików konfiguracyjnych i analizy linii polecenia
Name:		perl-AppConfig
Version:	1.66
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/AppConfig/%{pdir}-%{version}.tar.gz
# Source0-md5:	21aa4d1bf70a49a94c2dc9293389b3a0
URL:		http://search.cpan.org/dist/AppConfig/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Obsoletes:	perl-App-Config
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AppConfig is a Perl5 module for managing application configuration
information. It maintains the state of any number of variables and
provides methods for parsing configuration files, command line
arguments and CGI script parameters.

%description -l pl.UTF-8
AppConfig jest modułem Perla 5 służącym do czytania informacji
konfiguracyjnych aplikacji. Zachowuje on stan dowolnej liczby
zmiennych i udostępnia metody do analizy plików konfiguracyjnych,
argumrntów linii polecenia i parametrów skryptów CGI.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/AppConfig
%{perl_vendorlib}/*.pm
%{_mandir}/man3/*
