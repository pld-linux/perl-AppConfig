#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	AppConfig
Summary:	AppConfig Perl module
Summary(cs):	Modul AppConfig pro Perl
Summary(da):	Perlmodul AppConfig
Summary(de):	AppConfig Perl Modul
Summary(es):	M�dulo de Perl AppConfig
Summary(fr):	Module Perl AppConfig
Summary(it):	Modulo di Perl AppConfig
Summary(ja):	AppConfig Perl �⥸�塼��
Summary(ko):	AppConfig �� ����
Summary(no):	Perlmodul AppConfig
Summary(pl):	Modu� Perla AppConfig
Summary(pt):	M�dulo de Perl AppConfig
Summary(pt_BR):	M�dulo Perl AppConfig
Summary(ru):	������ ��� Perl AppConfig
Summary(sv):	AppConfig Perlmodul
Summary(uk):	������ ��� Perl AppConfig
Summary(zh_CN):	AppConfig Perl ģ��
Name:		perl-AppConfig
Version:	1.55
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{version}.tar.gz
# Source0-md5:	20d81571e7ef7da092613b4dd69fed33
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov >= 4.1-13
Obsoletes:	perl-App-Config
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AppConfig is module for reading configuration files and parsing
command line arguments.

%description -l pl
AppConfig jest modu�em do czytania plik�w konfiguracyjnych oraz
obs�ugi argument�w z linii polece�.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/AppConfig
%{perl_vendorlib}/*.pm
%{_mandir}/man3/*
