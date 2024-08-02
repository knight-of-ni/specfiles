Name:              wolfssl
Version:           5.7.2
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
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files and development libraries
for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%autosetup -p 1 -n %{name}-%{version}-stable

# Fix the bundled doc builder scripts to run in our environment
sed -i 's/command -v .*/true/g' doc/generate_documentation.sh
sed -i 's/doxygen Doxyfile/doxygen -u Doxyfile \&\& doxygen Doxyfile/g' doc/generate_documentation.sh
sed -i 's/Next...\\n/Next.../g' doc/check_api.sh

%build
autoreconf --verbose --force --install

# Wolfssl has a *lot* of build options. The options below represent an attempt at general compatiblity
# Note we need to set --disable-qt flag, in order enable HAVE_DH_DEFAULT_PARAMS (required for Netatalk)
#
# Netatalk project needs wolfssl built with HAVE_DH_DEFAULT_PARAMS, OPENSSL_EXTRA, and OPENSSL_ALL options
# https://github.com/Netatalk/netatalk/blob/main/meson.build#L566
%configure \
           --disable-static     \
           --enable-all         \
           --disable-qt

%make_build
%make_build dox-html

%install
%make_install

%check
#%make_build test

%files
%license COPYING LICENSING
%doc ChangeLog.md README README.md doc/html
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

%changelog
* Fri Aug 02 2024 Andrew Bauer <zonexpertconsulting@outlook.com> - 5.7.2-1
- Initial specfile

