%global srcname pysignals

Name: python-%{srcname}
Version: 0.1.2
Release: 1%{?dist}
Summary: PySignals is a signal dispatcher for Python

License: BSD
Url: https://pypi.org/project/pysignals/
Source0: %pypi_source

BuildArch: noarch

BuildRequires:  python3-devel

%global _description %{expand:
PySignals is a signal dispatcher for Python, extracted from “django.dispatch”
in the Django framework so it can be used in applications without requiring
the entire Django framework to be installed.
}

%package -n python3-%{srcname}

Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description %_description

%prep
%autosetup -p 1 -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{python3} setup.py test

%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/

* Wed Jun 17 2020 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.1.2-1
- Initial package

