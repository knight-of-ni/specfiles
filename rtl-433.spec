%global commit_date     20220401
%global commit_long     8228f0d4819bb07146b421cce3b535bd4d4db69c
%global commit_short    %(c=%{commit_long}; echo ${c:0:7})

Name: rtl-433
Version: 21.12
Release: 4.%{commit_date}git%{commit_short}%{dist}

Summary: Generic radio data receiver
License: GPLv2
Url: https://github.com/merbanan/rtl_433

Source0: https://github.com/merbanan/rtl_433/archive/%{commit_long}/%{name}-%{commit_long}.tar.gz

BuildRequires: coreutils
BuildRequires: sed
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: rtl-sdr-devel
BuildRequires: SoapySDR-devel
%if 0%{?fedora} > 36
BuildRequires: libusb-compat-0.1-devel
%else
BuildRequires: libusb-devel
%endif

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


# install the example config file into the config folder
install -Dm 644 conf/rtl_433.example.conf %{buildroot}%{_sysconfdir}/rtl_433/rtl_433.conf

# Commenting these config options made more sensible defaults on my system
for C in \
    'pulse_detect squelch' \
    'pulse_detect magest' \
    'samples_to_read 0' \
    'analyze_pulses false' \
    'device        0' \
    'pulse_detect autolevel' \
    'report_meta level' \
    'report_meta noise' \
    'report_meta stats' \
    'report_meta time:usec' \
    'report_meta protocol' \
    'signal_grabber none' \
    'output json' \
    'convert si' \
    'stop_after_successful_events false' \
;do
    sed -i 's\^'"$C"'$\'#"$C"'\' %{buildroot}%{_sysconfdir}/rtl_433/rtl_433.conf
done

# example config files will be placed under doc
rm -rf %{buildroot}%{_usr}%{_sysconfdir}

%check
%ctest

%files
%license COPYING
%doc AUTHORS *.md docs/*.md conf examples
%dir %{_sysconfdir}/rtl_433
%config(noreplace) %{_sysconfdir}/rtl_433/rtl_433.conf
%{_bindir}/rtl_433
%{_mandir}/man*/*

%files devel
%doc AUTHORS
%{_includedir}/rtl_433*.h

%changelog
* Sun Apr 17 2022 Andrew Bauer <zonexpertconsulting@outlook.com> - 21.12-4.20220401git8228f0d
- Move COPYING to license
- Run ctest suite

* Sun Apr 10 2022 Andrew Bauer <zonexpertconsulting@outlook.com> - 21.12-3.20220401git8228f0d
- Comment some of the config options makes for more sensible defaults
- Use install instead of cp for config file

* Fri Apr 08 2022 Andrew Bauer <zonexpertconsulting@outlook.com> - 21.12-2.20220401git8228f0d
- libusb obsoleted by libusb-compat-0.1 on f37 and newer

* Thu Apr 07 2022 Andrew Bauer <zonexpertconsulting@outlook.com> - 21.12-1.20220401git8228f0d
- Initial specfile based on altlinux pkg by Sergey Bolshakov <sbolshakov@altlinux.ru>

