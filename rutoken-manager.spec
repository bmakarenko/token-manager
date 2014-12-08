Name: rutoken-manager
Version: 0.2
Release: 2
License: MIT
Packager: Boris Makarenko
Group: System Environment/Base
Summary: Certificate manager for CryptoPro SCP
Source0: rutoken-manager.py
Source1: rutoken-manager.png
Source2: rutoken-manager.desktop
Source3: cpconfig-pam
Source4: cpconfig-amd64
Source5: cpconfig-ia32

Requires: PyQt4
BuildArch:  noarch

%description
A PyQt front-end for Crypto Pro CSP for CentOS 6 and GosLinux by The Federal Bailiffs' Service of Russia


%install
mkdir -p %{buildroot}{_bindir}
ln -sf /usr/bin/consolehelper %{buildroot}%{_bindir}/cpconfig-amd64
ln -sf /usr/bin/consolehelper %{buildroot}%{_bindir}/cpconfig-ia32
%{__install} -m 0644 %{SOURCE0} %{buildroot}%{_bindir}/rutoken-manager.py
mkdir -p %{buildroot}{_datadir}/pixmaps
mkdir -p %{buildroot}{_datadir}/applications
%{__install} -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/rutoken-manager.png
%{__install} -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/applications/rutoken-manager.desktop
mkdir -p %{buildroot}%{_sysconfdir}/pam.d
mkdir -p %{buildroot}%{_sysconfdir}/security/console.apps
%{__install} -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/pam.d/cpconfig-amd64
%{__install} -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/pam.d/cpconfig-ia32
%{__install} -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/security/console.apps/cpconfig-amd64
%{__install} -m 0644 %{SOURCE5} %{buildroot}%{_sysconfdir}/security/console.apps/cpconfig-ia32


%files
%{_bindir}/cpconfig-amd64
%{_bindir}/cpconfig-ia32
%{_bindir}/rutoken-manager.py
%{_datadir}/pixmaps/rutoken-manager.png
%{_datadir}/applications/rutoken-manager.desktop
%{_sysconfdir}/pam.d/cpconfig-amd64
%{_sysconfdir}/pam.d/cpconfig-ia32
%{_sysconfdir}/security/console.apps/cpconfig-amd64
%{_sysconfdir}/security/console.apps/cpconfig-ia32


%changelog
* Thu Dec 04 2014 Boris Makarenko <bmakarenko90@gmail.com>
- Initial build
