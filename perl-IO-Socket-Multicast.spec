Name:		perl-IO-Socket-Multicast
Version:	1.12
Release:	1%{?dist}
Summary:	Perl library for sending and receiving multicast messages
Group:		Development/Libraries
License:	GPL+ or Artistic
URL:		http://search.cpan.org/dist/IO-Socket-Multicast/
Source0:	http://search.cpan.org/CPAN/authors/id/B/BR/BRAMBLE/IO-Socket-Multicast-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(id -nu)
BuildRequires:	perl(ExtUtils::MakeMaker), perl(Test::Simple)
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:	perl(IO::Interface) >= 0.94

%description
The IO::Socket::Multicast module sub-classes IO::Socket::INET to enable
you to manipulate multicast groups. With this module (and an operating
system that supports multicast), you will be able to receive incoming
multicast transmissions and generate your own outgoing multicast
packets.

%prep
%setup -q -n IO-Socket-Multicast-%{version}
chmod 644 examples/*

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} ';' 2>/dev/null
%{_fixperms} %{buildroot}

%check
make test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc Changes README examples/
%{perl_vendorarch}/auto/IO/Socket/
%{perl_vendorarch}/IO/Socket/
%{_mandir}/man3/IO::Socket::Multicast.3pm*

%changelog
* Thu Sep 1 2011 Simon Thompson <sjt@roamingzebra.co.uk> - 1.12-1
- First build
