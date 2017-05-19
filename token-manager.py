#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2017 Борис Макаренко

Данная лицензия разрешает лицам, получившим копию данного программного обеспечения и сопутствующей документации
(в дальнейшем именуемыми «Программное Обеспечение»), безвозмездно использовать Программное Обеспечение без ограничений,
включая неограниченное право на использование, копирование, изменение, добавление, публикацию, распространение,
сублицензирование и/или продажу копий Программного Обеспечения, а также лицам, которым предоставляется данное
Программное Обеспечение, при соблюдении следующих условий:

Указанное выше уведомление об авторском праве и данные условия должны быть включены во все копии или значимые части
данного Программного Обеспечения.

ДАННОЕ ПРОГРАММНОЕ ОБЕСПЕЧЕНИЕ ПРЕДОСТАВЛЯЕТСЯ «КАК ЕСТЬ», БЕЗ КАКИХ-ЛИБО ГАРАНТИЙ, ЯВНО ВЫРАЖЕННЫХ ИЛИ ПОДРАЗУМЕВАЕМЫХ,
ВКЛЮЧАЯ ГАРАНТИИ ТОВАРНОЙ ПРИГОДНОСТИ, СООТВЕТСТВИЯ ПО ЕГО КОНКРЕТНОМУ НАЗНАЧЕНИЮ И ОТСУТСТВИЯ НАРУШЕНИЙ, НО НЕ
ОГРАНИЧИВАЯСЬ ИМИ. НИ В КАКОМ СЛУЧАЕ АВТОРЫ ИЛИ ПРАВООБЛАДАТЕЛИ НЕ НЕСУТ ОТВЕТСТВЕННОСТИ ПО КАКИМ-ЛИБО ИСКАМ, ЗА УЩЕРБ
ИЛИ ПО ИНЫМ ТРЕБОВАНИЯМ, В ТОМ ЧИСЛЕ, ПРИ ДЕЙСТВИИ КОНТРАКТА, ДЕЛИКТЕ ИЛИ ИНОЙ СИТУАЦИИ, ВОЗНИКШИМ ИЗ-ЗА ИСПОЛЬЗОВАНИЯ
ПРОГРАММНОГО ОБЕСПЕЧЕНИЯ ИЛИ ИНЫХ ДЕЙСТВИЙ С ПРОГРАММНЫМ ОБЕСПЕЧЕНИЕМ..

Copyright (c) 2017 Boris Makarenko

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
import os
import sys
from PyQt4 import QtCore
from PyQt4 import QtGui
import subprocess
import platform
import re
from datetime import datetime

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        """

        :param context:
        :param text:
        :param disambig:
        :return:
        """
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

qt_resource_data = "\
\x00\x00\x01\x64\
\x89\
\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d\x49\x48\x44\x52\x00\
\x00\x00\x14\x00\x00\x00\x14\x08\x06\x00\x00\x00\x8d\x89\x1d\x0d\
\x00\x00\x00\x06\x62\x4b\x47\x44\x00\xff\x00\xff\x00\xff\xa0\xbd\
\xa7\x93\x00\x00\x00\x09\x70\x48\x59\x73\x00\x00\x0d\xd7\x00\x00\
\x0d\xd7\x01\x42\x28\x9b\x78\x00\x00\x00\x07\x74\x49\x4d\x45\x07\
\xe0\x02\x08\x04\x19\x0e\x1e\x55\xe6\x6e\x00\x00\x00\xf1\x49\x44\
\x41\x54\x38\xcb\xad\xd4\xb1\x4a\x03\x41\x14\x85\xe1\xcf\x15\x6d\
\x85\x18\x6d\xc5\xce\x4a\x88\x08\x16\x29\xb5\x14\x8b\x34\x62\x25\
\xe2\xfb\xf8\x28\x42\x50\xb0\x10\xc5\xde\xc4\x60\xe7\x33\x28\x0a\
\x76\x29\xd6\x68\x33\x0b\xb2\xcc\x8e\xec\xc4\x03\xa7\x99\x99\xfb\
\x73\xe7\xcc\x70\x49\xeb\x04\x63\x7c\x04\x8f\x70\x2c\x53\x47\x98\
\xe1\xbb\xe6\x19\x0e\x73\x80\x0f\x11\x58\xe5\xfb\x1c\xe0\x7b\x02\
\xf8\xd6\x16\x56\xe0\x2b\x01\x2c\xc3\x99\x68\x61\x4c\x55\x51\x93\
\xca\x90\x65\x2b\xe0\x24\x01\x1c\xe7\x64\x78\x9e\xb8\xf2\x69\x0e\
\xb0\xc0\x30\x02\xbb\xc4\x42\xee\x5f\x5c\x0c\x9d\xde\x04\x9f\x25\
\x62\x6a\xcc\xb0\xc0\x3e\x2e\x70\x8b\x29\x06\xc1\x25\xee\xc2\xde\
\xc1\x5f\x70\xd8\xc4\x53\x22\xbb\xba\x27\xd8\x48\x75\xfb\xdc\x02\
\x56\x79\xd4\x94\x69\x3f\x03\x56\x79\x2f\x96\xe1\xb6\x7c\xf5\x62\
\xc0\xb5\x39\x80\xab\x31\x60\xe7\xbf\x81\x4b\x73\x00\x97\x63\x8b\
\x5d\x5c\x65\x3c\xc8\xf0\x77\x87\xb1\xe7\xde\x09\x13\x79\x17\x5b\
\x58\xc7\x4a\xd8\xfb\xc4\x2b\x5e\xf0\x88\xeb\xfa\x10\xf9\x01\xad\
\x71\x78\xa1\xb9\x86\xf8\x4e\x00\x00\x00\x00\x49\x45\x4e\x44\xae\
\x42\x60\x82\
\x00\x00\x01\xf4\
\x89\
\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d\x49\x48\x44\x52\x00\
\x00\x00\x14\x00\x00\x00\x14\x08\x06\x00\x00\x00\x8d\x89\x1d\x0d\
\x00\x00\x00\x06\x62\x4b\x47\x44\x00\xff\x00\xff\x00\xff\xa0\xbd\
\xa7\x93\x00\x00\x00\x09\x70\x48\x59\x73\x00\x00\x0d\xd7\x00\x00\
\x0d\xd7\x01\x42\x28\x9b\x78\x00\x00\x00\x07\x74\x49\x4d\x45\x07\
\xe0\x02\x08\x04\x0b\x1e\x7b\x16\x86\xd9\x00\x00\x01\x81\x49\x44\
\x41\x54\x38\xcb\x9d\xd4\x41\x4b\x95\x41\x14\xc6\xf1\xff\x99\xe7\
\xcc\xdc\x4d\xed\x82\x42\x4d\x45\x0c\x44\x11\xc1\x76\x2e\x22\x6a\
\x57\x1f\xa0\xb6\xb5\xc8\xef\xd1\xa6\x3e\x44\x3b\x6d\x1b\x19\xa8\
\x4b\x25\x04\xdd\x05\x45\x8b\x32\x0d\xb2\x4d\xde\x7d\xc4\xc5\x38\
\x6d\x14\x2f\xb7\xfb\xea\x9d\x3b\x70\x36\xef\x0c\xbf\x79\xe6\x30\
\xf3\xc2\x70\xe3\x8a\xcc\xdf\x66\xf2\xed\xde\x89\x34\x24\xb6\x6e\
\xc6\xc7\xb0\x58\xed\x45\x6b\xc1\xab\x32\xdf\x88\x60\x33\x88\x6b\
\x16\xf6\x24\x2c\x5e\xf7\x4b\x3a\x28\xf6\x5e\xe4\x67\x50\x66\x65\
\xde\xf6\xe4\xcf\x0b\x65\xde\xcd\xbf\xd6\xa0\x82\x32\x23\xf3\x9d\
\x44\x5e\x3e\xff\x5c\x66\xa0\xcc\x2a\xe5\x15\xc7\x97\x64\xda\x1f\
\x04\x1d\x93\xf9\xae\xcc\xe3\xb4\xb6\x81\x91\xb3\xc9\x4c\x5e\x90\
\x79\x5b\xe4\xa7\x4a\x7a\xa5\x94\x57\x2f\xc2\x6e\xca\xf4\xad\x0b\
\x0b\x99\x87\x9b\x7f\x01\x46\xbb\xd6\x5d\xf7\xe4\x2f\x64\xfe\x0e\
\x68\x35\x61\xe3\x32\x1d\xf4\x62\xe7\xa5\x7d\x60\x0c\xc0\x93\xbf\
\x94\xf9\x1a\x50\x00\xac\x01\xdb\x02\x9b\xba\xa4\x1d\x7b\x66\xec\
\x44\x30\xfd\x37\x4e\x1e\x01\x9d\x7e\x8b\x26\x64\x3a\x6c\x4e\xf6\
\x5f\xbd\x01\x72\xc3\x86\xad\x69\x99\x1f\x55\x60\x91\xc9\x8b\x4d\
\xf1\x27\x65\xfa\x5e\x83\xb9\xf9\xe7\xb3\xbe\x75\x0f\x07\x6e\xc8\
\xf2\x36\xc4\x44\xc5\x25\x6f\xa7\x48\x8f\xfb\xf6\x4d\x29\xaf\xd4\
\x24\x93\xf9\x71\xa1\xcc\x37\xed\x94\x08\xee\xd4\x24\x53\xa4\xfb\
\x1d\x3a\x9f\x9a\x41\xe2\xc7\x80\xd8\xb1\x22\xdd\xbb\x08\x3b\x6d\
\xa2\xdf\x95\xf9\xc9\x25\xc7\xfc\x55\x28\x73\x0c\xfe\xfa\xf5\x50\
\xe6\x7f\x1a\xb0\x9f\xd0\xba\x55\xfd\x6f\x12\x7a\xd0\x07\x1d\x0e\
\xeb\x3e\x7e\x32\xff\x20\xf3\xdf\x32\x5f\x07\x26\x6b\x8d\x7f\x42\
\x54\x97\x39\x69\xbd\x94\x4c\x00\x00\x00\x00\x49\x45\x4e\x44\xae\
\x42\x60\x82\
\x00\x00\x02\x5a\
\x89\
\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d\x49\x48\x44\x52\x00\
\x00\x00\x14\x00\x00\x00\x14\x08\x06\x00\x00\x00\x8d\x89\x1d\x0d\
\x00\x00\x00\x06\x62\x4b\x47\x44\x00\xff\x00\xff\x00\xff\xa0\xbd\
\xa7\x93\x00\x00\x00\x09\x70\x48\x59\x73\x00\x00\x0d\xd7\x00\x00\
\x0d\xd7\x01\x42\x28\x9b\x78\x00\x00\x00\x07\x74\x49\x4d\x45\x07\
\xe0\x02\x08\x04\x19\x31\xa8\x33\xcb\x53\x00\x00\x01\xe7\x49\x44\
\x41\x54\x38\xcb\x9d\x93\x3b\x68\x54\x41\x14\x86\xbf\xf3\xb8\x59\
\x15\xa2\x29\x22\x68\x19\x56\x41\x5d\x15\x41\x3b\x09\xd8\x58\x09\
\x82\xc1\xa4\x10\xc4\xce\x94\x82\xd8\xa5\xb1\xb5\x49\xc4\x5a\x2d\
\xc4\xce\x20\x08\x12\x41\x04\xd1\xc2\x08\x5a\xf8\x80\x40\x10\x04\
\x1b\x11\x0b\x63\x9a\x10\xdc\x9d\x39\x36\xeb\xba\xbb\xde\x4d\x6e\
\x3c\x30\x30\x77\xce\xb9\xdf\xfc\x33\x73\x7e\xf8\x1b\xa3\x2a\xfe\
\xc1\xc4\xb3\x89\x47\x85\xb1\xee\xea\xb3\x0c\x0a\xc3\x2e\x98\xf8\
\x53\x40\xa8\x16\x7b\x4c\xbc\xd9\x5f\xaf\x5d\xf3\x02\x58\x05\xa2\
\x22\xf0\x27\xe0\xfd\x40\x2f\xab\x74\xf5\x1b\x81\x8c\x0d\x22\x49\
\x8e\x3b\x2d\x5a\x2f\xda\x9f\xb1\x29\x50\xb2\xcc\x43\xec\x1a\x04\
\x6c\xd1\x5a\x1a\x94\x2b\x05\x36\x69\x7e\x2b\x28\xf2\x06\xc7\x5d\
\xe9\x9a\x6f\xae\xd0\xc4\x67\x33\x31\xf0\xc8\x16\x76\x33\x91\xe6\
\x2b\x2b\x4c\xd1\x9a\xac\xf0\x28\xdb\xca\x16\x95\x2d\x45\xad\xee\
\xf8\xe9\x3f\xfb\x42\x7c\xae\xa4\xf0\xdf\x22\xbf\x8e\x32\x4c\xa4\
\x33\x01\xc3\x26\xf6\x08\x90\x94\xd3\xb9\xff\x51\xb8\x33\x84\xe9\
\x9c\xe5\x13\xc2\x02\x12\x4f\xc8\xfa\x8e\x90\x63\x86\x35\x36\x72\
\xca\x25\x13\x7f\xd0\xbb\x3a\x74\xc0\xc4\x17\x0b\x8a\x69\x13\x5f\
\xeb\xb6\x9e\xe2\x33\x2e\xbe\x64\xd8\x54\x65\x85\x46\xaa\x43\x8c\
\x66\x65\x1c\xd8\xde\xd3\xab\xc2\xd5\x90\x78\x86\x72\xaa\xf2\x1d\
\x26\xd2\x73\xc3\xbf\x12\xb1\xb7\x24\x3d\x12\x59\xbe\x0b\xb1\xbc\
\x05\x85\xc5\x14\x70\x34\x82\x97\x25\xe9\x57\x22\x1c\x47\x75\xb2\
\xf7\x9f\x0e\x59\xf7\x85\xc8\x59\x45\x56\x14\x6d\x28\xda\x48\xe8\
\x47\xd5\xbc\x43\x84\x11\x44\x97\x81\x23\x6d\x6b\xbc\x27\xe4\x9e\
\x08\x27\x52\xd8\x15\x48\x3f\x3a\x57\xd1\xdd\x64\xa6\x36\x47\xc8\
\xfe\x8e\xa7\x42\x1e\x1a\xbc\xce\x12\x8b\xc0\xdb\x08\x16\x40\xb3\
\x68\x1c\x24\xe2\x22\x21\x97\x13\xcd\xfb\xc0\x7a\x19\xb0\xa4\xeb\
\xfd\x9a\x08\x33\x12\xdc\x02\x72\x08\xe3\xc0\x61\x09\xe6\xda\xed\
\x74\x12\x58\x4b\xd1\x9a\xe8\x86\x0e\xe4\x99\xda\x5d\x13\x5f\x35\
\xf1\x5f\x86\x9d\x07\x6a\xc0\x6e\xa8\xd5\x4d\x8a\x2f\xed\x16\x7a\
\x0c\x43\x87\x2a\x9b\xcd\xd4\x6e\x1b\x36\x51\x62\xe5\x31\x13\x7f\
\xd3\xff\xb0\xbf\x01\x50\xcf\x9c\x3a\x50\x91\x48\xdb\x00\x00\x00\
\x00\x49\x45\x4e\x44\xae\x42\x60\x82\
"

qt_resource_name = "\
\x00\x06\
\x07\x03\x7d\xc3\
\x00\x69\
\x00\x6d\x00\x61\x00\x67\x00\x65\x00\x73\
\x00\x0c\
\x0a\xa6\x63\x87\
\x00\x70\
\x00\x65\x00\x72\x00\x73\x00\x6f\x00\x6e\x00\x61\x00\x6c\x00\x2e\x00\x70\x00\x6e\x00\x67\
\x00\x0d\
\x08\xab\xc0\xe7\
\x00\x75\
\x00\x73\x00\x62\x00\x2d\x00\x74\x00\x6f\x00\x6b\x00\x65\x00\x6e\x00\x2e\x00\x70\x00\x6e\x00\x67\
\x00\x08\
\x06\x67\x58\x67\
\x00\x72\
\x00\x6f\x00\x6f\x00\x74\x00\x2e\x00\x70\x00\x6e\x00\x67\
"

qt_resource_struct = "\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00\x02\
\x00\x00\x00\x50\x00\x00\x00\x00\x00\x01\x00\x00\x03\x60\
\x00\x00\x00\x30\x00\x00\x00\x00\x00\x01\x00\x00\x01\x68\
\x00\x00\x00\x12\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
"


def qInitResources():
    QtCore.qRegisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)


def qCleanupResources():
    QtCore.qUnregisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)


qInitResources()

if platform.machine() == 'x86_64':
    arch = 'amd64'
elif platform.machine() == 'i686':
    arch = 'ia32'
else:
    exit(-1)


def get_cspversion():
    csptest = subprocess.Popen(['/opt/cprocsp/bin/%s/csptest' % arch, '-keyset', '-verifycontext'],
                               stdout=subprocess.PIPE)
    output = csptest.communicate()[0].split('\n')[0]
    r = re.search(r'v([0-9.]*[0-9]+)\ (.+)\ Release Ver\:([0-9.]*[0-9]+)\ OS\:([a-zA-z]+)', output)
    return r.group(1), r.group(2), r.group(3), r.group(4)


def versiontuple(v):
    return tuple(map(int, (v.split("."))))


def get_tokens():
    list_pcsc = subprocess.Popen(['/opt/cprocsp/bin/%s/list_pcsc' % arch], stdout=subprocess.PIPE)
    output = list_pcsc.communicate()[0]
    if 'ERROR' in output:
        return u'<ключевых носителей не обнаружено>', 1
    m = re.findall(r'(?:available reader: |^)(.+)', output, re.MULTILINE)
    return m, 0


def get_token_serial(token):
    opensc_tool = subprocess.Popen(['/usr/bin/opensc-tool', '--serial', '-r', token], stdout=subprocess.PIPE)
    output = opensc_tool.communicate()[0]
    if not opensc_tool.returncode:
        return '%010d' % int(output[:11].replace(' ', ''), 16)


def get_token_certs(token):
    csptest = subprocess.Popen(['/opt/cprocsp/bin/%s/csptest' % arch, '-keyset', '-enum_cont', '-unique', '-fqcn',
                                '-verifyc'], stdout=subprocess.PIPE)
    output = csptest.communicate()[0]
    certs = []
    if csptest.returncode:
        return u'Ошибка', 1
    for line in output.split("\n"):
        if token in line:
            certs.append(line)
    return certs, 0


def get_store_certs(store):
    if store == 'root':
        certmgr = subprocess.Popen(['/opt/cprocsp/bin/%s/certmgr' % arch, '-list', '-store', 'root'], stdout=subprocess.PIPE)
        output = certmgr.communicate()[0]
        m = re.findall(r'(\d+)-{7}\nIssuer.*?: (.+?)\n.*?Subject.*?: (.+?)\n.*?Serial.*?: (0x\w+?)\nSHA1 Hash.*?(0x\w+?)\n.*?Not valid before.*?(\d.+?)UTC\nNot valid after.*?(\d.+?)UTC', output, re.MULTILINE + re.DOTALL)
    else:
        certmgr = subprocess.Popen(['/opt/cprocsp/bin/%s/certmgr' % arch, '-list', '' if versiontuple(get_cspversion()[2]) >= versiontuple("4.0.9708") else '-verbose' , '-store', store], stdout=subprocess.PIPE)
        output = certmgr.communicate()[0]
        m = re.findall(r'(\d+)-{7}\nIssuer.*?: (.+?)\n.*?Subject.*?: (.+?)\n.*?Serial.*?: (0x\w+?)\nSHA1 Hash.*?(0x\w+?)\n.*?Not valid before.*?(\d.+?)UTC\nNot valid after.*?(\d.+?)UTC.+?Extended Key Usage.*?([\d\.\s]+)\n', output, re.MULTILINE + re.DOTALL)
    return m


def list_cert(cert):
    certmgr = subprocess.Popen(['/opt/cprocsp/bin/%s/certmgr' % arch, '-list', '' if versiontuple(get_cspversion()[2]) >= versiontuple("4.0.9708") else '-verbose', '-cont', cert], stdout=subprocess.PIPE)
    output = certmgr.communicate()[0]
    m = re.findall(r'(\d+)-{7}\nIssuer.*?: (.+?)\n.*?Subject.*?: (.+?)\n.*?Serial.*?: (0x.+?)\nSHA1 Hash.*?(0x.+?)\n.*?Not valid before.*?(\d.+?)UTC\nNot valid after.*?(\d.+?)UTC.+?Extended Key Usage.*?([\d\.\s]+)\n',
        output, re.MULTILINE + re.DOTALL)
    return m


def inst_cert(cert):
    certmgr = subprocess.Popen(['/opt/cprocsp/bin/%s/certmgr' % arch, '-inst', '-store', 'uMy', '-cont',
                                cert], stdout=subprocess.PIPE)
    output = certmgr.communicate()[0]
    if certmgr.returncode:
        return output.split("\n")[-1]
    return u"Сертификат успешно установлен"


def inst_cert_from_file(filepath):
    certmgr = subprocess.Popen(['/opt/cprocsp/bin/%s/certmgr' % arch, '-inst', '-store', 'uMy', '-file',
                                filepath], stdout=subprocess.PIPE)
    output = certmgr.communicate()[0]
    if certmgr.returncode:
        return output.split("\n")[-1]
    return u"Сертификат успешно установлен"


def del_cont(cert):
    certmgr = subprocess.Popen(['/opt/cprocsp/bin/%s/certmgr' % arch, '-delete', '-cont', cert], stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    output = certmgr.communicate()[0]
    if certmgr.returncode:
        return output
    return u"Сертификат успешно удален"


def del_store_cert(cert_index, store):
    certmgr = subprocess.Popen(['/opt/cprocsp/bin/%s/certmgr' % arch, '-delete', '-store', store],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    output = certmgr.communicate(cert_index)[0]
    if certmgr.returncode:
        return output
    return u"Сертификат успешно удален"


def set_license(cpro_license):
    cpconfig = subprocess.Popen(['/usr/bin/cpconfig-%s' % arch, '-license', '-set', cpro_license],
                                stdout=subprocess.PIPE)
    output = cpconfig.communicate()[0]
    if cpconfig.returncode:
        return output.split("\n")[-1], 1
    return None, 0


def get_license():
    cpconfig = subprocess.Popen(['/opt/cprocsp/sbin/%s/cpconfig' % arch, '-license', '-view'], stdout=subprocess.PIPE)
    output = cpconfig.communicate()[0]
    return output


def install_root_cert(file):
    certmgr = subprocess.Popen(['/opt/cprocsp/bin/%s/certmgr' % arch, '-inst', '-store', 'root', '-file', file],
                               stdout=subprocess.PIPE)
    output = certmgr.communicate()[0]
    m = re.findall(
        r'(\d+)-{7}\nIssuer.*?CN=(.+?)[\n,].*?Subject.*?CN=(.+?)[\n,].*?Serial.*?(0x.+?)\nSHA1 Hash.*?(0x.+?)\n.*?Not valid before.*?(\d.+?)UTC\nNot valid after.*?(\d.+?)UTC',
        output, re.MULTILINE + re.DOTALL)
    return m


def list_root_certs():
    certmgr = subprocess.Popen(['/opt/cprocsp/bin/%s/certmgr' % arch, '-list', '-store', 'root'],
                               stdout=subprocess.PIPE)
    output = certmgr.communicate()[0]
    m = re.findall(
        r'(\d+)-{7}\nIssuer.*?CN=(.+?)[\n,].*?Subject.*?CN=(.+?)[\n,].*?Serial.*?(0x.+?)\nSHA1 Hash.*?(0x.+?)\n.*?Not valid before.*?(\d.+?)UTC\nNot valid after.*?(\d.+?)UTC',
        output,
        re.MULTILINE + re.DOTALL)
    return m


def install_crl(file):
    certmgr = subprocess.Popen(['/opt/cprocsp/bin/%s/certmgr' % arch, '-inst', '-crl', '-store', 'root', '-file', file],
                               stdout=subprocess.PIPE)
    output = certmgr.communicate()[0]
    m = re.findall(r'(\d+)-{7}.+?CN=(.+?)[\n,].*?ThisUpdate: (\d.+?)UTC\nNextUpdate: (\d.+?)UTC', output,
                   re.MULTILINE + re.DOTALL)
    return m


def list_crls():
    certmgr = subprocess.Popen(['/opt/cprocsp/bin/%s/certmgr' % arch, '-list', '-crl', '-store', 'root'],
                               stdout=subprocess.PIPE)
    output = certmgr.communicate()[0]
    m = re.findall(r'(\d+)-{7}.+?CN=(.+?)[\n,].*?ThisUpdate: (\d.+?)UTC\nNextUpdate: (\d.+?)UTC', output,
                   re.MULTILINE + re.DOTALL)
    return m


def change_user_pin(old_pin, new_pin):
    pkcs15tool = subprocess.Popen(
        ['pkcs15-tool', '--auth-id', '02', '--change-pin', '--pin', old_pin, '--new-pin', new_pin],
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = pkcs15tool.communicate()[0]
    tries = output.split('\n')[1].split(': ')[-1]
    if tries:
        return False, tries
    else:
        return True, None


def init_token():
    createpkcs15 = subprocess.Popen(['/usr/bin/pkcs15-init', '--create-pkcs15', '--pin', '12345678', '--so-pin',
                                     '87654321', '--so-puk', ''], stdout=subprocess.PIPE)
    storepin = subprocess.Popen(['/usr/bin/pkcs15-init', '--store-pin', '--label', 'User PIN', '--auth-id', '02',
                                 '--pin', '12345678', '--puk', '', '--so-pin', '87654321'], stdout=subprocess.PIPE)
    createpkcs15.communicate()
    storepin.communicate()
    if createpkcs15.returncode or storepin.returncode:
        return False
    else:
        return True


def check_user_pin():
    pkcs15tool = subprocess.Popen(['/usr/bin/pkcs15-tool', '-D'], stdout=subprocess.PIPE)
    output = pkcs15tool.communicate()[0]
    search = 'User PIN'
    s = re.search(search, output)
    if s:
        auth_id = output.split('[User PIN]')[1].split('\n\t')[2].split(':')[-1].strip()
        return auth_id
    else:
        return None


def add_ini(pin, cont_id):
    cpconfig = subprocess.Popen(['/opt/cprocsp/sbin/%s/cpconfig' % arch, '-ini',
                                 '\\LOCAL\\KeyDevices\\passwords\\%s\%s\%s' % tuple(cont_id[:-1]), '-add', 'string',
                                 'passwd', pin], stdout=subprocess.PIPE)
    return cpconfig.returncode


def set_as_reader(token):
    cpconfig = subprocess.Popen(['/usr/bin/cpconfig-%s' % arch, '-hardware', 'reader', '-add', token],
                                stdout=subprocess.PIPE)
    output = cpconfig.communicate()[0]
    if "Succeeded, code:0x0" in output:
        return True
    else:
        return False


def translate_cert_fields(fieldname):
    fields = {'1.2.840.113549.1.9.2': u'неструктурированное имя',
              '1.2.643.5.1.5.2.1.2': u'код должности',
              '1.2.643.5.1.5.2.1.1': u'код структурного подразделения ФССП России (ВКСП)',
              '1.2.643.5.1.5.2.2.1': u'Полномочия публикации обновлений ПО',
              '1.2.643.5.1.5.2.2.2': u'Подсистема АИС ФССП России',
              '1.2.643.5.1.24.2.9': u'Главный судебный пристав Российской Федерации',
              '1.2.643.5.1.24.2.10': u'Заместитель главного судебного пристава Российской Федерации',
              '1.2.643.5.1.24.2.11': u'Главный судебный пристав субъекта Российской Федерации',
              '1.2.643.5.1.24.2.12': u'Заместитель главного судебного пристава субъекта Российской Федерации',
              '1.2.643.5.1.24.2.13': u'Старший судебный пристав',
              '1.2.643.5.1.24.2.14': u'Судебный пристав-исполнитель',
              '1.2.643.100.2.1': u'Доступ к СМЭВ (ФЛ)',
              '1.2.643.100.2.2': u'Доступ к СМЭВ (ЮЛ)',
              '1.2.643.2.2.34.2': u'Временный доступ к Центру Регистрации',
              '1.2.643.2.2.34.4': u'Администратор Центра Регистрации КриптоПро УЦ',
              '1.2.643.2.2.34.5': u'Оператор Центра Регистрации КриптоПро УЦ',
              '1.2.643.2.2.34.6': u'Пользователь центра регистрации КриптоПро УЦ',
              '1.2.643.2.2.34.7': u'Центр Регистрации КриптоПро УЦ',
              '1.3.6.1.5.5.7.3.1': u'Проверка подлинности сервера',
              '1.3.6.1.5.5.7.3.2': u'Проверка подлинности клиента',
              '1.3.6.1.5.5.7.3.4': u'Защищенная электронная почта',
              '1.3.6.1.5.5.7.3.8': u'Установка штампа времени',
              '1.2.643.3.61.502710.1.6.3.4.1.1': u'Администратор организации',
              '1.2.643.3.61.502710.1.6.3.4.1.2': u'Уполномоченный специалист',
              '1.2.643.3.61.502710.1.6.3.4.1.3': u'Должностное лицо с правом подписи контракта',
              '1.2.643.3.61.502710.1.6.3.4.1.4': u'Специалист с правом направления проекта контракта участнику размещения заказа',
              'CN': u'общее имя',
              'SN': u'фамилия',
              'G': u'имя и отчество',
              'I': u'инициалы',
              'T': u'должность',
              'OU': u'структурное подразделение',
              'O': u'организация',
              'L': u'населенный пункт',
              'S': u'субъект РФ',
              'C': u'страна',
              'E': u'адрес электронной почты',
              'INN': u'ИНН',
              'OGRN': u'ОГРН',
              'SNILS': u'СНИЛС',
              'STREET': u'название улицы, номер дома',
              'StreetAddress': u'адрес места нахождения',
              'Unstructured Name': u'неструктурированное имя'}
    try:
        return fields[fieldname]
    except KeyError:
        return fieldname


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(413, 388)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(344, 0))
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("/usr/share/pixmaps/token-manager.png")), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setLineWidth(2)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.token_refresh = QtGui.QPushButton(self.centralwidget)
        self.token_refresh.setObjectName(_fromUtf8("token_refresh"))
        self.horizontalLayout_3.addWidget(self.token_refresh)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.token_list = QtGui.QListWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.token_list.sizePolicy().hasHeightForWidth())
        self.token_list.setSizePolicy(sizePolicy)
        self.token_list.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.token_list.setObjectName(_fromUtf8("token_list"))
        self.verticalLayout.addWidget(self.token_list)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.asReader = QtGui.QPushButton(self.centralwidget)
        self.asReader.setEnabled(False)
        self.asReader.setObjectName(_fromUtf8("asReader"))
        self.horizontalLayout_2.addWidget(self.asReader)
        self.cachePIN = QtGui.QPushButton(self.centralwidget)
        self.cachePIN.setEnabled(False)
        self.cachePIN.setObjectName(_fromUtf8("cachePIN"))
        self.horizontalLayout_2.addWidget(self.cachePIN)
        self.changePIN = QtGui.QPushButton(self.centralwidget)
        self.changePIN.setEnabled(False)
        self.changePIN.setObjectName(_fromUtf8("changePIN"))
        self.horizontalLayout_2.addWidget(self.changePIN)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.cert_list = QtGui.QListWidget(self.centralwidget)
        self.cert_list.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.cert_list.setObjectName(_fromUtf8("cert_list"))
        self.verticalLayout.addWidget(self.cert_list)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.cert_delete = QtGui.QPushButton(self.centralwidget)
        self.cert_delete.setEnabled(False)
        self.cert_delete.setObjectName(_fromUtf8("cert_delete"))
        self.horizontalLayout.addWidget(self.cert_delete)
        self.cert_view = QtGui.QPushButton(self.centralwidget)
        self.cert_view.setEnabled(False)
        self.cert_view.setObjectName(_fromUtf8("cert_view"))
        self.horizontalLayout.addWidget(self.cert_view)
        self.cert_install = QtGui.QPushButton(self.centralwidget)
        self.cert_install.setEnabled(False)
        self.cert_install.setObjectName(_fromUtf8("cert_install"))
        self.horizontalLayout.addWidget(self.cert_install)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 413, 27))
        self.menuBar.setDefaultUp(False)
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.operations = QtGui.QMenu(self.menuBar)
        self.operations.setObjectName(_fromUtf8("operations"))
        MainWindow.setMenuBar(self.menuBar)
        self.add_license = QtGui.QAction(MainWindow)
        self.add_license.setObjectName(_fromUtf8("add_license"))
        self.install_root_certs = QtGui.QAction(MainWindow)
        self.install_root_certs.setObjectName(_fromUtf8("install_root_certs"))
        self.install_crl = QtGui.QAction(MainWindow)
        self.install_crl.setObjectName(_fromUtf8("install_crl"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.view_license = QtGui.QAction(MainWindow)
        self.view_license.setObjectName(_fromUtf8("view_license"))
        self.view_root = QtGui.QAction(MainWindow)
        self.view_root.setObjectName(_fromUtf8("view_root"))
        self.view_crl = QtGui.QAction(MainWindow)
        self.view_crl.setObjectName(_fromUtf8("view_crl"))
        self.operations.addAction(self.add_license)
        self.operations.addAction(self.view_license)
        self.operations.addSeparator()
        self.operations.addAction(self.install_root_certs)
        self.operations.addAction(self.install_crl)
        self.operations.addSeparator()
        self.operations.addAction(self.view_root)
        self.operations.addAction(self.view_crl)
        self.menuBar.addAction(self.operations.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "token-manager", None))
        self.label.setText(_translate("MainWindow", "Выберите ключевой носитель или хранилище", None))
        self.token_refresh.setText(_translate("MainWindow", "Обновить", None))
        self.asReader.setText(_translate("MainWindow", "Подключить как считыватель", None))
        self.cachePIN.setText(_translate("MainWindow", "Сохранить PIN", None))
        self.changePIN.setText(_translate("MainWindow", "Сменить PIN", None))
        self.label_2.setText(_translate("MainWindow", "Выберите контейнер сертификата", None))
        self.cert_delete.setText(_translate("MainWindow", "Удалить", None))
        self.cert_view.setText(_translate("MainWindow", "Просмотр", None))
        self.cert_install.setText(_translate("MainWindow", "Установить", None))
        self.operations.setTitle(_translate("MainWindow", "Операции", None))
        self.add_license.setText(_translate("MainWindow", "Ввод лицензии КриптоПро CSP", None))
        self.install_root_certs.setText(_translate("MainWindow", "Установка корневых сертификатов", None))
        self.install_crl.setText(_translate("MainWindow", "Установка списков отозванных сертификатов", None))
        self.actionAbout.setText(_translate("MainWindow", "about", None))
        self.view_license.setText(_translate("MainWindow", "Просмотр лицензии КриптоПро CSP", None))
        self.view_root.setText(_translate("MainWindow", "Просмотр корневых сертификатов", None))
        self.view_crl.setText(_translate("MainWindow", "Просмотр списков отозванных сертификатов", None))


class Ui_cert_view(object):
    def setupUi(self, cert_view):
        cert_view.setObjectName(_fromUtf8("cert_view"))
        cert_view.resize(430, 343)
        self.gridLayout = QtGui.QGridLayout(cert_view)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(323, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.close_cert_view = QtGui.QPushButton(cert_view)
        self.close_cert_view.setObjectName(_fromUtf8("close_cert_view"))
        self.gridLayout.addWidget(self.close_cert_view, 1, 1, 1, 1)
        self.cert_listview = QtGui.QListWidget(cert_view)
        self.cert_listview.setObjectName(_fromUtf8("cert_listview"))
        self.gridLayout.addWidget(self.cert_listview, 0, 0, 1, 2)

        self.retranslateUi(cert_view)
        QtCore.QObject.connect(self.close_cert_view, QtCore.SIGNAL(_fromUtf8("clicked()")), cert_view.close)
        QtCore.QMetaObject.connectSlotsByName(cert_view)

    def retranslateUi(self, cert_view):
        cert_view.setWindowTitle(_translate("cert_view", "Просмотр", None))
        self.close_cert_view.setText(_translate("cert_view", "Закрыть", None))


class Ui_cert_list(object):
    def setupUi(self, cert_list):
        cert_list.setObjectName(_fromUtf8("cert_list"))
        cert_list.resize(404, 343)
        self.gridLayout = QtGui.QGridLayout(cert_list)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(323, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.close_cert_list = QtGui.QPushButton(cert_list)
        self.close_cert_list.setObjectName(_fromUtf8("close_cert_list"))
        self.gridLayout.addWidget(self.close_cert_list, 2, 1, 1, 1)
        self.cert_listview = QtGui.QListWidget(cert_list)
        self.cert_listview.setObjectName(_fromUtf8("cert_listview"))
        self.gridLayout.addWidget(self.cert_listview, 1, 0, 1, 2)
        self.cert_list_filter = QtGui.QLineEdit(cert_list)
        self.cert_list_filter.setObjectName(_fromUtf8("cert_list_filter"))
        self.gridLayout.addWidget(self.cert_list_filter, 0, 0, 1, 2)

        self.retranslateUi(cert_list)
        QtCore.QObject.connect(self.close_cert_list, QtCore.SIGNAL(_fromUtf8("clicked()")), cert_list.close)
        QtCore.QMetaObject.connectSlotsByName(cert_list)

    def retranslateUi(self, cert_list):
        cert_list.setWindowTitle(_translate("cert_list", "Список", None))
        self.close_cert_list.setText(_translate("cert_list", "Закрыть", None))


class ViewCert(QtGui.QDialog):
    def __init__(self):
        super(ViewCert, self).__init__()
        self.ui = Ui_cert_view()
        self.ui.setupUi(self)


class ListCert(QtGui.QDialog):

    list_data = []
    is_root = False

    def __init__(self, certlist_data, is_root):
        super(ListCert, self).__init__()
        self.ui = Ui_cert_list()
        self.ui.setupUi(self)
        self.ui.cert_list_filter.textChanged.connect(self.filterout)
        self.list_data = certlist_data
        self.is_root = is_root
        self.filterout()

    def filterout(self):
        self.ui.cert_listview.clear()
        filter_text = unicode(self.ui.cert_list_filter.text())
        for line in self.list_data:
            if filter_text.upper() in line[1].decode('utf-8').upper():
                item = QtGui.QListWidgetItem()
                if self.is_root:
                    not_valid_before = datetime.strptime(line[5], '%d/%m/%Y  %H:%M:%S ')
                    not_valid_after = datetime.strptime(line[6], '%d/%m/%Y  %H:%M:%S ')
                    if not_valid_after < datetime.utcnow():
                        item.setBackgroundColor(QtGui.QColor(252, 133, 133))
                    item.setText(('Эмитент: %s\nСубъект: %s\nСерийный номер: %s\nХэш SHA1: %s\nНе действителен до: %s\n'
                          'Не действителен после: %s' % (line[1], line[2], line[3], line[4],
                                                         datetime.strftime(not_valid_before, '%d.%m.%Y %H:%M:%S'),
                                                         datetime.strftime(not_valid_after,
                                                                           '%d.%m.%Y %H:%M:%S'))).decode('utf-8'))
                else:
                    this_update = datetime.strptime(line[2], '%d/%m/%Y  %H:%M:%S ')
                    next_update = datetime.strptime(line[3], '%d/%m/%Y  %H:%M:%S ')
                    if next_update < datetime.utcnow():
                        item.setBackgroundColor(QtGui.QColor(252, 133, 133))
                    item.setText(('%s\nДата выпуска: %s UTC\nДата обновления: %s UTC' %
                          (line[1], datetime.strftime(this_update, '%d.%m.%Y %H:%M:%S'),
                           datetime.strftime(next_update, '%d.%m.%Y %H:%M:%S'))).decode('utf-8'))
                self.ui.cert_listview.addItem(item)

class TokenListItem(QtGui.QListWidgetItem):
    isToken = True
    storage = ''
    token_name = ''

    def __init__(self, parent=None):
        super(TokenListItem, self).__init__(parent)


class CertListItem(QtGui.QListWidgetItem):
    cert_index = 0

    def __init__(self, parent=None):
        super(CertListItem, self).__init__(parent)


class MainWindow(QtGui.QMainWindow):
    token = ""
    cert = ""
    cont_id = ""

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        aboutAction = QtGui.QAction(u'&О программе', self)
        aboutAction.setShortcut('Ctrl+Q')
        aboutAction.triggered.connect(self.aboutProgram)
        self.ui.menuBar.addAction(aboutAction)
        if not os.path.exists('/opt/cprocsp/bin/%s/certmgr' % arch) or not os.path.exists('/opt/cprocsp/bin/%s/cryptcp' % arch):
            raise Exception(u'СКЗИ Крипто Про CSP или некоторые его компоненты не установлены.')
        self.refresh_token()
        self.ui.token_refresh.clicked.connect(self.refresh_token)
        self.ui.token_list.itemClicked.connect(self.select_token)
        self.ui.cert_view.clicked.connect(self.view_cert)
        self.ui.cert_list.itemClicked.connect(self.select_cert)
        self.ui.cert_install.clicked.connect(self.install_cert)
        self.ui.add_license.triggered.connect(self.enter_license)
        self.ui.view_license.triggered.connect(self.view_license)
        self.ui.install_root_certs.triggered.connect(self.open_root_certs)
        self.ui.install_crl.triggered.connect(self.open_crl)
        self.ui.view_root.triggered.connect(self.view_root)
        self.ui.view_crl.triggered.connect(self.view_crl)
        self.ui.changePIN.clicked.connect(self.change_pin)
        self.ui.cert_delete.clicked.connect(self.delete_cert)
        self.ui.cachePIN.clicked.connect(self.cache_pin)
        self.ui.asReader.clicked.connect(self.set_reader)
        if versiontuple(get_cspversion()[2]) < versiontuple("3.6.7491"):
            QtGui.QMessageBox.information(self, u"Сообщение", u"Необходимо обновить КриптоПро CSP."
                                                              u"<br>Ваша текущая версия: %s"
                                                              u"<br>Минимальная рекомендуемая: 3.6.7491" %
                                          get_cspversion()[2])

    def set_reader(self):
        if set_as_reader(self.token):
            QtGui.QMessageBox.information(self, u"Cообщение", u"Ключевой носитель %s успешно добавлен в качестве "
                                                              u"считывателя" % self.token)
        else:
            QtGui.QMessageBox.information(self, u"Cообщение", u"Произошла ошибка")

    def cache_pin(self):
        pin, ok = QtGui.QInputDialog.getText(None, u"Ввод PIN-кода", u"Введите PIN-код:",
                                             QtGui.QLineEdit.Password)
        if ok:
            if not add_ini(pin, self.cont_id):
                QtGui.QMessageBox.information(self, u"Cообщение", u"PIN-код успешно сохранен")

    def change_pin(self):
        auth_id = check_user_pin()
        if auth_id:
            old_pin, ok = QtGui.QInputDialog.getText(None, u"Ввод PIN-кода", u"Введите текущий PIN-код:",
                                                     QtGui.QLineEdit.Password)
            if ok:
                new_pin, ok = QtGui.QInputDialog.getText(None, u"Ввод PIN-кода", u"Введите новый PIN-код:",
                                                         QtGui.QLineEdit.Password)
                if ok:
                    conf_pin, ok = QtGui.QInputDialog.getText(None, u"Ввод PIN-кода", u"Повторите новый PIN-код:",
                                                              QtGui.QLineEdit.Password)
                    if ok and new_pin == conf_pin:
                        if len(new_pin) < 8:
                            QtGui.QMessageBox.warning(self, u'Ошибка', u"Недостаточная длина PIN-кода.\nМинимальная "
                                                                       u"длина PIN составляет 8 символов")
                            return
                        ok, tries = change_user_pin(old_pin, new_pin)
                        if ok:
                            QtGui.QMessageBox.information(self, u"Cообщение", u"PIN-код успешно изменен")
                            add_ini(new_pin, self.cont_id)
                        else:
                            QtGui.QMessageBox.warning(self, u'Ошибка', u"PIN-код введен неверно\nОсталось попыток: %s" %
                                                      tries)
                    else:
                        QtGui.QMessageBox.warning(self, u'Ошибка', u"Введенные PIN-коды не совпадают")
        else:
            if not init_token():
                QtGui.QMessageBox.warning(self, u"Ошибка", u'Произошла ошибка при инициализации ключевого носителя')
            else:
                self.change_pin()

    def view_root(self):
        root_info = list_root_certs()
        root_view = ListCert(root_info, True)
        root_view.exec_()

    def view_crl(self):
        crl_info = list_crls()
        crl_view = ListCert(crl_info, False)
        crl_view.exec_()

    def open_crl(self):
        file_names = QtGui.QFileDialog.getOpenFileNames(self, u"Выберите файл(ы)", "", "*.crl")
        if not file_names:
            return
        crl_view = ViewCert()
        for filename in file_names:
            crl_info = install_crl(unicode(filename))
            for line in crl_info:
                item = QtGui.QListWidgetItem()
                this_update = datetime.strptime(line[2], '%d/%m/%Y  %H:%M:%S ')
                next_update = datetime.strptime(line[3], '%d/%m/%Y  %H:%M:%S ')
                if next_update < datetime.utcnow():
                    item.setBackgroundColor(QtGui.QColor(252, 133, 133))
                item.setText(('%s\nДата выпуска: %s UTC\nДата обновления: %s UTC' %
                              (line[1], datetime.strftime(this_update, '%d.%m.%Y %H:%M:%S'),
                               datetime.strftime(next_update, '%d.%m.%Y %H:%M:%S'))).decode('utf-8'))
                crl_view.ui.cert_listview.addItem(item)
        crl_view.setWindowTitle(QtCore.QString(u'Установлен список отозванных сертификатов'))
        crl_view.exec_()

    def open_root_certs(self):
        file_names = QtGui.QFileDialog.getOpenFileNames(self, u"Выберите файл(ы)", "", "*.cer *.crt")
        if not file_names:
            return
        root_view = ViewCert()
        for filename in file_names:
            root_info = install_root_cert(unicode(filename))
            for line in root_info:
                item = QtGui.QListWidgetItem()
                not_valid_before = datetime.strptime(line[5], '%d/%m/%Y  %H:%M:%S ')
                not_valid_after = datetime.strptime(line[6], '%d/%m/%Y  %H:%M:%S ')
                if not_valid_after < datetime.utcnow():
                    item.setBackgroundColor(QtGui.QColor(252, 133, 133))
                item.setText(('Эмитент: %s\nСубъект: %s\nСерийный номер: %s\nХэш SHA1: %s\nНе действителен до: %s\n'
                              'Не действителен после: %s' % (line[1], line[2], line[3], line[4],
                                                             datetime.strftime(not_valid_before, '%d.%m.%Y %H:%M:%S'),
                                                             datetime.strftime(not_valid_after,
                                                                               '%d.%m.%Y %H:%M:%S'))).decode('utf-8'))
                root_view.ui.cert_listview.addItem(item)
        root_view.setWindowTitle(QtCore.QString(u'Установлен корневой сертификат'))
        root_view.exec_()

    def view_license(self):
        license_info = get_license()
        license_view = ViewCert()
        item = QtGui.QListWidgetItem()
        item.setText(license_info)
        license_view.ui.cert_listview.addItem(item)
        license_view.exec_()

    def enter_license(self):
        cpro_license, ok = QtGui.QInputDialog.getText(self, u'Лицензия КриптоПро',
                                                      u'Введите лицензионный ключ:')
        if ok:
            m = re.match('([A-Z0-9]{5}-){4}[A-Z0-9]{5}', cpro_license)
            if m:
                l = set_license(cpro_license)
                if l[1]:
                    QtGui.QMessageBox.warning(self, u"Ошибка", u"Произошла ошибка: %s" % l[0])
                else:
                    QtGui.QMessageBox.information(self, u"Cообщение", u"Лицензионный ключ успешно установлен")
            else:
                QtGui.QMessageBox.warning(self, u"Ошибка", u"Лицензионный ключ введен неверно!")

    def install_cert(self):
        ret = inst_cert(self.cert)
        QtGui.QMessageBox.information(self, u"Сообщение", ret)

    def install_local_cert(self):
        file_name = QtGui.QFileDialog().getOpenFileName(self, u"Выберите файл(ы)", "", "*.cer")
        if not file_name:
            return
        ret = inst_cert_from_file(unicode(file_name))
        QtGui.QMessageBox.information(self, u"Сообщение", ret)

    def delete_cert(self):
        is_token = self.ui.token_list.currentItem().isToken
        if is_token:
            reply = QtGui.QMessageBox.question(self, u'Подтверждение',
                                               u'Вы уверенны что хотите удалить данный сертификат '
                                               u'с ключевого носителя?\n'
                                               u'Эту операцию нельзя отменить.',
                                               QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
            if reply == QtGui.QMessageBox.Yes:
                ret = del_cont(self.cert)
                QtGui.QMessageBox.information(self, u"Сообщение", ret)
                self.ui.cert_delete.setEnabled(False)
                self.ui.cert_view.setEnabled(False)
                self.ui.cert_install.setEnabled(False)
        else:
            reply = QtGui.QMessageBox.question(self, u'Подтверждение',
                                               u'Вы уверенны что хотите удалить данный сертификат?\n'
                                               u'Эту операцию нельзя отменить.',
                                               QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
            if reply == QtGui.QMessageBox.Yes:
                ret = del_store_cert(self.ui.cert_list.currentItem().cert_index,
                                     self.ui.token_list.currentItem().storage)
                QtGui.QMessageBox.information(self, u"Сообщение", ret)
                self.ui.cert_delete.setEnabled(False)
                self.ui.cert_view.setEnabled(False)
                self.ui.cert_install.setEnabled(False)
        #for SelectedItem in self.ui.cert_list.selectedItems():
        self.ui.cert_list.takeItem(self.ui.cert_list.currentRow())

    def select_cert(self, item):
        is_token = self.ui.token_list.currentItem().isToken
        self.ui.cert_install.setEnabled(True)
        self.ui.cert_view.setEnabled(True)
        self.ui.cert_delete.setEnabled(True)
        self.ui.cachePIN.setEnabled(is_token)
        self.ui.changePIN.setEnabled(is_token)
        self.ui.asReader.setEnabled(is_token)
        self.ui.cert_view.clicked.disconnect()
        if is_token:
            self.ui.cert_view.clicked.connect(self.view_cert)
            containers = get_token_certs(self.token)
            cert_name = str(item.text().toUtf8())
            for line in containers[0]:
                container = line.decode('cp1251').encode('utf-8')
                if cert_name in container:
                    self.cert = line.split('|')[1]
                    self.cont_id = line.split('|')[1].split('\\')[4:] # содержит список, который нужно объединить бэкслэшами
        else:
            self.ui.cert_view.clicked.connect(self.view_cert)

    def select_token(self, item):
        self.ui.cert_list.clear()
        # Костыль, помогающий не присваивать атрибуту self.token значение задисейбленого итема
        if item.isSelected() and item.isToken:
            self.ui.cert_install.setHidden(False)
            self.ui.cert_install.clicked.disconnect()
            self.ui.cert_install.clicked.connect(self.install_cert)
            self.ui.label_2.setText(u'Выберите контейнер сертификата')
            self.ui.asReader.setEnabled(True)
            self.token = str(item.token_name)
            certs = get_token_certs(str(item.token_name))[0]
            for cert in certs:
                cert_item = QtGui.QListWidgetItem()
                cert_item.setText(cert.split('|')[0].split('\\')[-1].decode('cp1251'))
                self.ui.cert_list.addItem(cert_item)
        if not item.isToken:
            self.ui.cert_install.setEnabled(True)
            if item.storage == 'root':
                self.ui.cert_install.clicked.disconnect()
                self.ui.cert_install.clicked.connect(self.open_root_certs)
            elif item.storage == 'uMy':
                self.ui.cert_install.clicked.disconnect()
                self.ui.cert_install.clicked.connect(self.install_local_cert)
            self.ui.label_2.setText(u'Выберите сертификат')
            self.ui.asReader.setEnabled(False)
            self.ui.changePIN.setEnabled(False)
            self.ui.cachePIN.setEnabled(False)
            certs = get_store_certs(item.storage)
            for cert in certs:
                cert_item = CertListItem()
                cert_item.cert_index = cert[0]
                if datetime.strptime(cert[6], '%d/%m/%Y  %H:%M:%S ') < datetime.utcnow():
                    cert_item.setBackgroundColor(QtGui.QColor(252, 133, 133))
                cert_subject_cn = dict(re.findall(ur'([A-Z0-9\.]+?)=("?[\w \.\,0-9@\-\#\/\"]+"?)(?:, |$)', cert[2].decode('utf-8'), re.UNICODE))['CN']
                cert_issuer_cn = dict(re.findall(ur'([A-Z0-9\.]+?)=("?[\w \.\,0-9@\-\#\/\"]+"?)(?:, |$)', cert[1].decode('utf-8'), re.UNICODE))['CN']
                cert_item.setText(u"%s\nвыдан %s" % (cert_subject_cn, cert_issuer_cn))
                self.ui.cert_list.addItem(cert_item)

    def view_cert(self):
        store = self.ui.token_list.currentItem().storage
        if self.ui.token_list.currentItem().isToken:
            cert_info = list_cert(self.cert)
            line = cert_info[0]
        else:
            cert_info = get_store_certs(store)
            line = cert_info[int(self.ui.cert_list.currentItem().cert_index) - 1]
        cert_view = ViewCert()
        item = QtGui.QListWidgetItem(cert_view.ui.cert_listview)
        label = QtGui.QLabel()
        label.setText(u'<b>Эмитент</b>:')
        cert_view.ui.cert_listview.setItemWidget(item, label)
        issuer_info = dict(re.findall(ur'([A-Z0-9\.]+?)=("?[\w \.\,0-9@\-\#\/\"]+"?)(?:, |$)', line[1].decode('utf-8'), re.UNICODE))
        for field in issuer_info:
            item = QtGui.QListWidgetItem(cert_view.ui.cert_listview)
            label = QtGui.QLabel()
            label.setText(u'<b>%s</b>:\t\t%s' % (translate_cert_fields(field), issuer_info[field]))
            cert_view.ui.cert_listview.setItemWidget(item, label)
        item = QtGui.QListWidgetItem(cert_view.ui.cert_listview)
        item = QtGui.QListWidgetItem(cert_view.ui.cert_listview)
        label = QtGui.QLabel()
        label.setText(u'<b>Субъект</b>:')
        cert_view.ui.cert_listview.setItemWidget(item, label)
        subject_info = dict(re.findall(ur'([A-Z0-9\.]+?)=("?[\w \.\,0-9@\-\#\/\"]+"?)(?:, |$)', line[2].decode('utf-8'), re.UNICODE))
        for field in subject_info:
            item = QtGui.QListWidgetItem(cert_view.ui.cert_listview)
            label = QtGui.QLabel()
            if subject_info[field][:2] == '"#':  # Если поле в HEX-виде
                label.setText(u'<b>%s</b>:\t%s' % (translate_cert_fields(field), subject_info[field][6:-1].decode('hex').decode('utf-8')))
            else:
                label.setText(u'<b>%s</b>:\t%s' % (translate_cert_fields(field), subject_info[field]))
            cert_view.ui.cert_listview.setItemWidget(item, label)
        item = QtGui.QListWidgetItem(cert_view.ui.cert_listview)
        item = QtGui.QListWidgetItem(cert_view.ui.cert_listview)
        not_valid_before = datetime.strptime(line[5], '%d/%m/%Y  %H:%M:%S ')
        label = QtGui.QLabel()
        label.setText(u'<b>Не действителен до</b>: %s' % datetime.strftime(not_valid_before, '%d.%m.%Y %H:%M:%S'))
        cert_view.ui.cert_listview.setItemWidget(item, label)
        item = QtGui.QListWidgetItem(cert_view.ui.cert_listview)
        not_valid_after = datetime.strptime(line[6], '%d/%m/%Y  %H:%M:%S ')
        if not_valid_after < datetime.utcnow():
            item.setBackgroundColor(QtGui.QColor(252, 133, 133))
        label = QtGui.QLabel()
        label.setText(u'<b>Не действителен после</b>: %s' % datetime.strftime(not_valid_after, '%d.%m.%Y %H:%M:%S'))
        cert_view.ui.cert_listview.setItemWidget(item, label)
        item = QtGui.QListWidgetItem(cert_view.ui.cert_listview)
        item = QtGui.QListWidgetItem(cert_view.ui.cert_listview)
        label = QtGui.QLabel()
        label.setText(u'<b>Расширенное использование ключа</b>: ')
        cert_view.ui.cert_listview.setItemWidget(item, label)
        try:
            ext_key = line[7].split()
        except IndexError:
            ext_key = [u'<i>Не имеет</i>']
        for oid in ext_key:
            item = QtGui.QListWidgetItem(cert_view.ui.cert_listview)
            label = QtGui.QLabel()
            label.setText(translate_cert_fields(oid))
            cert_view.ui.cert_listview.setItemWidget(item, label)
        cert_view.exec_()

    def refresh_token(self):
        self.ui.token_list.clear()
        tokens = get_tokens()
        root_store_item = TokenListItem()
        root_store_item.setText(u"Хранилище корневых сертификатов")
        root_store_item.isToken = False
        root_store_item.storage = 'root'
        root_store_item.setIcon(QtGui.QIcon(':/images/root.png'))
        self.ui.token_list.addItem(root_store_item)
        personal_store_item = TokenListItem()
        personal_store_item.setText(u"Личное хранилище сертификатов")
        personal_store_item.isToken = False
        personal_store_item.storage = 'uMy'
        personal_store_item.setIcon(QtGui.QIcon(':/images/personal.png'))
        self.ui.token_list.addItem(personal_store_item)
        if tokens[1]:
            token_item = TokenListItem()
            self.ui.cert_list.clearSelection()
            token_item.setText(u'<Ключевых носителей не обнаружено>')
            token_item.setSelected(False)
            token_item.setFlags(QtCore.Qt.NoItemFlags)
        else:
            for token in tokens[0]:
                token_item = TokenListItem()
                token_item.token_name = token
                token_item.setText(u'%s - сер. № %s' % (token, get_token_serial(token)))
                token_item.setIcon(QtGui.QIcon(':/images/usb-token.png'))
                self.ui.token_list.addItem(token_item)

    def aboutProgram(self):
        QtGui.QMessageBox.about(self, u"О программе",
                                u"<b>token-manager 0.12</b><br>"
                                u"Версия CSP: %s<br>"
                                u"Класс криптосредств: %s<br>"
                                u"Релиз: %s<br>"
                                u"ОС: %s<br>"
                                u"<br>Борис Макаренко<br>УИТ ФССП России"
                                u"<br>E-mail: <a href='mailto:makarenko@fssprus.ru'>makarenko@fssprus.ru</a>"
                                u"<br> <a href='mailto:bmakarenko90@gmail.com'>bmakarenko90@gmail.com<br><br>"
                                u"<a href='http://opensource.org/licenses/MIT'>Лицензия MIT</a>" % get_cspversion())


def main():
    app = QtGui.QApplication(sys.argv)
    try:
        ex = MainWindow()
    except Exception as error:
        QtGui.QMessageBox().warning(QtGui.QMessageBox(), u"Cообщение", u"Произошла ошибка:\n%s" % error)
        exit(-1)

    if len(sys.argv) == 1:
        ex.show()
        sys.exit(app.exec_())
    else:
        if os.path.isfile(sys.argv[1].decode('utf-8')):
            ret = inst_cert_from_file(sys.argv[1].decode('utf-8'))
            QtGui.QMessageBox().information(QtGui.QMessageBox(), u"Сообщение", ret)

if __name__ == '__main__':
    main()
