# -*- coding: utf-8 -*-

"""
Copyright (c) 2014 Борис Макаренко

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

Copyright (c) 2014 Boris Makarenko

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

import sys
from PyQt4 import QtCore
from PyQt4 import QtGui
import subprocess
import platform
import re

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

if platform.machine() == 'x86_64':
    arch = 'amd64'
elif platform.machine() == 'i686':
    arch = 'ia32'
else:
    exit()


def get_token():
    list_pcsc = subprocess.Popen(['/opt/cprocsp/bin/%s/list_pcsc' % arch], stdout=subprocess.PIPE)
    output = list_pcsc.communicate()[0]
    if list_pcsc.returncode:
        return u'<ключевых носителей не обнаружено>', 1
    return output.replace("available reader: ", "").replace("\n", ""), 0


def get_certs(token):
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


def list_cert(cert):
    certmgr = subprocess.Popen(['/opt/cprocsp/bin/%s/certmgr' % arch, '-list', '-cont', cert], stdout=subprocess.PIPE)
    output = certmgr.communicate()[0]
    if certmgr.returncode:
        return output.split("\n")[-1], 1
    return output.decode('utf-8'), 0


def inst_cert(cert):
    certmgr = subprocess.Popen(['/opt/cprocsp/bin/%s/certmgr' % arch, '-inst', '-store', 'uMy', '-cont',
                                cert], stdout=subprocess.PIPE)
    output = certmgr.communicate()[0]
    if certmgr.returncode:
        return output.split("\n")[-1]
    return u"Сертификат успешно установлен"


def del_cert(cert):
    certmgr = subprocess.Popen(['/opt/cprocsp/bin/%s/certmgr' % arch, '-delete', '-cont', cert], stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    output = certmgr.communicate()[0]
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
    return output.decode('utf-8')


def list_root_certs():
    certmgr = subprocess.Popen(['/opt/cprocsp/bin/%s/certmgr' % arch, '-list', '-store', 'root'],
                               stdout=subprocess.PIPE)
    output = certmgr.communicate()[0]
    return output.decode('utf-8')


def install_crl(file):
    certmgr = subprocess.Popen(['/opt/cprocsp/bin/%s/certmgr' % arch, '-inst', '-crl', '-store', 'root', '-file', file],
                               stdout=subprocess.PIPE)
    output = certmgr.communicate()[0]
    return output.decode('utf-8')


def list_crls():
    certmgr = subprocess.Popen(['/opt/cprocsp/bin/%s/certmgr' % arch, '-list', '-crl', '-store', 'root'],
                               stdout=subprocess.PIPE)
    output = certmgr.communicate()[0]
    return output.decode('utf-8')


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


def get_cspversion():
    csptest = subprocess.Popen(['/opt/cprocsp/bin/%s/csptest' % arch, '-keyset', '-verifycontext'],
                               stdout=subprocess.PIPE)
    output = csptest.communicate()[0].split('\n')[0]
    r = re.search(r'v([0-9.]*[0-9]+)\ (.+)\ Release Ver\:([0-9.]*[0-9]+)\ OS\:([a-zA-z]+)', output)
    return r.group(1), r.group(2), r.group(3), r.group(4)


def versiontuple(v):
    return tuple(map(int, (v.split("."))))


def add_ini(pin, cont_id):
    cpconfig = subprocess.Popen(['/opt/cprocsp/sbin/%s/cpconfig' % arch, '-ini',
                                 '\\LOCAL\\KeyDevices\\passwords\\%s\%s\%s' % tuple(cont_id[:-1]), '-add', 'string',
                                 'passwd', pin], stdout=subprocess.PIPE)
    return cpconfig.returncode


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(344, 370)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(360, 0))
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("/usr/share/pixmaps/token-manager.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setLineWidth(2)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.token_list = QtGui.QListView(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.token_list.sizePolicy().hasHeightForWidth())
        self.token_list.setSizePolicy(sizePolicy)
        self.token_list.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.token_list.setObjectName(_fromUtf8("token_list"))
        self.verticalLayout_2.addWidget(self.token_list)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.cachePIN = QtGui.QPushButton(self.centralwidget)
        self.cachePIN.setEnabled(False)
        self.cachePIN.setObjectName(_fromUtf8("cachePIN"))
        self.horizontalLayout_2.addWidget(self.cachePIN)
        self.changePIN = QtGui.QPushButton(self.centralwidget)
        self.changePIN.setEnabled(False)
        self.changePIN.setObjectName(_fromUtf8("changePIN"))
        self.horizontalLayout_2.addWidget(self.changePIN)
        self.token_refresh = QtGui.QPushButton(self.centralwidget)
        self.token_refresh.setObjectName(_fromUtf8("token_refresh"))
        self.horizontalLayout_2.addWidget(self.token_refresh)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.cert_list = QtGui.QListView(self.centralwidget)
        self.cert_list.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.cert_list.setObjectName(_fromUtf8("cert_list"))
        self.verticalLayout_2.addWidget(self.cert_list)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
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
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 344, 21))
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
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>Выберите ключевой носитель</p></body></html>", None))
        self.cachePIN.setText(_translate("MainWindow", "Сохранить PIN-код", None))
        self.changePIN.setText(_translate("MainWindow", "Сменить PIN-код", None))
        self.token_refresh.setText(_translate("MainWindow", "Обновить", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>Выберите сертификат</p></body></html>", None))
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
        cert_view.resize(435, 328)
        self.gridLayout = QtGui.QGridLayout(cert_view)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.cert_listview = QtGui.QListView(cert_view)
        self.cert_listview.setObjectName(_fromUtf8("cert_listview"))
        self.gridLayout.addWidget(self.cert_listview, 0, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(323, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.close_cert_view = QtGui.QPushButton(cert_view)
        self.close_cert_view.setObjectName(_fromUtf8("close_cert_view"))
        self.gridLayout.addWidget(self.close_cert_view, 1, 1, 1, 1)

        self.retranslateUi(cert_view)
        QtCore.QObject.connect(self.close_cert_view, QtCore.SIGNAL(_fromUtf8("clicked()")), cert_view.close)
        QtCore.QMetaObject.connectSlotsByName(cert_view)

    def retranslateUi(self, cert_view):
        cert_view.setWindowTitle(_translate("cert_view", "Просмотр", None))
        self.close_cert_view.setText(_translate("cert_view", "Закрыть", None))


class ViewCert(QtGui.QDialog):
    def __init__(self):
        super(ViewCert, self).__init__()
        self.ui = Ui_cert_view()
        self.ui.setupUi(self)


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
        self.refresh_token()
        self.ui.token_refresh.clicked.connect(self.refresh_token)
        self.ui.token_list.clicked.connect(self.select_token)
        self.ui.cert_view.clicked.connect(self.view_cert)
        self.ui.cert_list.clicked.connect(self.select_cert)
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
        self.show()
        if versiontuple(get_cspversion()[2]) < versiontuple("3.6.7491"):
            QtGui.QMessageBox.information(self, u"Сообщение", u"Необходимо обновить КриптоПро CSP."
                                                              u"<br>Ваша текущая версия: %s"
                                                              u"<br>Минимальная рекомендуемая: 3.6.7491" %
                                          get_cspversion()[2])

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
        root_view = ViewCert()
        model = QtGui.QStringListModel()
        root_list = QtCore.QStringList()
        for line in root_info.split("\n"):
            for param in line.split(", "):
                root_list.append(QtCore.QString(param))
        model.setStringList(root_list)
        root_view.ui.cert_listview.setModel(model)
        root_view.exec_()

    def view_crl(self):
        crl_info = list_crls()
        crl_view = ViewCert()
        model = QtGui.QStringListModel()
        crl_list = QtCore.QStringList()
        for line in crl_info.split("\n"):
            for param in line.split(", "):
                crl_list.append(QtCore.QString(param))
        model.setStringList(crl_list)
        crl_view.ui.cert_listview.setModel(model)
        crl_view.exec_()

    def open_crl(self):
        file_names = QtGui.QFileDialog.getOpenFileNames(self, u"Выберите файл(ы)", "", "*.crl")
        for filename in file_names:
            crl_info = install_crl(unicode(filename))
            crl_view = ViewCert()
            model = QtGui.QStringListModel()
            crl_list = QtCore.QStringList()
            for line in crl_info.split("\n"):
                for param in line.split(", "):
                    crl_list.append(QtCore.QString(param))
            model.setStringList(crl_list)
            crl_view.ui.cert_listview.setModel(model)
            crl_view.exec_()

    def open_root_certs(self):
        file_names = QtGui.QFileDialog.getOpenFileNames(self, u"Выберите файл(ы)", "", "*.cer")
        for filename in file_names:
            root_info = install_root_cert(unicode(filename))
            root_view = ViewCert()
            model = QtGui.QStringListModel()
            root_list = QtCore.QStringList()
            for line in root_info.split("\n"):
                for param in line.split(", "):
                    root_list.append(QtCore.QString(param))
            model.setStringList(root_list)
            root_view.ui.cert_listview.setModel(model)
            root_view.exec_()

    def view_license(self):
        license_info = get_license()
        license_view = ViewCert()
        model = QtGui.QStringListModel()
        license_list = QtCore.QStringList()
        for line in license_info.split("\n"):
            for param in line.split(", "):
                license_list.append(QtCore.QString(param))
        model.setStringList(license_list)
        license_view.ui.cert_listview.setModel(model)
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

    def delete_cert(self):
        reply = QtGui.QMessageBox.question(self, u'Подтверждение', u'Вы уверенны что хотите удалить данный сертификат '
                                                                   u'с ключевого носителя?\n'
                                                                   u'Эту операцию нельзя отменить.',
                                           QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            ret = del_cert(self.cert)
            QtGui.QMessageBox.information(self, u"Сообщение", ret)
            model = QtGui.QStringListModel()
            cert_list = QtCore.QStringList()
            certs = get_certs(self.token)[0]
            for cert in certs:
                cert_list.append(cert.split('\\')[-1])
            model.setStringList(cert_list)
            self.ui.cert_list.setModel(model)
            self.ui.cert_delete.setEnabled(False)
            self.ui.cert_view.setEnabled(False)
            self.ui.cert_install.setEnabled(False)

    def select_cert(self, index):
        self.ui.cert_install.setEnabled(True)
        self.ui.cert_view.setEnabled(True)
        self.ui.cert_delete.setEnabled(True)
        self.ui.cachePIN.setEnabled(True)
        containers = get_certs(self.token)
        cert_name = str(index.data().toString())
        for line in containers[0]:
            if cert_name in line:
                self.cert = r"\\.\%s\%s" % (self.token, cert_name)
                self.cont_id = line.split('|')[1].split('\\')[4:]  # содержит список, который нужно объединить бэкслэшами

    def select_token(self, index):
        self.token = str(index.data().toString())
        model = QtGui.QStringListModel()
        cert_list = QtCore.QStringList()
        certs = get_certs(str(index.data().toString()))[0]
        for cert in certs:
            cert_list.append(cert.split('|')[0].split('\\')[-1])
        model.setStringList(cert_list)
        self.ui.cert_list.setModel(model)
        self.ui.changePIN.setEnabled(True)

    def view_cert(self):
        cert_info = list_cert(self.cert)
        cert_view = ViewCert()
        model = QtGui.QStringListModel()
        cert_list = QtCore.QStringList()
        cert_list.append(QtCore.QString(self.cert))
        for line in cert_info[0].split("\n"):
            for param in line.split(", "):
                cert_list.append(QtCore.QString(param))
        model.setStringList(cert_list)
        cert_view.ui.cert_listview.setModel(model)
        cert_view.exec_()

    def refresh_token(self):
        token = get_token()
        model = QtGui.QStringListModel()
        token_list = QtCore.QStringList()
        token_list.append(QtCore.QString(token[0]))
        if token[1]:
            self.ui.token_list.setEnabled(False)
            self.ui.cert_list.clearSelection()
        else:
            self.ui.token_list.setEnabled(True)
        model.setStringList(token_list)
        self.ui.token_list.setModel(model)

    def aboutProgram(self):
        QtGui.QMessageBox.about(self, u"О программе",
                                u"<b>token-manager 0.7</b><br>"
                                u"Версия CSP: %s<br>"
                                u"Класс криптосредств: %s<br>"
                                u"Релиз: %s<br>"
                                u"ОС: %s<br>"
                                u"<br>Борис Макаренко<br>УФССП России по Красноярскому краю"
                                u"<br>E-mail: <a href='mailto:makarenko@r24.fssprus.ru'>makarenko@r24.fssprus.ru</a>"
                                u"<br> <a href='mailto:bmakarenko90@gmail.com'>bmakarenko90@gmail.com<br><br>"
                                u"<a href='http://opensource.org/licenses/MIT'>Лицензия MIT</a>" % get_cspversion())


def main():
    app = QtGui.QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
