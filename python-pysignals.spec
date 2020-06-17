%global srcname pysignals

Name: python-%{srcname}
Version: 0.1.2
Release: 2%{?dist}
Summary: PySignals is a signal dispatcher for Python

License: BSD
Url: https://pypi.org/project/pysignals/
Source0: %pypi_source
Source1: https://raw.githubusercontent.com/theojulienne/PySignals/master/LICENSE.txt

# https://github.com/knight-of-ni/PySignals/commit/5912d4ecdc9d8cedb4e813dacc6fa5b22f01cf5c.patch
Patch0:  python-pysignals-py3compat.patch

BuildArch: noarch

BuildRequires:  python3-devel

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
%autosetup -p 1 -n %{srcname}-%{version}

install -pm 0644 %{SOURCE1} .

%build
%py3_build

%install
%py3_install

%check
%{python3} setup.py test

%files -n python3-%{srcname}
%license LICENSE.txt
%doc PKG-INFO
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/

%changelog
* Wed Jun 17 2020 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.1.2-2
- Add LICENSE.txt from upstream

* Wed Jun 17 2020 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.1.2-1
- Initial package

