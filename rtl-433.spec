%global commit_date     20220401
%global commit_long     8228f0d4819bb07146b421cce3b535bd4d4db69c
%global commit_short    %(c=%{commit_long}; echo ${c:0:7})

Name: rtl-433
Version: 21.12
Release: 1.%{commit_date}git%{commit_short}%{dist}

Summary: Generic radio data receiver
License: GPLv2
Url: https://github.com/merbanan/rtl_433

Source0: https://github.com/merbanan/rtl_433/archive/%{commit_long}/%{name}-%{commit_long}.tar.gz

BuildRequires: coreutils
BuildRequires: sed
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: libusb-devel
BuildRequires: rtl-sdr-devel
BuildRequires: SoapySDR-devel

%description
rtl_433 (despite the name) is a generic data receiver, mainly
for the 433.92 MHz, 868 MHz (SRD), 315 MHz, and 915 MHz ISM bands.

For more documentation and related projects see the https://triq.org/ site.

%package devel
Summary:    Development libraries for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
Development libraries for %{name}

%prep
%autosetup -n rtl_433-%{commit_long}

# Fix python shebang in examples
sed -ri 's\^#!/usr/bin/env python3?$\#!%{python3}\' examples/*.py

%build
%cmake
%cmake_build

%install
%cmake_install
mkdir -p %{buildroot}%{_sysconfdir}/rtl_433
cp conf/rtl_433.example.conf %{buildroot}%{_sysconfdir}/rtl_433/rtl_433.conf

# example config files will be placed under doc
rm -rf %{buildroot}%{_usr}%{_sysconfdir}

%files
%doc AUTHORS COPYING *.md docs/*.md conf examples
%dir %{_sysconfdir}/rtl_433
%config(noreplace) %{_sysconfdir}/rtl_433/*.conf
%{_bindir}/rtl_433
%{_mandir}/man*/*

%files devel
%doc AUTHORS COPYING
%{_includedir}/rtl_433*.h

%changelog
* Thu Apr 07 2022 Andrew Bauer <zonexpertconsulting@outlook.com> - 21.12-1.20220401git8228f0d
- Initial specfile based on altlinux pkg by Sergey Bolshakov <sbolshakov@altlinux.ru>

