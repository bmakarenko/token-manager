Name: token-manager
Version: 0.10
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
* Wed Jul 06 2016 Boris Makarenko <bmakarenko90@gmail.com> - 0.10
- Release 0.10-1
- Filter list of root certificates and CRLs

* Wed May 04 2016 Boris Makarenko <bmakarenko90@gmail.com> - 0.10
- Release 0.10
- Displaying the token's serial number

* Tue Feb 09 2016 Boris Makarenko <bmakarenko90@gmail.com> - 0.9
- Release 0.9
- Personal and root certificate storages
- Displaying complete and translated into Russian info about certificates

* Wed Feb 03 2016 Boris Makarenko <bmakarenko90@gmail.com> - 0.8
- Release 0.8
- Hardware reader setup
- Remastered viewer windows

* Thu Aug 06 2015 Boris Makarenko <bmakarenko90@gmail.com> - 0.7
- Release 0.7
- Added cache PIN feature

* Wed Mar 18 2015 Boris Makarenko <bmakarenko90@gmail.com> - 0.6
- Release 0.6
- Display CSP version
- Obsolete CSP version warning

* Wed Dec 24 2014 Boris Makarenko <bmakarenko90@gmail.com> - 0.5
- Release 0.5
- Added delete container feature

* Tue Dec 23 2014 Boris Makarenko <bmakarenko90@gmail.com> - 0.4
- Release 0.4
- Added change PIN feature

* Fri Dec 19 2014 Boris Makarenko <bmakarenko90@gmail.com> - 0.3
- Release 0.3
- View installed root certificates and CRLs

* Mon Dec 08 2014 Boris Makarenko <bmakarenko90@gmail.com> - 0.2
- Release 0.2
- Added features: Set license, View license, Install root certificate, Install CRL

* Thu Dec 04 2014 Boris Makarenko <bmakarenko90@gmail.com> - 0.1
- Initial build
