token-manager
===============

A PyQt front-end for CryptoPro CSP for CentOS 6 and GosLinux by The Federal Bailiffs' Service of Russia

The application requires following packages to be installed before you use it(for x86_64 architecture):

PyQt4, rtSupCP-64, opensc, cprocsp-rdr-pcsc-64, lsb-cprocsp-capilite-64, opensc, cprocsp-rdr-gui or cprocsp-rdr-gui-gtk

If you have installed all of those packages, you are able to run <b>python token-manager.py</b> to use it.

Token-manager was designed for the GosLinux(not gOS) distribution by The Federal Bailiffs' Service of Russia and uses only necessary features of CryptoPro CSP. You are welcome to expand capabilites of the application by sending a pull request or forking this repository. It was also tested on Linux Mint 17. In theory it can work on any EL6 or Ubuntu-based distribution.

Building RPM package
===============
Make sure you have installed rpmbuild utility. Then you can run <b>rpmbuild.sh</b> shell-script to build RPM package. The package you can find at <your home directory>/rpmbuild/RPMS/noarch
