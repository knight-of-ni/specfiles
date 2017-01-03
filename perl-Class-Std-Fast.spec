%define real_name Class-Std-Fast

Name:      perl-Class-Std-Fast
Summary:   Class::Std perl module
Version:   0.0.8
Release:   4%{?dist}
License:   GPL+ or Artistic
Group:     Applications/CPAN
URL:       http://search.cpan.org/dist/Class-Std-Fast/
Source:    http://www.cpan.org/CPAN/authors/id/A/AC/ACID/Class-Std-Fast-v%{version}.tar.gz
BuildArch: noarch

BuildRequires: perl-generators
BuildRequires: perl(Test::More)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Class::Std)

Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
# rpm does not pick this up automagically
Requires: perl(Class::Std)

%description
Faster but less secure than Class::Std.

%prep
%autosetup -n %{real_name}-v%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_build pure_install DESTDIR=%{buildroot}

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Class::Std::Fast.3pm*
%doc %{_mandir}/man3/Class::Std::Fast::*.3pm*
%dir %{perl_vendorlib}/Class/
%dir %{perl_vendorlib}/Class/Std/
%{perl_vendorlib}/Class/Std/Fast/
%{perl_vendorlib}/Class/Std/Fast.pm

%changelog
* Mon Jan 02 2017 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.08-4
- Add perl-generators buildrequires
- modernize perl and make macros 
- change contact email

* Fri Nov 25 2016 Andrew Bauer <knnniggett@sourceforge.net> - 0.0.8-3
- Rebuild for zmrepo.
- Add perl(fast::std) buildrequires to fix mock build issue

* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 0.0.8-1 - 7981/dag
- Updated to release 0.0.8.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 0.0.6-1
- Initial package. (using DAR)
