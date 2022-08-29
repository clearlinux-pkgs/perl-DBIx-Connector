#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-DBIx-Connector
Version  : 0.58
Release  : 23
URL      : https://cpan.metacpan.org/authors/id/A/AR/ARISTOTLE/DBIx-Connector-0.58.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/A/AR/ARISTOTLE/DBIx-Connector-0.58.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libd/libdbix-connector-perl/libdbix-connector-perl_0.56-1.debian.tar.xz
Summary  : 'Fast, safe DBI connection and transaction management'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-DBIx-Connector-license = %{version}-%{release}
Requires: perl-DBIx-Connector-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(DBI)

%description
DBIx::Connector
DBIx::Connector provides a simple interface for fast and safe DBI
connection and transaction management. Connecting to a database can be
expensive; you don't want your application to re-connect every time you
need to run a query. The efficient thing to do is to hang on to a
database handle to maintain a connection to the database in order to
minimize that overhead. DBIx::Connector lets you do that without having
to worry about dropped or corrupted connections.

%package dev
Summary: dev components for the perl-DBIx-Connector package.
Group: Development
Provides: perl-DBIx-Connector-devel = %{version}-%{release}
Requires: perl-DBIx-Connector = %{version}-%{release}

%description dev
dev components for the perl-DBIx-Connector package.


%package license
Summary: license components for the perl-DBIx-Connector package.
Group: Default

%description license
license components for the perl-DBIx-Connector package.


%package perl
Summary: perl components for the perl-DBIx-Connector package.
Group: Default
Requires: perl-DBIx-Connector = %{version}-%{release}

%description perl
perl components for the perl-DBIx-Connector package.


%prep
%setup -q -n DBIx-Connector-0.58
cd %{_builddir}
tar xf %{_sourcedir}/libdbix-connector-perl_0.56-1.debian.tar.xz
cd %{_builddir}/DBIx-Connector-0.58
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/DBIx-Connector-0.58/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-DBIx-Connector
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-DBIx-Connector/fa7ae390181139d908a4930057131ca5e66efc3a || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/DBIx::Connector.3
/usr/share/man/man3/DBIx::Connector::Driver.3
/usr/share/man/man3/DBIx::Connector::Driver::Firebird.3
/usr/share/man/man3/DBIx::Connector::Driver::MSSQL.3
/usr/share/man/man3/DBIx::Connector::Driver::Oracle.3
/usr/share/man/man3/DBIx::Connector::Driver::Pg.3
/usr/share/man/man3/DBIx::Connector::Driver::SQLite.3
/usr/share/man/man3/DBIx::Connector::Driver::mysql.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-DBIx-Connector/fa7ae390181139d908a4930057131ca5e66efc3a

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
