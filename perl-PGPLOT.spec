#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define	pdir	PGPLOT
Summary:	PGPLOT Perl module
Summary(pl.UTF-8):	Moduł Perla PGPLOT
Name:		perl-PGPLOT
Version:	2.29
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/PGPLOT/%{pdir}-%{version}.tar.gz
# Source0-md5:	eb7aa46a86485dfded60b24cf67eb886
URL:		https://metacpan.org/dist/PGPLOT
BuildRequires:	gcc-fortran
BuildRequires:	libpng-devel
BuildRequires:	perl-Devel-CheckLib >= 1.14
BuildRequires:	perl-ExtUtils-F77 >= 1.13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	pgplot-devel >= 5.2.2-1
BuildRequires:	pkgconfig
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	zlib-devel
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

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

# currently packaged in perl-PDL.spec
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/PDL/Demos/PGPLOT*.pm
%{__rm} -r $RPM_BUILD_ROOT%{perl_vendorarch}/PDL/Graphics/PGPLOT*
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man3/PDL::*.3pm

rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/PGPLOT/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES HELP LICENSE README
%{perl_vendorarch}/PGPLOT.pm
%dir %{perl_vendorarch}/auto/PGPLOT
%attr(755,root,root) %{perl_vendorarch}/auto/PGPLOT/PGPLOT.so
%{_mandir}/man3/PGPLOT.3pm*
