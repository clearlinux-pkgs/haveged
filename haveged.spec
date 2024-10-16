#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v20
# autospec commit: f35655a
#
Name     : haveged
Version  : 1.9.19
Release  : 6
URL      : https://github.com/jirka-h/haveged/archive/v1.9.19/haveged-1.9.19.tar.gz
Source0  : https://github.com/jirka-h/haveged/archive/v1.9.19/haveged-1.9.19.tar.gz
Source1  : haveged.service
Summary  : A Linux entropy source using the HAVEGE algorithm
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0+
Requires: haveged-bin = %{version}-%{release}
Requires: haveged-lib = %{version}-%{release}
Requires: haveged-license = %{version}-%{release}
Requires: haveged-man = %{version}-%{release}
Requires: haveged-services = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : file
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: haveged-no-syslog.patch

%description
A Linux entropy source using the HAVEGE algorithm

Haveged is a user space entropy daemon which is not dependent upon the
standard mechanisms for harvesting randomness for the system entropy
pool. This is important in systems with high entropy needs or limited
user interaction (e.g. headless servers).

Haveged uses HAVEGE (HArdware Volatile Entropy Gathering and Expansion)
to maintain a 1M pool of random bytes used to fill /dev/random
whenever the supply of random bits in /dev/random falls below the low
water mark of the device. The principle inputs to haveged are the
sizes of the processor instruction and data caches used to setup the
HAVEGE collector. The haveged default is a 4kb data cache and a 16kb
instruction cache. On machines with a cpuid instruction, haveged will
attempt to select appropriate values from internal tables.

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
Requires: systemd

%description services
services components for the haveged package.


%prep
%setup -q -n haveged-1.9.19
cd %{_builddir}/haveged-1.9.19
%patch -P 1 -p1
pushd ..
cp -a haveged-1.9.19 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1728055811
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static --enable-daemon \
--enable-clock_gettime
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static --enable-daemon \
--enable-clock_gettime
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1728055811
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/haveged
cp %{_builddir}/haveged-%{version}/COPYING %{buildroot}/usr/share/package-licenses/haveged/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/haveged.service
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/haveged
/usr/bin/haveged

%files dev
%defattr(-,root,root,-)
/usr/include/haveged/havege.h
/usr/lib64/libhavege.so
/usr/share/man/man3/libhavege.3

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libhavege.so.2.0.0
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
