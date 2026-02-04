%global srcname CxxUrl

%global commit_date     20241201
%global commit_long     eaf46c0207df24853a238d4499e7f4426d9d234c
%global commit_short    %(c=%{commit_long}; echo ${c:0:7})

Name:              cxxurl
Version:           0.3
Release:           1.%{commit_date}git%{commit_short}%{dist}
Summary:           A simple C++ URL class
License:           MIT
URL:               https://github.com/chmike/CxxUrl
Source0:           %{url}/archive/%{commit_long}/%{name}-%{commit_long}.tar.gz

# Per i686 leaf package policy 
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:     gcc-c++
BuildRequires:     cmake

%description
The cxxurl library provides a C++ URL handling class with a very simple API.
Its use is straightforward. URIs that don't follow the URL standard defined
in RFC3986 might not be correctly parsed in all cases.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p 1 -n %{srcname}-%{commit_long}

%build
%cmake \
       -DENABLE_INSTALL=ON \
       -DCxxUrl_BUILD_STATIC_LIBS=OFF

%cmake_build

%install
%cmake_install

%check
# no tests available

%files
%license LICENSE
%doc README.md
%{_libdir}/lib%{srcname}.so.1{,.*}

%files devel
%{_libdir}/lib%{srcname}.so
%dir %{_libdir}/cmake/%{srcname}
%{_libdir}/cmake/%{srcname}/*.cmake
%{_includedir}/%{srcname}/url.hpp
%{_includedir}/%{srcname}/string.hpp

%changelog
* Wed Feb 04 2026 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.3-1.20241201giteaf46c0
- initial specfile

