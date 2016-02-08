#!/bin/bash
mkdir -p ~/rpmbuild/SPEC ~/rpmbuild/SOURCES
cp token-manager.spec ~/rpmbuild/SPEC/
cp token-manager.py ~/rpmbuild/SOURCES/
cp token-manager.desktop ~/rpmbuild/SOURCES/
cp token-manager.png ~/rpmbuild/SOURCES/
cp cpconfig-amd64 ~/rpmbuild/SOURCES/
cp cpconfig-ia32 ~/rpmbuild/SOURCES/
cp cpconfig-pam ~/rpmbuild/SOURCES/
rpmbuild -ba ~/rpmbuild/SPEC/token-manager.spec
