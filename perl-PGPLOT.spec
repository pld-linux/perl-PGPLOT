#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	PGPLOT perl module
Summary(pl):	Modu³ perla PGPLOT
Name:		perl-PGPLOT
Version:	2.18
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/PGPLOT/PGPLOT-%{version}.tar.gz
BuildRequires:	XFree86-devel
BuildRequires:	gcc-g77
BuildRequires:	perl >= 5.6
BuildRequires:	perl-ExtUtils-F77 >= 1.11
BuildRequires:	pgplot-devel >= 5.2.2-1
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PGPLOT - perl interface to the PGPLOT graphics library.

%description -l pl
PGPLOT - interfejs perla do biblioteki graficznej PGPLOT.

%prep
%setup -q -n PGPLOT-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%{!?_without_tests:echo /NULL | %{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README HELP
%{perl_sitearch}/PGPLOT.pm
%dir %{perl_sitearch}/auto/PGPLOT
%{perl_sitearch}/auto/PGPLOT/PGPLOT.bs
%attr(755,root,root) %{perl_sitearch}/auto/PGPLOT/PGPLOT.so
%{_mandir}/man3/*
