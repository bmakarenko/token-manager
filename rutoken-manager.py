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
        return (u'<ключевых носителей не обнаружено>', 1)
    return (output.replace("available reader: ", "").replace("\n", ""), 0)


def get_certs(token):
    csptest = subprocess.Popen(['/opt/cprocsp/bin/%s/csptest' % arch, '-keyset', '-enum_cont', '-fqcn', '-verifyc'],
                               stdout=subprocess.PIPE)
    output = csptest.communicate()[0]
    certs = []
    if csptest.returncode:
        return (u'Ошибка', 1)
    for line in output.split("\n"):
        if token in line:
            certs.append(line)
    return (certs, 0)


def list_cert(cert):
    certmgr = subprocess.Popen(['/opt/cprocsp/bin/%s/certmgr' % arch, '-list', '-cont', cert], stdout=subprocess.PIPE)
    output = certmgr.communicate()[0]
    if certmgr.returncode:
        return (output.split("\n")[-1], 1)
    return (output.decode('utf-8'), 0)


def inst_cert(cert):
    certmgr = subprocess.Popen(['/opt/cprocsp/bin/%s/certmgr' % arch, '-inst', '-cont', cert], stdout=subprocess.PIPE)
    output = certmgr.communicate()[0]
    if certmgr.returncode:
        return output.split("\n")[-1]
    return u"Сертификат успешно установлен"


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(344, 370)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(344, 0))
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("rutoken-manager.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        self.cert_view = QtGui.QPushButton(self.centralwidget)
        self.cert_view.setObjectName(_fromUtf8("cert_view"))
        self.horizontalLayout.addWidget(self.cert_view)
        self.cert_install = QtGui.QPushButton(self.centralwidget)
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
        self.operations.addAction(self.add_license)
        self.operations.addAction(self.install_root_certs)
        self.operations.addAction(self.install_crl)
        self.menuBar.addAction(self.operations.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "rutoken-manager", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>Выберите ключевой носитель</p></body></html>", None))
        self.token_refresh.setText(_translate("MainWindow", "Обновить", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>Выберите сертификат</p></body></html>", None))
        self.cert_view.setText(_translate("MainWindow", "Просмотр", None))
        self.cert_install.setText(_translate("MainWindow", "Установить", None))
        self.operations.setTitle(_translate("MainWindow", "Операции", None))
        self.add_license.setText(_translate("MainWindow", "Ввод лицензии Крипто Про CSP", None))
        self.install_root_certs.setText(_translate("MainWindow", "Установка корневых сертификатов", None))
        self.install_crl.setText(_translate("MainWindow", "Установка списков отозванных сертификатов", None))
        self.actionAbout.setText(_translate("MainWindow", "about", None))

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

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        aboutAction = QtGui.QAction(u'&О программе', self)
        aboutAction.setShortcut('Ctrl+Q')
        aboutAction.setStatusTip('Exit application')
        aboutAction.triggered.connect(self.aboutProgram)
        self.ui.menuBar.addAction(aboutAction)
        self.ui.cert_install.setEnabled(False)
        self.ui.cert_view.setEnabled(False)
        self.refresh_token()
        self.ui.token_refresh.clicked.connect(self.refresh_token)
        self.ui.token_list.clicked.connect(self.select_token)
        self.ui.cert_view.clicked.connect(self.view_cert)
        self.ui.cert_list.clicked.connect(self.select_cert)
        self.ui.cert_install.clicked.connect(self.install_cert)
        self.show()

    def install_cert(self):
        ret = inst_cert(self.cert)
        QtGui.QMessageBox.about(self, u"Сообщение", ret)

    def select_cert(self, index):
        self.ui.cert_install.setEnabled(True)
        self.ui.cert_view.setEnabled(True)
        self.cert = "\\\\.\\%s\\%s" % (self.token, str(index.data().toString()))

    def select_token(self, index):
        self.token = str(index.data().toString())
        model = QtGui.QStringListModel()
        list = QtCore.QStringList()
        certs = get_certs(str(index.data().toString()))[0]
        for cert in certs:
            list.append(cert.split('\\')[-1])
        model.setStringList(list)
        self.ui.cert_list.setModel(model)

    def view_cert(self):
        cert_info = list_cert(self.cert)
        cert_view = ViewCert()
        model = QtGui.QStringListModel()
        list = QtCore.QStringList()
        list.append(QtCore.QString(self.cert))
        for line in cert_info[0].split("\n"):
            for param in line.split(", "):
                list.append(QtCore.QString(param))
        model.setStringList(list)
        cert_view.ui.cert_listview.setModel(model)
        cert_view.exec_()

    def refresh_token(self):
        token = get_token()
        model = QtGui.QStringListModel()
        list = QtCore.QStringList()
        list.append(QtCore.QString(token[0]))
        if token[1]:
            self.ui.token_list.setEnabled(False)
            self.ui.cert_list.clearSelection()
        else:
            self.ui.token_list.setEnabled(True)
        model.setStringList(list)
        self.ui.token_list.setModel(model)

    def aboutProgram(self):
        QtGui.QMessageBox.about(self, u"О программе",
                                u"<b>rutoken-manager 0.1</b><br><br>Борис Макаренко<br>УФССП России по Красноярскому"
                                u" краю<br>E-mail: <a href='mailto:infotdel@r24.fssprus.ru'>infotdel@r24.fssprus.ru</a>,"
                                u"<br> <a href='mailto:bmakarenko90@gmail.com'>bmakarenko90@gmail.com<br><br><a href='http://opensource.org/licenses/MIT'>Лицензия MIT</a>")


def main():
    app = QtGui.QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
