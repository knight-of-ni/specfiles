Name:      perl-X10
Summary:   X10 perl module
Version:   0.03
Release:   4%{?dist}
License:   GPL+ or Artistic
Group:     Applications/CPAN
URL:       http://search.cpan.org/dist/X10/
Source:    http://search.cpan.org/CPAN/authors/id/R/RO/ROBF/X10-%{version}.tar.gz
Buildarch: noarch

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl-generators

# Needed during build for the perl test
BuildRequires: perl(Astro::SunTime) perl(Time::ParseDate) perl(Device::SerialPort)
BuildRequires: perl(File::Basename) perl(FileHandle) perl(IO::Select)
BuildRequires: perl(IO::Socket) perl(POSIX) perl(Storable) perl(Data::Dumper)

Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires: perl(Astro::SunTime) perl(Time::ParseDate) perl(Device::SerialPort)
Requires: perl(File::Basename) perl(FileHandle) perl(IO::Select)
Requires: perl(IO::Socket) perl(POSIX) perl(Storable) perl(Data::Dumper)

%description
X10 perl module for the Firecracker, ActiveHome, and TwoWay/TW523 interfaces.

%prep
%autosetup -n X10-%{version}

%build
# PMLIBDIRS intentionally reset to avoid placing config & doc files into the vendorlib folder
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 PMLIBDIRS=
%make_build

%install
%make_build pure_install DESTDIR=%{buildroot}
# older Perls don't support the NO_PACKLIST flag
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'

%check
%make_build test

%files
%doc Changes MANIFEST README TODO test.pl
%doc devices macros.config ports scheduler.config

%{_bindir}/x10client
%{_bindir}/x10server

%{perl_vendorlib}/X10.pm
%{perl_vendorlib}/X10/

%changelog
* Mon Jan 02 2017 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.03-3
- Add perl-generators buildrequires
- Move make test to %check

* Sun Jan 01 2017 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.03-2
- Update spec file to modern Fedora packaging guidelines 

* Fri Aug 23 2013 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.03-1
- Initial build using cpan2rpm.
