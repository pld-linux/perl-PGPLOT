%include	/usr/lib/rpm/macros.perl
Summary:	PGPLOT perl module
Summary(pl):	Modu� perla PGPLOT
Name:		perl-PGPLOT
Version:	2.17
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/PGPLOT/PGPLOT-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	XFree86-devel
BuildRequires:	pgplot-devel
BuildRequires:	perl-ExtUtils-F77 >= 1.11
BuildRequires:	gcc-g77
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PGPLOT - perl interface to the PGPLOT graphics library.

%description -l pl
PGPLOT - interfejs perla do biblioteki graficznej PGPLOT.

%prep
%setup -q -n PGPLOT-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf CHANGES README HELP

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitearch}/PGPLOT.pm
%dir %{perl_sitearch}/auto/PGPLOT
%{perl_sitearch}/auto/PGPLOT/PGPLOT.bs
%attr(755,root,root) %{perl_sitearch}/auto/PGPLOT/PGPLOT.so
%{_mandir}/man3/*
