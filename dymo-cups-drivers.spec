%global short_version 1.4.0

Name: dymo-cups-drivers
Version: %{short_version}.5
Release: 3%{?dist}
Summary: DYMO LabelWriter Drivers for CUPS
Group: System Environment/Libraries
License: GPLv2
URL: http://www.dymo.com

Source0: http://download.dymo.com/dymo/Software/Download%20Drivers/Linux/Download/dymo-cups-drivers-%{short_version}.tar.gz#/%{name}-%{version}.tar.gz

# https://github.com/matthiasbock/dymo-cups-drivers/pull/6
Patch0: dymo-cups-drivers-fix-fsf-address.patch

# Patch files obtained from printer-driver-dymo Debian source package
Patch1: 0001-Inheritate-CXXFLAGS-from-the-environment-to-use-dpkg.patch
Patch2: 0002-Port-to-newer-cups-headers-ppd_file_t-is-only-define.patch

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: cups-devel
BuildRequires: glibc-headers
BuildRequires: libtool
BuildRequires: gcc-c++
BuildRequires: sed

Requires: cups

%description
DYMO LabelWriter and DYMO LabelMANAGER series drivers for CUPS

%prep
%autosetup -p 1

# fix wrong-file-end-of-line-encoding
sed -i 's/\r$//' COPYING

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake} --force-missing --add-missing
%{__autoconf}
%{configure}
%make_build

%install
%make_install

%files
%license LICENSE
%doc AUTHORS ChangeLog COPYING README docs/ samples/
%{_cups_serverbin}/filter/
%{_datadir}/cups/

%changelog
* Fri Dec 14 2018 Andrew Bauer <zonexpertconsulting@outlook.com> - 1.4.0.5-3
- fix typo calling configure macro
- add license and doc files
- use _cups_serverbin macro

* Mon Nov 26 2018 Andrew Bauer <zonexpertconsulting@outlook.com> - 1.4.0.5-2
- Add gcc buildrequires for f29

* Sat Sep 1 2018 Andrew Bauer <zonexpertconsulting@outlook.com> - 1.4.0.5-1
- Initial specfile
