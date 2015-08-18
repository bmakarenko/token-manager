Name: token-manager
Version: 0.7
Release: 1
License: MIT
Packager: Boris Makarenko
Group: System Environment/Base
Summary: Certificate manager for CryptoPro CSP
Source0: token-manager.py
Source1: token-manager.png
Source2: token-manager.desktop
Source3: cpconfig-pam
Source4: cpconfig-amd64
Source5: cpconfig-ia32

Requires: PyQt4, usermode, opensc
BuildArch: noarch

%description
A PyQt front-end for Crypto Pro CSP for CentOS 6 and GosLinux by The Federal Bailiffs' Service of Russia


%install
mkdir -p %{buildroot}/%{_bindir}
ln -sf /usr/bin/consolehelper %{buildroot}%{_bindir}/cpconfig-amd64
ln -sf /usr/bin/consolehelper %{buildroot}%{_bindir}/cpconfig-ia32
%{__install} -m 0644 %{SOURCE0} %{buildroot}%{_bindir}/token-manager.py
mkdir -p %{buildroot}/%{_datadir}/pixmaps
mkdir -p %{buildroot}/%{_datadir}/applications
%{__install} -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/token-manager.png
%{__install} -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/applications/token-manager.desktop
mkdir -p %{buildroot}/%{_sysconfdir}/pam.d
mkdir -p %{buildroot}/%{_sysconfdir}/security/console.apps
%{__install} -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/pam.d/cpconfig-amd64
%{__install} -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/pam.d/cpconfig-ia32
%{__install} -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/security/console.apps/cpconfig-amd64
%{__install} -m 0644 %{SOURCE5} %{buildroot}%{_sysconfdir}/security/console.apps/cpconfig-ia32


%files
%{_bindir}/cpconfig-amd64
%{_bindir}/cpconfig-ia32
%{_bindir}/token-manager.py
%{_datadir}/pixmaps/token-manager.png
%{_datadir}/applications/token-manager.desktop
%{_sysconfdir}/pam.d/cpconfig-amd64
%{_sysconfdir}/pam.d/cpconfig-ia32
%{_sysconfdir}/security/console.apps/cpconfig-amd64
%{_sysconfdir}/security/console.apps/cpconfig-ia32


%changelog
* Tue Dec 24 2014 Boris Makarenko <bmakarenko90@gmail.com>
- Release 0.7
- Added cache PIN feature

* Tue Dec 24 2014 Boris Makarenko <bmakarenko90@gmail.com>
- Release 0.6
- Display CSP version
- Obsolete CSP version warning

* Tue Dec 24 2014 Boris Makarenko <bmakarenko90@gmail.com>
- Release 0.5
- Added delete container feature

* Tue Dec 23 2014 Boris Makarenko <bmakarenko90@gmail.com>
- Release 0.4
- Added change PIN feature

* Fri Dec 19 2014 Boris Makarenko <bmakarenko90@gmail.com>
- Release 0.3
- View installed root certificates and CRLs

* Mon Dec 08 2014 Boris Makarenko <bmakarenko90@gmail.com>
- Release 0.2
- Added features: Set license, View license, Install root certificate, Install CRL

* Thu Dec 04 2014 Boris Makarenko <bmakarenko90@gmail.com>
- Initial build
