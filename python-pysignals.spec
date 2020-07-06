%global srcname pysignals

Name: python-%{srcname}
Version: 0.1.3
Release: 1%{?dist}
Summary: PySignals is a signal dispatcher for Python

License: BSD
Url: https://github.com/theojulienne/%{srcname}
Source0: https://github.com/theojulienne/%{srcname}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires:  python3-devel

# required for check
BuildRequires: %{py3_dist six}
BuildRequires: %{py3_dist future}

%global _description %{expand:
PySignals is a signal dispatcher for Python, extracted from “django.dispatch”
in the Django framework so it can be used in applications without requiring
the entire Django framework to be installed.
}

%description %_description

%package -n python3-%{srcname}

Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description

%prep
%autosetup -p 1 -n PySignals-%{version}

%build
%py3_build

%install
%py3_install

%check
%{python3} setup.py test

%files -n python3-%{srcname}
%license LICENSE.txt license.python.txt
%doc README.rst
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/

%changelog
* Sun Jul 05 2020 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.1.3-1
- Release 0.1.3
- Point source url to most recent release on github, rather than pypi

* Thu Jun 18 2020 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.1.2-3
- Update pysignals to latest django dispatch 1.9.13

* Wed Jun 17 2020 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.1.2-2
- Add LICENSE.txt from upstream

* Wed Jun 17 2020 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.1.2-1
- Initial package

