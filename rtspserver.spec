%global srcname RtspServer

%global commit_date     20260131
%global commit_long     24e6b7153aa561ecc4123cc7c8fc1b530cde0bc9
%global commit_short    %(c=%{commit_long}; echo ${c:0:7})

Name:              rtspserver
Version:           1.0.0^%{commit_date}git%{commit_short}
Release:           1%{dist}
Summary:           A RTSP server and pusher based on C++11
License:           MIT
URL:               https://github.com/ZoneMinder/RtspServer
Source0:           %{url}/archive/%{commit_long}/%{name}-%{commit_long}.tar.gz

# Per i686 leaf package policy 
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:     gcc-c++
BuildRequires:     cmake
BuildRequires:     sed

%description
A RTSP server and pusher based on C++11. This is a fork of the original
project by PHZ76. It includes bug fixes and improvements, such as AV1 support.

Features
--------
Support AV1/H.264/H.265/G711A/AAC
Support unicast(rtp over udp, rtp over rtsp), multicast
Support digest authentication

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p 1 -n %{srcname}-%{commit_long}

# Build shared libraries
sed -i 's/STATIC/SHARED/' CMakeLists.txt
head -n -4 CMakeLists.txt > temp.txt && mv temp.txt CMakeLists.txt

%build
%cmake

%cmake_build

%install
%cmake_install

%check
# not tests available

%files
%license LICENSE
%doc README.md
%{_libdir}/lib%{srcname}.so

%files devel
%doc example/
%doc pic/

%changelog
* Sat Feb 14 2026 Andrew Bauer <zonexpertconsulting@outlook.com> - 1.0.0^20260214git24e6b71-1
- initial specfile

