Name:      perl-Schedule-Cron
Summary:   Provides a simple but complete cron like scheduler
Version:   1.01
Release:   1%{?dist}
License:   GPL+ or Artistic
Group:     Development/Libraries
URL:       https://metacpan.org/release/Schedule-Cron
BuildArch: noarch

Source0:   https://cpan.metacpan.org/authors/id/R/RO/ROLAND/Schedule-Cron-%{version}.tar.gz
# The following license text is included due to the "perl" license assignment
# shown in Makefile.PL
Source1:        http://dev.perl.org/licenses/#/%{name}-Licensing.html

# https://github.com/rhuss/schedule-cron/pull/8
Patch0: perl-schedule-cron-fix-unescaped-left-brace.patch
# Patch obtained from Debian libschedule-cron-perl source package
Patch1: perl-schedule-cron-fix-spelling.patch

BuildRequires:  perl-devel
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  findutils

# Needed during build for the perl test
BuildRequires: perl(Time::ParseDate)
BuildRequires: perl(Test::More)

%description
This module provides  a simple but complete cron  like scheduler.  I.e
this modules can be  used for periodically executing Perl subroutines.
The  dates  and  parameters  for  the subroutines  to  be  called  are
specified with a format known as crontab entry (see man page crontab(5)
or documentation of Schedule::Cron).

The   philosophy  behind   Schedule::Cron  is   to   call  subroutines
periodically from  within one single  Perl program instead  of letting
cron  trigger several  (possibly different)  Perl  scripts. Everything
under  one  roof.  Furthermore  Schedule::Cron  provides mechanism  to
create crontab entries dynamically, which isn't that easy with cron.

Schedule::Cron  knows  about  all   extensions  (well,  at  least  all
extensions I'm aware of, i.e those  of the so called "Vixie" cron) for
crontab entries like ranges  including 'steps', specification of month
and days of the week by name or coexistence of lists and ranges in the
same field. And  even a bit more (like lists  and ranges with symbolic
names).

This module is rather effective concerning system load.  It calculates
the execution  dates in advance and  will sleep until  those dates are
reached (and  wont wake  up every minute  to check for  execution like
cron).   However, it  relies on  the accuracy  of your  sleep() system
call.

%prep
%autosetup -p 1 -n Schedule-Cron-%{version}
cp -a %{SOURCE1} Licensing.html

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_build pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type d -empty -delete

%{_fixperms} %{buildroot}/*

%check
%make_build test

%files
%license Licensing.html
%{perl_vendorlib}/Schedule/
%{_mandir}/man3/*

%changelog
* Wed Dec 12 2018 Andrew Bauer <zonexpertconsulting@outlook.com> - 1.01-1
- Initial specfile

