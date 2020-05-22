# Author's releases page is not up to date with setup.py, so use git commit
%global commit 6b6984be27ae7f800417bc7fe68bca38e2b5a9c1
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global srcname ouimeaux

Name: python-%{srcname}
Version: 0.8.2
Release: 1%{?shortcommit:.git.%{shortcommit}}%{?dist}
Summary: Open source control for Belkin WeMo devices

License: BSD
Url: https://github.com/iancmcc/ouimeaux
Source0: https://github.com/iancmcc/%{srcname}/archive/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz

BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: findutils
BuildRequires: sed

# Required for check
BuildRequires: %{py3_dist gevent} >= 1.3
BuildRequires: %{py3_dist requests} >= 2.3.0
BuildRequires: %{py3_dist pyyaml}
BuildRequires: %{py3_dist six}
BuildRequires: %{py3_dist future}

%global _description %{expand:
Open source control for Belkin WeMo devices

- Supports WeMo Switch, Light Switch, Insight Switch and Motion
- Command-line tool to discover and control devices in your environment
- REST API to obtain information and perform actions on devices
- Simple responsive Web app provides device control on mobile
- Python API to interact with device at a low level
}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{commit}

# Remove python shebang from __init__.py and make the version match the actual release version
sed -i -e '/^#!\//, 1d' ouimeaux/__init__.py
sed -i 's|[0-9]\.[0-9]\.[0-9]|%{version}|' ouimeaux/__init__.py

# fix python shebang and non-executable-script errors
find \( -name device.py -or -name service.py -or -name watch.py \) -type f -exec chmod +x {} \; -exec sed -i 's\^#!/usr/bin/env python$\#!%{python3}\' {} \;

%build
%py3_build

%install
%py3_install

%check
%{python3} setup.py test

%files -n python3-%{srcname}
%license LICENSE
%doc README.md HISTORY.rst AUTHORS.rst CONTRIBUTING.rst
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/
%{_bindir}/wemo

%changelog
* Sun May 17 2020 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.8.2-1.git.6b6984b
- Initial package

