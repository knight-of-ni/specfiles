Name:              wolfssl
Version:           5.7.0
Release:           1%{?dist}
Summary:           Lightweight SSL/TLS library written in ANSI C
License:           GPLv2
URL:               https://github.com/wolfSSL/wolfssl
Source0:           %{url}/archive/v%{version}-stable.tar.gz#/%{name}-%{version}.tar.gz

# Per i686 leaf package policy 
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires: libtool
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: make
BuildRequires: pkgconfig
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: doxygen
BuildRequires: sed
BuildRequires: findutils
# openssl executable needed for check
BuildRequires: openssl

%description
The wolfSSL embedded SSL library (formerly CyaSSL) is a lightweight SSL/TLS
library written in ANSI C and targeted for embedded, RTOS, and
resource-constrained environments - primarily because of its small size,
speed, and feature set. It is commonly used in standard operating environments
as well because of its royalty-free pricing and excellent cross platform
support. wolfSSL supports industry standards up to the current TLS 1.3 and
DTLS 1.3, is up to 20 times smaller than OpenSSL, and offers progressive
ciphers such as ChaCha20, Curve25519, Blake2b and Post-Quantum TLS 1.3 groups.
User bench-marking and feedback reports dramatically better performance when
using wolfSSL over OpenSSL.

wolfSSL is powered by the wolfCrypt cryptography library. Two versions of
wolfCrypt have been FIPS 140-2 validated (Certificate #2425 and certificate
#3389). FIPS 140-3 validation is in progress. For additional information,
visit the wolfCrypt FIPS FAQ or contact fips@wolfssl.com.

%package devel
Summary: Header files and development libraries for %{name}
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files and development libraries
for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package doc
Summary:        HTML Documentation for wolfssl
BuildArch:      noarch

%description doc
This package contains the HTML documentation for wolfssl

%prep
%autosetup -p 1 -n %{name}-%{version}-stable

# Fix the bundled doc builder scripts to run in our environment
sed -i 's/command -v .*/true/g' doc/generate_documentation.sh
sed -i 's/doxygen Doxyfile/doxygen -u Doxyfile \&\& doxygen Doxyfile/g' doc/generate_documentation.sh
sed -i 's/Next...\\n/Next.../g' doc/check_api.sh

# Disable tests that need Internets
sed -i 's/^if BUILD_OCSP$/if FALSE/' scripts/include.am
sed -i 's/^if BUILD_OCSP_STAPLING$/if FALSE/' scripts/include.am

%build
./autogen.sh

# Wolfssl has a *lot* of build options. The options below represent an attempt at general compatiblity
# Note we need to set --disable-qt flag, in order to enable HAVE_DH_DEFAULT_PARAMS (required for Netatalk)
#
# Netatalk package needs wolfssl built with HAVE_DH_DEFAULT_PARAMS, OPENSSL_EXTRA, and OPENSSL_ALL options
# https://github.com/Netatalk/netatalk/blob/main/meson.build#L566
%configure \
           --disable-static     \
           --enable-all         \
           --enable-all-crypto  \
           --disable-qt

%make_build
%make_build dox-html

# fix the shebang in wolfssl-config
sed -i '1s|.*|#!/usr/bin/sh|' wolfssl-config

# Eliminate duplicate files to stop rpmlint from complaining
for ndx in a 0 1 2 3 10 11; do
  ln -sf groups_${ndx}.js doc/html/search/all_${ndx}.js
done
ln -sf functions_4.js doc/html/search/all_1a.js
ln -sf files_b.js doc/html/search/all_13.js
ln -sf groups_16.js doc/html/search/all_18.js

%install
%make_install

# It seems .la files are left hanging around for el9 builds
find %{buildroot} \( -name '*.la' -o -name '*.a' \) -type f -delete -print

%check
%make_build test

%files
%license COPYING LICENSING
%doc ChangeLog.md README README.md
# pickup the documentation placed into pgkdocdir during install
%doc %{_pkgdocdir}/*
%exclude %{_pkgdocdir}/example
%{_libdir}/libwolfssl.so.42{,.*}

%files devel
%doc %{_pkgdocdir}/example
%{_bindir}/wolfssl-config
%{_includedir}/wolfssl/*.h
%{_includedir}/wolfssl/wolfcrypt/*.h
%{_includedir}/wolfssl/openssl/*.h
%{_libdir}/pkgconfig/wolfssl.pc
%{_libdir}/libwolfssl.so

%files doc
%license COPYING LICENSING
%doc doc/html

%changelog
* Fri Aug 02 2024 Andrew Bauer <zonexpertconsulting@outlook.com> - 5.7.2-1
- Initial specfile
