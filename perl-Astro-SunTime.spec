%global debug_package %{nil}

Name:      perl-Astro-SunTime
Summary:   Astro::SunTime perl module
Version:   0.01
Release:   3%{?dist}
License:   GPL+ or Artistic
Group:     Applications/CPAN
URL:       http://search.cpan.org/dist/Astro-SunTime/
Source:    http://www.cpan.org/CPAN/authors/id/R/RO/ROBF/Astro-SunTime-%{version}.tar.gz
BuildArch: noarch

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Time::ParseDate)
BuildRequires: perl-generators

Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Astro::SunTime perl module provides a function interface to calculate sun rise/set times.

%prep
%autosetup -n Astro-SunTime-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%check
%make_build test

%install
%make_build pure_install DESTDIR=%{buildroot}
# older Perls don't support the NO_PACKLIST flag
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'

%files
%doc Changes MANIFEST README test.pl
%{perl_vendorlib}/Astro/SunTime.pm

%changelog
* Mon Jan 02 2017 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.01-3
- Add perl-generators buildrequires 
- move make test to %check

* Sun Jan 01 2017 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.01-2
- Update spec file to modern Fedora packaging guidelines 

* Fri Aug 23 2013 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.01-1
- Initial build using cpan2rpm.
