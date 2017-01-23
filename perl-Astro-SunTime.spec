Name:      perl-Astro-SunTime
Summary:   Calculates sun rise/set times 
Version:   0.05
Release:   2%{?dist}
License:   GPLv3
Group:     Development/Libraries
URL:       http://search.cpan.org/dist/Astro-SunTime/
Source:    http://www.cpan.org/CPAN/authors/id/R/RO/ROBF/Astro-SunTime-%{version}.tar.gz
BuildArch: noarch

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl
BuildRequires: perl-generators
BuildRequires: findutils

# Needed during build for the perl test
BuildRequires: perl(Test)
BuildRequires: perl(POSIX)
BuildRequires: perl(strict)
BuildRequires: perl(Time::ParseDate)
BuildRequires: perl(vars)

Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:  perl(Time::ParseDate)

%description
Astro::SunTime Perl module provides a function interface to calculate sun
rise/set times.

%prep
%autosetup -n Astro-SunTime-%{version}

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
%doc Changes README
%dir %{perl_vendorlib}/Astro
%{perl_vendorlib}/Astro/SunTime.pm

%changelog
* Mon Jan 23 2017 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.05-2
- Add perl(Time::ParseDate) requires. It is not autodetected.

* Fri Jan 20 2017 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.05-1
- Update to release 0.05
- Added Perl(Test) buildrequries to run new tests in 0.05 release

* Tue Jan 03 2017 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.01-5
- Additional feedback from bugzilla 1409869

* Tue Jan 03 2017 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.01-4
- bugzilla 1409869 feedback applies to this package too

* Mon Jan 02 2017 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.01-3
- Add perl-generators buildrequires 
- move make test to %%check

* Sun Jan 01 2017 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.01-2
- Update spec file to modern Fedora packaging guidelines 

* Fri Aug 23 2013 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.01-1
- Initial build using cpan2rpm.
