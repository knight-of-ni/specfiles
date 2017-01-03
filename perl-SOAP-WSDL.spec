%define real_name SOAP-WSDL

Name:      perl-SOAP-WSDL
Summary:   SOAP::WSDL perl module
Version:   3.003
Release:   4%{?dist}
License:   GPL+ or Artistic
Group:     Applications/CPAN
URL:       http://search.cpan.org/dist/SOAP-WSDL/
Source:    http://www.cpan.org/modules/by-module/SOAP/SOAP-WSDL-%{version}.tar.gz
BuildArch: noarch

Patch0: wsdl2perl.patch

BuildRequires: perl-generators
BuildRequires: perl >= 2:5.8.0
BuildRequires: perl(Class::Std::Fast) > 0.0.5
BuildRequires: perl(Cwd)
BuildRequires: perl(Date::Format)
BuildRequires: perl(Date::Parse)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Path)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(List::Util)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Storable)
BuildRequires: perl(Template)
BuildRequires: perl(Test::More)
BuildRequires: perl(XML::Parser::Expat)

Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
A WSDL-driven message preprocessor for SOAP::Lite.

%package doc
Group: Documentation
Summary: Documentation for the Perl SOAP WSDL module
Requires: %{name} = %{version}-%{release}

%description doc
The SOAP-WSDL-doc package contains the README documentation, man files,
and exmaples.

%package server
Group: Applications/CPAN
Summary: SOAP server with WSDL support
Requires: %{name} = %{version}-%{release}

%description server
The SOAP-WSDL-server pacakge contains a SOAP compliant server capable of
sending messages via the Apache2 web server.

%prep
%setup -n %{real_name}-%{version}
%patch0 -p0

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_build pure_install DESTDIR=%{buildroot}

# older Perls don't support the NO_PACKLIST flag
find %{buildroot} -type f -name .packlist -exec %{__rm} -f {} ';'

### Clean up docs
find example/ -type f -exec %{__chmod} a-x {} \;

%files
%defattr(-, root, root, 0755)
%{_bindir}/wsdl2perl.pl

%dir %{perl_vendorlib}/SOAP/

%{perl_vendorlib}/SOAP/WSDL/SOAP/
%{perl_vendorlib}/SOAP/WSDL/XSD/
%{perl_vendorlib}/SOAP/WSDL/Manual/
%{perl_vendorlib}/SOAP/WSDL/Factory/
%{perl_vendorlib}/SOAP/WSDL/Serializer/
%{perl_vendorlib}/SOAP/WSDL/Deserializer/
%{perl_vendorlib}/SOAP/WSDL/Expat/
%{perl_vendorlib}/SOAP/WSDL/Client/
%{perl_vendorlib}/SOAP/WSDL/Generator/
%{perl_vendorlib}/SOAP/WSDL/Transport/
%{perl_vendorlib}/SOAP/*.pm
%{perl_vendorlib}/SOAP/WSDL/*.pm
%{perl_vendorlib}/SOAP/WSDL/*.pod
%{perl_vendorlib}/SOAP/test_html.pl

%files doc
%defattr(-, root, root, 0755)
%doc Changes HACKING LICENSE MANIFEST META.yml README TODO example/
%doc %{_mandir}/man1/wsdl2perl.pl.1*
%doc %{_mandir}/man3/SOAP::WSDL.3pm*
%doc %{_mandir}/man3/SOAP::WSDL::*.3pm*

%files server
%defattr(-, root, root, 0755)
%{perl_vendorlib}/SOAP/WSDL/Server/

%changelog
* Tue Jan 03 2017 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.01-4
- Add perl-generators buildrequires 
- update to modern Fedora packaging standards

* Tue Dec 13 2016 Andrew Bauer <knnniggett@users.sourceforge.net> - 3.00.3-3
- Rebuild to fix an issue with rpm provides 

* Wed Nov 9 2016 Andrew Bauer <knnniggett@users.sourceforge.net> - 3.00.3-2
- Break into subpackages, primarily to separate portions dependant on Apache2

* Fri Jun 17 2016 Andrew Bauer <knnniggett@users.sourceforge.net> - 3.00.3-1
- Updated to release 3.00.3.

* Thu Jun 18 2009 Christoph Maser <cmr@financial.com> - 2.00.10-1 - 7981/dag
- Updated to release 2.00.10.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 2.00.01-1
- Updated to release 2.00.01.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 1.27-1
- Updated to release 1.27.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 1.26-1
- Updated to release 1.26.

* Wed Dec 29 2004 Dries Verachtert <dries@ulyssis.org> - 1.20-1
- Updated to release 1.20.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 1.18-1
- Initial package.
