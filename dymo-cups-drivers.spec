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
# https://github.com/matthiasbock/dymo-cups-drivers/commit/2433fa303dd9925f8b36b18406863c56766c651b
Patch1: dymo-cups-drivers-replace-boolean-or-with-bitwise.patch
# https://github.com/matthiasbock/dymo-cups-drivers/commit/d7ef90a48c61c898a3d69f353673d81d7540c892
Patch2: dymo-cups-drivers-unused-var-statusok.patch
# https://github.com/matthiasbock/dymo-cups-drivers/commit/697cfb8115054fb95b9e91d54d68f47ee3805060
Patch3: dymo-cups-drivers-replace-deprecated-type.patch

# Patch files obtained from printer-driver-dymo Debian source package
Patch4: 0001-Inheritate-CXXFLAGS-from-the-environment-to-use-dpkg.patch
Patch5: 0002-Port-to-newer-cups-headers-ppd_file_t-is-only-define.patch

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
autoreconf --force --install
# Must enable c++11 for el7
%{configure} CXXFLAGS="${CXXFLAGS} -std=c++11"
%make_build

%install
%make_install

%files
%license LICENSE
%doc AUTHORS ChangeLog COPYING README docs/ samples/
%{_cups_serverbin}/filter/
%{_datadir}/cups/

%changelog
* Mon Jan 07 2019 Andrew Bauer <zonexpertconsulting@outlook.com> - 1.4.0.5-3
- fix typo calling configure macro
- add license and doc files
- use _cups_serverbin macro
- use autoreconf

* Mon Nov 26 2018 Andrew Bauer <zonexpertconsulting@outlook.com> - 1.4.0.5-2
- Add gcc buildrequires for f29

* Sat Sep 1 2018 Andrew Bauer <zonexpertconsulting@outlook.com> - 1.4.0.5-1
- Initial specfile
