# IMPORTANT
# This is simplified drupal9 specfile, which does not use php composer or symfony as they are not available in all epel repos
# Portions of this specfile borrowed from the Drupal 8 specfile written by Shawn Iwinski <shawn@iwin.ski>

# Build using "--with tests" to enable tests
%global with_tests 0%{?_with_tests:1}

# drupal 9 requires php 7.3 or newer
%global php_min_ver 7.3.0

Name:      drupal9
Version:   9.1.3
Release:   1%{?dist}
Summary:   An open source content management platform
License:   GPLv2+
URL:       https://www.drupal.org/9
Source0:   http://ftp.drupal.org/files/projects/drupal-%{version}.tar.gz
Source1:   %{name}-prep-licenses-and-docs.sh

BuildArch: noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  sed
BuildRequires:  grep
BuildRequires:  php-cli

# A basic set of runtime requirements which may not be complete
Requires:  php-common >= %{php_min_ver}
Requires:  php-cli >= %{php_min_ver}
Requires:  php-fpm >= %{php_min_ver}
Requires:  php-gd >= %{php_min_ver}
Requires:  php-mysqlnd >= %{php_min_ver}
Requires:  php-mbstring >= %{php_min_ver}
Requires:  php-json >= %{php_min_ver}
Requires:  php-common >= %{php_min_ver}
Requires:  php-dba >= %{php_min_ver}
Requires:  php-dbg >= %{php_min_ver}
Requires:  php-devel >= %{php_min_ver}
Requires:  php-embedded >= %{php_min_ver}
Requires:  php-enchant >= %{php_min_ver}
Requires:  php-bcmath >= %{php_min_ver}
Requires:  php-gmp >= %{php_min_ver}
Requires:  php-intl >= %{php_min_ver}
Requires:  php-ldap >= %{php_min_ver}
Requires:  php-odbc >= %{php_min_ver}
Requires:  php-pdo >= %{php_min_ver}
Requires:  php-opcache >= %{php_min_ver}
Requires:  php-pear >= %{php_min_ver}
Requires:  php-pgsql >= %{php_min_ver}
Requires:  php-process >= %{php_min_ver}
Requires:  php-recode >= %{php_min_ver}
Requires:  php-snmp >= %{php_min_ver}
Requires:  php-soap >= %{php_min_ver}
Requires:  php-xml >= %{php_min_ver}
Requires:  php-xmlrpc >= %{php_min_ver}

%description
Drupal is an open source content management platform powering millions of
websites and applications. It’s built, used, and supported by an active and
diverse community of people around the world.

%prep
%autosetup -n drupal-%{version}
mkdir .rpm
cp -p %{SOURCE1} .rpm/

# Remove unneeded files
rm -rf vendor core/vendor
rm -f core/composer.json
find . -name '.git*' -delete -print
find . -name 'web.config' -delete -print

# Licenses and docs
.rpm/%{name}-prep-licenses-and-docs.sh
mv core/INSTALL.*.* .rpm/docs/core/

# Move license and doc files required at runtime back in place
mv .rpm/docs/core/modules/system/tests/fixtures/HtaccessTest/composer.* \
    core/modules/system/tests/fixtures/HtaccessTest/
rmdir .rpm/docs/core/modules/system/tests/fixtures/HtaccessTest
rmdir .rpm/docs/core/modules/system/tests/fixtures
cp .rpm/docs/core/INSTALL.txt core/

# Remove all empty license and doc files
find .rpm/{licenses,docs}/ -type f -size 0 -delete -print

# Apache .htaccess
sed 's!# RewriteBase /$!# RewriteBase /\n  RewriteBase /drupal9!' \
    -i .htaccess

# Update php bin
sed 's#/bin/php#%{_bindir}/php#' \
    -i core/scripts/update-countries.sh

# Fix "non-executable-script" rpmlint errors
chmod +x core/scripts/*.{php,sh}

# Fix "script-without-shebang" rpmlint errors
chmod -x core/scripts/run-tests.sh

%build
# nothing to build

%install
# Main
mkdir -p %{buildroot}%{_datadir}/drupal9
cp -pr * %{buildroot}%{_datadir}/drupal9/

# Sites
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/sites
mv %{buildroot}%{_datadir}/drupal9/sites/* %{buildroot}%{_sysconfdir}/%{name}/sites/
rmdir %{buildroot}%{_datadir}/drupal9/sites
ln -s %{_sysconfdir}/%{name}/sites %{buildroot}%{_datadir}/drupal9/sites

# Files
mkdir -p %{buildroot}%{_localstatedir}/lib/%{name}/files/{public,private}/default
ln -s %{_localstatedir}/lib/%{name}/files/public/default \
    %{buildroot}%{_sysconfdir}/%{name}/sites/default/files

# Robots
mv %{buildroot}%{_datadir}/drupal9/robots.txt %{buildroot}%{_sysconfdir}/%{name}/
ln -s %{_sysconfdir}/%{name}/robots.txt %{buildroot}%{_datadir}/drupal9/robots.txt

%check
# Version check
%{_bindir}/php -r '
    require_once "%{buildroot}%{_datadir}/drupal9/core/lib/Drupal.php";
    $version = \Drupal::VERSION;
    echo "Version $version (expected %{version})\n";
    exit(version_compare("%{version}", "$version", "=") ? 0 : 1);
'

# Ensure php bin updated
! grep -r '#!/bin/php' .

%if %{with_tests}
pushd core
    # Unit tests
    %{_bindir}/phpunit
popd
%else
# Test suite skipped
%endif

%files
%license .rpm/licenses/*
%doc .rpm/docs/*
%config(noreplace) %{_sysconfdir}/%{name}/robots.txt
%ghost %{_datadir}/drupal9/sites/default/settings.php

%{_datadir}/drupal9/
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/sites
%config(noreplace) %{_sysconfdir}/%{name}/sites/development.services.yml
%dir %{_sysconfdir}/%{name}/sites/default
## Managed upstream example/default configs
%config %{_sysconfdir}/%{name}/sites/example.*
%config %{_sysconfdir}/%{name}/sites/default/default.*
# Files
%{_sysconfdir}/%{name}/sites/default/files
%dir %{_localstatedir}/lib/%{name}
%dir %{_localstatedir}/lib/%{name}/files
%dir %{_localstatedir}/lib/%{name}/files/private
%dir %{_localstatedir}/lib/%{name}/files/public

%changelog
* Sat Jan 30 2021 Andrew Bauer <zonexpertconsulting@outlook.com> - 9.1.3-1
- Initial specfile for drupal 9

