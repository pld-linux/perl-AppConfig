#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	AppConfig
Summary:	AppConfig Perl module
Summary(cs):	Modul AppConfig pro Perl
Summary(da):	Perlmodul AppConfig
Summary(de):	AppConfig Perl Modul
Summary(es):	Módulo de Perl AppConfig
Summary(fr):	Module Perl AppConfig
Summary(it):	Modulo di Perl AppConfig
Summary(ja):	AppConfig Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	AppConfig ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul AppConfig
Summary(pl):	Modu³ Perla AppConfig
Summary(pt):	Módulo de Perl AppConfig
Summary(pt_BR):	Módulo Perl AppConfig
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl AppConfig
Summary(sv):	AppConfig Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl AppConfig
Summary(zh_CN):	AppConfig Perl Ä£¿é
Name:		perl-AppConfig
Version:	1.52
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{version}.tar.gz
BuildRequires:	perl >= 5.6.1
BuildRequires:	rpm-perlprov >= 3.0.3-16
Obsoletes:	perl-App-Config
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AppConfig is module for reading configuration files and parsing
command line arguments.

%description -l pl
AppConfig jest modu³em do czytania plików konfiguracyjnych oraz
obs³ugi argumentów z linii poleceñ.

%prep
%setup -q -n %{pdir}-%{version}

%build
perl Makefile.PL
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
%{perl_sitelib}/AppConfig
%{perl_sitelib}/*.pm
%{_mandir}/man3/*
