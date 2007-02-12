#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	PGPLOT
Summary:	PGPLOT perl module
Summary(pl.UTF-8):   Moduł perla PGPLOT
Name:		perl-PGPLOT
Version:	2.18
Release:	5
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{version}.tar.gz
# Source0-md5:	0c27c49f6443eb4fdcc9eaee4c756c87
BuildRequires:	XFree86-devel
BuildRequires:	gcc-g77
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-ExtUtils-F77 >= 1.11
BuildRequires:	pgplot-devel >= 5.2.2-1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PGPLOT - perl interface to the PGPLOT graphics library.

%description -l pl.UTF-8
PGPLOT - interfejs perla do biblioteki graficznej PGPLOT.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:echo /NULL | %{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README HELP
%{perl_vendorarch}/PGPLOT.pm
%dir %{perl_vendorarch}/auto/PGPLOT
%{perl_vendorarch}/auto/PGPLOT/PGPLOT.bs
%attr(755,root,root) %{perl_vendorarch}/auto/PGPLOT/PGPLOT.so
%{_mandir}/man3/*
