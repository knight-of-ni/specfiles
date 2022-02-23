# This is the correct folder for firewalld service files, even on x86_64
# It is not used for shared objects
%global fw_services %{_prefix}/lib/firewalld/services

Name:    janus-gateway
Version: 0.11.8
Release: 1%{?dist}
Summary: General purpose WebRTC gateway
License: GPLv3
URL: https://github.com/NethServer/janus-gateway

Source0: https://github.com/meetecho/janus-gateway/archive/refs/tags/v%{version}.tar.gz
Source1: janus-gateway.service
Source2: janus-apache.conf
Source3: janus.jcfg
Source4: janus.plugin.streaming.jcfg
Source5: janus.transport.http.jcfg
Source6: janus-gateway.xml
Source7: janus-nginx.conf

BuildRequires: gengetopt
BuildRequires: libtool
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: jansson-devel
BuildRequires: openssl-devel
BuildRequires: libsrtp-devel
BuildRequires: glib2-devel
BuildRequires: libcurl-devel
BuildRequires: libconfig-devel
BuildRequires: libmicrohttpd-devel >= 0.9.59
BuildRequires: libnice-devel >= 0.1.14
BuildRequires: systemd-devel
BuildRequires:  findutils
BuildRequires:  coreutils

%{?systemd_requires}
Requires: jansson
Requires: openssl
Requires: libnice >= 0.1.14
Requires: libmicrohttpd >= 0.9.59

#VERIFY: Normally rpmbuild will sniff these dependencies automatically.
#Requires: glib2
#Requires: libsrtp

%description
Janus is an open source, general purpose, WebRTC gateway designed and developed
by Meetecho.

%package devel
Summary:    Development libraries for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
Development libraries for Janus Gateway

%prep
%autosetup

%build
autoreconf --verbose --force --install
%configure \
    --disable-static \
    --prefix=%{_prefix} \
    --sysconfdir=%{_sysconfdir} \
    %{?dbgflags:CFLAGS="%{dbgflags}" \
    LDFLAGS="%{dbgflags}"}

%make_build

%install
%make_install

install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
install -D -p -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/httpd/conf.d/janus.conf
install -D -p -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/janus/janus.jcfg
install -D -p -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/janus/janus.plugin.streaming.jcfg
install -D -p -m 0644 %{SOURCE5} %{buildroot}%{_sysconfdir}/janus/janus.transport.http.jcfg
install -D -p -m 0644 %{SOURCE7} %{buildroot}%{_sysconfdir}/nginx/default.d/janus.conf

# Install firewalld config
mkdir -p %{buildroot}%{fw_services}
install -pm 0644 %{SOURCE6} %{buildroot}%{fw_services}/

# Remove all libtool archives
find %{buildroot} -regex ".*\.la$" -delete

%post
# Initial installation
if [ $1 -eq 1 ] ; then
    %systemd_post %{name}.service
fi

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license COPYING
%doc README.md SECURITY.md CHANGELOG.md
%config(noreplace) %{_sysconfdir}/janus/*
%{_mandir}/man*/*
%{_bindir}/janus
%{_bindir}/janus-cfgconv
%{_unitdir}/janus-gateway.service
%{_sysconfdir}/nginx/default.d/janus.conf
%{fw_services}/%{name}.xml

# FIXME Place this under etc then have end user symlink it to httpd/conf.d when ready
%{_sysconfdir}/httpd/conf.d/janus.conf

# FIXME this makes the package apache specific - might need apache & nginx subpackages
%attr(755,apache,apache) /usr/share/janus/

%files devel
%doc docs/doxy-boot.js docs/footer.html docs/header.html docs/janus-doxygen.cfg
%{_libdir}/janus
%{_includedir}/janus

%changelog
* Wed Feb 23 2022 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.11.8-1
- 0.11.8 release

* Wed Feb 23 2022 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.11.6-4
- first pass updating specfile to latest standards

* Wed Jan 19 2022 Jonathan Bennett <JBennett@incomsystems.biz> - 0.11.6-3
- Janus-Gateway: Remove pre-set passwords

* Sat Jan 15 2022 Jonathan Bennett <JBennett@incomsystems.biz> - 0.11.6-2
- Janus-Gateway: change service name, add nginx config

* Sat Jan 15 2022 Jonathan Bennett <JBennett@incomsystems.biz> - 0.11.6-1
- Janus-Gateway: upgrade to 0.11.6 (ed0ec46) - Adapted from NethServer sources

* Thu Feb 18 2021 Alessandro Polidori <alessandro.polidori@nethesis.it> - 0.10.10-1
- Janus-Gateway: upgrade to 0.10.10 (7732127) - NethServer/dev#6416

* Tue Oct 20 2020 Alessandro Polidori <alessandro.polidori@nethesis.it> - 0.10.6-1
- Janus-Gateway: upgrade to 0.10.6 (cc204a5) - NethServer/dev#6313

* Tue Jul 14 2020 Davide Principi <davide.principi@nethesis.it> - 0.10.2-2
- Janus-Gateway: upgrade to 922b392 - NethServer/dev#6195
- Upgrade janus lib to 922b392 - nethesis/dev#5824
- Development builds for Janus and sofia-sip - nethesis/dev#5836


* Mon Jun 22 2020 Alessandro Polidori <alessandro.polidori@nethesis.it> - 0.10.2.1-1
- Upgrade janus-gateway to commit a46344d - NethServer/dev#6195

* Tue Jun 16 2020 Alessandro Polidori <alessandro.polidori@nethesis.it> - 0.10.1.1-1
- Upgrade janus-gateway to commit 085ed39 - NethServer/dev#6195

* Thu Mar 21 2019 Alessandro Polidori <alessandro.polidori@nethesis.it> - 0.6.3-1
- Update janus-gateway to 0.6.3 - NethServer/dev#5735

* Thu Mar 7 2019 Alessandro Polidori <alessandro.polidori@nethesis.it> - 0.6.2-1
- Update janus-gateway to 0.6.2 - NethServer/dev#5728

* Thu Feb 28 2019 Alessandro Polidori <alessandro.polidori@nethesis.it> - 0.6.1-1
- Update janus-gateway to 0.6.1 - NethServer/dev#5723

* Tue Jan 15 2019 Alessandro Polidori <alessandro.polidori@nethesis.it> - 0.6.0-1
- Update janus-gateway to 0.6.0 - NethServer/dev#5555

* Wed Nov 21 2018 Alessandro Polidori <alessandro.polidori@nethesis.it> - 0.5.0-1
- Update janus-gateway to 0.5.0 - NethServer/dev#5648

* Tue Sep 25 2018 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 0.4.3-2
- Update to upstream commit ef8477e6081c4015e244fbce37d9930e73b83412

* Tue Jul 24 2018 Alessandro Polidori <alessandro.polidori@gmail.com> - 0.4.3-1
- Update janus-gateway to 0.4.3 - NethServer/dev#5511

* Thu May 31 2018 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 0.4.1
- Update to upstream release 0.4.1

* Thu Mar 08 2018 Stefano Fancello <stefano.fancello@nethesis.it> - 0.2.5.1-1
- janus-gateway: Janus doesn't try to restart if it fails - Bug NethServer/dev#5426

* Mon Nov 20 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 0.2.5-1
- janus-gateway ignores rtp_port_range option - Bug NethServer/dev#5374
