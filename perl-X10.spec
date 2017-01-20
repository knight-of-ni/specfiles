Name:      perl-X10
Summary:   Enables Perl to communicate with X10 devices
Version:   0.04
Release:   1%{?dist}
License:   GPLv3
Group:     Development/Libraries
URL:       http://search.cpan.org/dist/X10/
Source:    http://search.cpan.org/CPAN/authors/id/R/RO/ROBF/X10-%{version}.tar.gz
Buildarch: noarch

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl
BuildRequires: perl-generators
BuildRequires: findutils

# Needed during build for the perl test
BuildRequires: perl(Astro::SunTime)
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(File::Basename)
BuildRequires: perl(POSIX)
BuildRequires: perl(Storable)
BuildRequires: perl(strict)
BuildRequires: perl(Time::ParseDate)
BuildRequires: perl(vars)

Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
X10 Perl module for the Firecracker, ActiveHome, and TwoWay/TW523 interfaces.

%prep
%autosetup -n X10-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_build pure_install DESTDIR=%{buildroot}
# older Perls don't support the NO_PACKLIST flag
find %{buildroot} -type f -name .packlist -delete

%check
%make_build test

%files
%doc Changes README TODO
%doc macros.config scheduler.config

%{_mandir}/man1/x10client.1*
%{_mandir}/man1/x10server.1*

# rpmlint flags non-standard-executable-perm if we don't force 755 perms
%attr(755,-,-) %{_bindir}/x10client
%attr(755,-,-) %{_bindir}/x10server

%{perl_vendorlib}/X10.pm
%{perl_vendorlib}/X10/

%changelog
* Fri Jan 20 2017 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.04-1
- Update to release 0.04
- Add man pages for executables

* Thu Jan 12 2017 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.03-5
- Additional feedback from bugzilla 1409869

* Tue Jan 03 2017 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.03-4
- bugzilla 1409869 feedback

* Mon Jan 02 2017 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.03-3
- Add perl-generators buildrequires
- Move make test to %%check

* Sun Jan 01 2017 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.03-2
- Update spec file to modern Fedora packaging guidelines 

* Fri Aug 23 2013 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.03-1
- Initial build using cpan2rpm.
