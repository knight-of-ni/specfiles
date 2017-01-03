%define real_name Class-Std

Name:      perl-Class-Std
Summary:   Class::Std perl module
Version:   0.0.9
Release:   2%{?dist}
License:   GPL+ or Artistic
Group:     Applications/CPAN
URL:       http://search.cpan.org/dist/Class-Std/
Source:    http://www.cpan.org/CPAN/authors/id/C/CH/CHORNY/Class-Std-%{version}.tar.gz
BuildArch: noarch

BuildRequires: perl-generators
BuildRequires: perl(ExtUtils::MakeMaker)

Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module provides tools that help to implement the 
"inside out object" class structure in a convenient and standard way.

Portions of the following code and documentation from 
"Perl Best Practices" copyright (c) 2005 by O'Reilly Media, Inc. 
and reprinted with permission.

%prep
%autosetup -n %{real_name}-%{version}

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
%doc %{_mandir}/man3/Class::Std.3pm*
%dir %{perl_vendorlib}/Class/
%{perl_vendorlib}/Class/Std.pm

%changelog
* Mon Jan 02 2017 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.0.9-2
- Add perl-generators buildrequires
- update to modern Fedora packaging standards

* Sat May 03 2008 Dag Wieers <dag@wieers.com> - 0.0.9-1 - 7981/dag
- Updated to release 0.0.9.

* Fri Jun 29 2007 Quien Sabe (aka Jim) <quien-sabe@metaorg.com> - 0.0.8-1
- Initial package.
