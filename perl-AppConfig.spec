%include	/usr/lib/rpm/macros.perl
Summary:	App-Config perl module
Summary(pl):	Modu� perla App-Config
Name:		perl-AppConfig
Version:	1.52
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/AppConfig/AppConfig-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AppConfig is module for reading configuration files and
parsing command line arguments.

%description -l pl
AppConfig jest modu�em do czytania plik�w konfiguracyjnych oraz
obs�ugi argument�w z lini polece�.

%prep
%setup -q -n AppConfig-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/AppConfig
%{perl_sitelib}/*.pm
%{_mandir}/man3/*
