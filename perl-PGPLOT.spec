%include	/usr/lib/rpm/macros.perl
Summary:	PGPLOT perl module
Summary(pl):	Modu³ perla PGPLOT
Name:		perl-PGPLOT
Version:	2.15
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/PGPLOT/PGPLOT-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	XFree86-devel
BuildRequires:	pgplot-devel
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
PGPLOT - perl interface to the PGPLOT graphics library.

%description -l pl
PGPLOT - interfejs perla do biblioteki graficznej PGPLOT.

%prep
%setup -q -n PGPLOT-%{version}

%build
perl Makefile.PL
make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT/%{perl_sitearch}/auto/PGPLOT/*.so

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/PGPLOT
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        CHANGES README HELP

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {CHANGES,README,HELP}.gz

%{perl_sitearch}/PGPLOT.pm

%dir %{perl_sitearch}/auto/PGPLOT
%{perl_sitearch}/auto/PGPLOT/.packlist
%{perl_sitearch}/auto/PGPLOT/PGPLOT.bs
%attr(755,root,root) %{perl_sitearch}/auto/PGPLOT/PGPLOT.so

%{_mandir}/man3/*
