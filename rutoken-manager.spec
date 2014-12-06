Name: rutoken-manager
Version: 0.1
Release: 1
License: MIT
Packager: Boris Makarenko
Group: System Environment/Base
Summary: Certificate manager for CryptoPro SCP
Source0: rutoken-manager.py
Source1: rutoken-manager.png
Source2: rutoken-manager.desktop
Requires: PyQt4, rtSupCP-64, cprocsp-rdr-pcsc-64, lsb-cprocsp-capilite-64
BuildArch:  x86_64

%description
A PyQt front-end for Crypto Pro CSP for CentOS 6 and GosLinux by The Federal Bailiffs' Service of Russia

%install
%{__install} -m 0644 %{SOURCE0} %{buildroot}%{_bindir}/rutoken-manager.py
%{__install} -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/rutoken-manager.png
%{__install} -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/applications/rutoken-manager.desktop

%files
%{_bindir}/rutoken-manager.py
%{_datadir}/pixmaps/rutoken-manager.png
%{_datadir}/applications/rutoken-manager.desktop

%changelog
* Thu Dec 04 2014 Boris Makarenko <bmakarenko90@gmail.com>
- Initial build
