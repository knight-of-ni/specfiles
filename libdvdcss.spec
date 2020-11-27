Summary:    A portable abstraction library for DVD decryption
Name:       libdvdcss
Version:    1.4.2
Release:    2%{?dist}
License:    GPLv2+
Source:     http://www.videolan.org/pub/videolan/libdvdcss/%{version}/libdvdcss-%{version}.tar.bz2
URL:        http://www.videolan.org/libdvdcss/

BuildRequires: doxygen
BuildRequires: gcc


%description
This is a portable abstraction library for DVD decryption which is used by
the VideoLAN project, a full MPEG2 client/server solution.  You will need
to install this package in order to have encrypted DVD playback with the
VideoLAN client and the Xine navigation plugin.


%package devel
Summary:     Header files and development libraries for %{name}
Requires:    %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the header files and development libraries
for %{name}. If you like to develop programs using %{name}, 
you will need to install %{name}-devel.


%prep
%setup -q


%build
%configure --disable-static
make %{_smp_mflags}


%install
make install DESTDIR=%{buildroot}

# remove generated doc from build
mv %{buildroot}/usr/share/doc/libdvdcss docdir

# Remove all libtool archives
find %{buildroot} -regex ".*\.la$" -delete



%if 0%{?fedora} < 28 && 0%{?rhel} < 8
%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%endif


%files
%license COPYING
%doc AUTHORS ChangeLog README
%{_libdir}/%{name}.so.2*

%files devel
%doc docdir/*
%{_includedir}/dvdcss
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Sun Apr 01 2018 josef radinger <cheese@nosuchhost.net> - 1.4.2-2
- bump version

* Fri Mar 23 2018 Remi Collet <remi@remirepo.net> - 1.4.2-1
- Update to 1.4.2

* Mon Feb 26 2018 Remi Collet <remi@remirepo.net> - 1.4.1-2
- drop ldconfig scriptlets on F28+

* Thu Feb 01 2018 Xavier Bachelot <xavier@bachelot.org> - 1.4.1-1
- Update to 1.4.1.
- Clean up spec.

* Fri Dec 18 2015 Remi Collet <remi@remirepo.net> - 1.4.0-1
- Update to 1.4.0

* Sun Aug 17 2014 Remi Collet <remi@remirepo.net> - 1.3.0-1
- Update to 1.3.0

* Wed Feb 27 2013 Remi Collet <remi@remirepo.net> - 1.2.13-1
- Update to 1.2.13

* Mon Mar 12 2012 Remi Collet <remi@remirepo.net> - 1.2.12-1
- Update to 1.2.12

* Sat Feb 18 2012 Remi Collet <remi@remirepo.net> - 1.2.11-2
- If unsure, assume the drive is of RPC-I type

* Mon Nov 21 2011 Remi Collet <remi@remirepo.net> - 1.2.11-1
- Update to 1.2.11

* Sat Oct 16 2010 Remi Collet <remi@remirepo.net> - 1.2.10-1
- F-14 rebuild

* Sun Sep 28 2008 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.2.10-4
- Update to 1.2.10.

* Tue Sep 12 2006 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.2.9-3
- Update to 1.2.9.

* Sun Aug  3 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.2.8.

* Wed Jun 25 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.2.7.

* Mon Mar 31 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Rebuilt for Red Hat Linux 9.
- Exclude .la file.

* Tue Mar 11 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.2.6.

* Mon Feb  3 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.2.5.

* Fri Nov 15 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.2.4.

* Mon Oct 21 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.2.3.

* Thu Sep 26 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Rebuilt for Red Hat Linux 8.0.

* Mon Aug 12 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.2.2.

* Mon Jun  3 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.2.1.

* Fri May 24 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.2.0.

* Thu May  2 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Rebuilt against Red Hat Linux 7.3.
- Added the %%{?_smp_mflags} expansion.

* Mon Apr  8 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.1.1.

* Sun Nov  4 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Changed to the Ogle patched version of the lib.

* Mon Oct 22 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Initial RPM release.
- Decided to put libdvdcss in a separate package since both videolan and the
  xine DVD menu plugin use it.

