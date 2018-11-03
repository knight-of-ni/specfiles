%global commit 99c942c90063c73734e56bacaa65f947772d9186
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20150530

Name:           fcgiwrap
Version:        1.1.0
Release:        6.%{date}git%{shortcommit}%{?dist}
Summary:        Simple FastCGI wrapper for CGI scripts
Group:          System Environment/Daemons
License:        MIT
URL:            https://github.com/gnosek/fcgiwrap
Source0:        https://github.com/gnosek/fcgiwrap/archive/%{commit}/%{name}-%{commit}.tar.gz
Source1:        fcgiwrap.service
Source2:        fcgiwrap.socket
Source3:        fcgiwrap

# https://github.com/gnosek/fcgiwrap/pull/39
Patch0:         %{name}-1.1.0-use_pkg-config_libsystemd.patch
# https://github.com/gnosek/fcgiwrap/pull/43
Patch1:         %{name}-1.1.0-declare_cgi_error_noreturn.patch
# https://github.com/gnosek/fcgiwrap/pull/44
Patch2:         %{name}-1.1.0-fix_kill_param_sequence.patch

BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fcgi-devel
BuildRequires:  systemd-devel
%{?systemd_requires}

%description
This package provides a simple FastCGI wrapper for CGI scripts with/
following features:
 - very lightweight (84KB of private memory per instance)
 - fixes broken CR/LF in headers
 - handles environment in a sane way (CGI scripts get HTTP-related environment
   vars from FastCGI parameters and inherit all the others from
   environment of fcgiwrap )
 - no configuration, so you can run several sites off the same
   fcgiwrap pool
 - passes CGI std error output to std error stream of cgiwrap or FastCGI
 - support systemd socket activation, launcher program like spawn-fcgi
   is no longer required on systemd-enabled distributions

%prep
%autosetup -n %{name}-%{commit}

%build
autoreconf -i
%configure --prefix="" --without-systemd # We will supply our own systemd configs
%make_build

%install
%make_install

# Install our own systemd config files
install -Dm 644 %{SOURCE1} %{buildroot}%{_unitdir}/fcgiwrap.service
install -Dm 644 %{SOURCE2} %{buildroot}%{_unitdir}/fcgiwrap.socket
install -Dm 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/sysconfig/fcgiwrap

%post
%systemd_post fcgiwrap.service
%systemd_post fcgiwrap.socket

%preun
%systemd_preun fcgiwrap.service
%systemd_preun fcgiwrap.socket

%postun
%systemd_postun_with_restart fcgiwrap.service
%systemd_postun_with_restart fcgiwrap.socket

%files
%doc README.rst
%license COPYING
%{_sbindir}/fcgiwrap
%{_mandir}/man8/fcgiwrap.8*
%{_unitdir}/fcgiwrap.service
%{_unitdir}/fcgiwrap.socket
%config(noreplace) %{_sysconfdir}/sysconfig/fcgiwrap

%changelog
* Sat Nov 03 2018 Andrew Bauer <zonexpertconsulting@outlook.com> - 1.1.0-6.20150530git99c942c
- Supply our own systemd service, socket, and environment files
- Add Patch2 to fix kill parameter sequence

* Wed Aug 30 2017 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.1.0-5.20150530git99c942c
- Add license
- Use systemd_requires macro
- Update URL
- Add Patch1 to fix compilation with gcc 7

* Wed Nov 09 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.1.0-4.20150530git99c942c
- Patch0 to rename pkg-config libsystemd-daemon to libsystemd

* Thu Feb 04 2016 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.1.0-3.20150530git99c942c
- Use %%make_build macro

* Sat May 30 2015 Juan Orti Alcaine <jorti@fedoraproject.org> - 1.1.0-2.20150530git99c942c
- Update to commit 99c942c

* Fri Feb 08 2013 Hiroaki Nakamura <hnakamur@gmail.com> - 1.1.0-1
- new upstream release.

* Fri Jan 11 2013 Hiroaki Nakamura <hnakamur@gmail.com> - 1.0.3.20120908-1
- Change version to increase monotonously.

* Wed Jan  9 2013 Hiroaki Nakamura <hnakamur@gmail.com> - 1.0.3-3.gitb9f03e6377
- Make the rpm relocatable.

* Tue Dec 25 2012 Hiroaki Nakamura <hnakamur@gmail.com> - 1.0.3-2.gitb9f03e6377

* Tue Jan 31 2012 Craig Barnes <cr@igbarn.es> - 1.0.3-1.git1328862
- Initial package
