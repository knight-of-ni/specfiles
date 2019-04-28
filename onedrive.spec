%global commit fbad4b483558c223b998fc00cae0e5fa8b588f50
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20190424

Name:       onedrive
Version:    2.3.3
Release:    1.%{date}git%{shortcommit}%{?dist}
Summary:    Microsoft OneDrive Client
Group:      System Environment/Network
License:    GPLv3
URL:        https://github.com/abraunegg/onedrive
Source0:    https://github.com/abraunegg/onedrive/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires:	dmd >= 2.085.0
BuildRequires:	sqlite-devel >= 3.7.15
BuildRequires:	libcurl-devel
BuildRequires:  systemd-units

Requires:       sqlite >= 3.7.15
Requires:       libcurl

%{?systemd_requires}

%description
Microsoft OneDrive Client for Linux

%prep
%autosetup -n %{name}-%{commit}

%build
%configure \
    --enable-notifications

%make_build

%install
install -Dm 755 onedrive %{buildroot}%{_bindir}/onedrive
install -Dm 644 logrotate/onedrive.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/onedrive
install -Dm 644 onedrive.1 %{buildroot}%{_mandir}/man1/onedrive.1

install -Dm 644 systemd.units/onedrive.service %{buildroot}%{_unitdir}/onedrive.service
install -Dm 644 systemd.units/onedrive.service %{buildroot}%{_unitdir}/onedrive@.service

%pre
rm -f /root/.config/onedrive/items.db
rm -f /root/.config/onedrive/items.sqlite3
rm -f /root/.config/onedrive/resume_upload

%post
mkdir -p /root/.config/onedrive
mkdir -p /root/OneDrive
mkdir -p /var/log/onedrive
chown root.users /var/log/onedrive
chmod 0775 /var/log/onedrive

%systemd_post onedrive.service

%preun
%systemd_preun onedrive.service

%files
%license LICENSE
%doc README.md README.Office365.md
%{_mandir}/man1/%{name}.1*
%{_bindir}/onedrive
%config(noreplace) %{_sysconfdir}/logrotate.d/onedrive
%ghost %{_localstatedir}/log/onedrive

%{_unitdir}/onedrive.service
%{_unitdir}/onedrive@.service

%changelog
* Sat Apr 27 2019 Andrew Bauer <zonexpertconsulting@outlook.com> - 2.3.3-1.20190424gitfbad4b4
- Initial build of project master branch

