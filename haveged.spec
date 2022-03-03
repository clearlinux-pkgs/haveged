#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : haveged
Version  : 1.9.17
Release  : 4
URL      : https://github.com/jirka-h/haveged/archive/v1.9.17/haveged-1.9.17.tar.gz
Source0  : https://github.com/jirka-h/haveged/archive/v1.9.17/haveged-1.9.17.tar.gz
Source1  : haveged.service
Summary  : Feed entropy into random pool
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0+
Requires: haveged-bin = %{version}-%{release}
Requires: haveged-lib = %{version}-%{release}
Requires: haveged-license = %{version}-%{release}
Requires: haveged-man = %{version}-%{release}
Requires: haveged-services = %{version}-%{release}
Patch1: haveged-no-syslog.patch

%description
The haveged daemon feeds the linux entropy pool with random
numbers generated from hidden processor state.

%package bin
Summary: bin components for the haveged package.
Group: Binaries
Requires: haveged-license = %{version}-%{release}
Requires: haveged-services = %{version}-%{release}

%description bin
bin components for the haveged package.


%package dev
Summary: dev components for the haveged package.
Group: Development
Requires: haveged-lib = %{version}-%{release}
Requires: haveged-bin = %{version}-%{release}
Provides: haveged-devel = %{version}-%{release}
Requires: haveged = %{version}-%{release}

%description dev
dev components for the haveged package.


%package lib
Summary: lib components for the haveged package.
Group: Libraries
Requires: haveged-license = %{version}-%{release}

%description lib
lib components for the haveged package.


%package license
Summary: license components for the haveged package.
Group: Default

%description license
license components for the haveged package.


%package man
Summary: man components for the haveged package.
Group: Default

%description man
man components for the haveged package.


%package services
Summary: services components for the haveged package.
Group: Systemd services

%description services
services components for the haveged package.


%prep
%setup -q -n haveged-1.9.17
cd %{_builddir}/haveged-1.9.17
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1646282881
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%configure --disable-static --enable-daemon \
--enable-clock_gettime
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1646282881
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/haveged
cp %{_builddir}/haveged-1.9.17/COPYING %{buildroot}/usr/share/package-licenses/haveged/8624bcdae55baeef00cd11d5dfcfa60f68710a02
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/haveged.service

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/haveged

%files dev
%defattr(-,root,root,-)
/usr/include/haveged/havege.h
/usr/lib64/libhavege.so
/usr/share/man/man3/libhavege.3

%files lib
%defattr(-,root,root,-)
/usr/lib64/libhavege.so.2
/usr/lib64/libhavege.so.2.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/haveged/8624bcdae55baeef00cd11d5dfcfa60f68710a02

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/haveged.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/haveged.service
