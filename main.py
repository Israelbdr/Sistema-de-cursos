# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcome.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sqlite3
from menu import Ui_menu

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName(_fromUtf8("login"))
        login.resize(401, 302)
        login.setStyleSheet(_fromUtf8("background-color: rgb(170, 167, 255);"))
        self.user_ent = QtGui.QLineEdit(login)
        self.user_ent.setGeometry(QtCore.QRect(120, 170, 201, 21))
        self.user_ent.setObjectName(_fromUtf8("user_ent"))
        self.user_ent.setStyleSheet(_fromUtf8("background-color:rgb(255,255,255);"))
        self.passwd_ent = QtGui.QLineEdit(login)
        self.passwd_ent.setStyleSheet(_fromUtf8("background-color:rgb(255,255,255);"))
        self.passwd_ent.setGeometry(QtCore.QRect(120, 200, 201, 21))
        self.passwd_ent.setObjectName(_fromUtf8("passwd_ent"))
        self.user_lbl = QtGui.QLabel(login)
        self.user_lbl.setGeometry(QtCore.QRect(70, 170, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.user_lbl.setFont(font)
        self.user_lbl.setObjectName(_fromUtf8("user_lbl"))
        self.passwd_lbl = QtGui.QLabel(login)
        self.passwd_lbl.setGeometry(QtCore.QRect(70, 200, 51, 20))
        self.passwd_ent.setEchoMode(QtGui.QLineEdit.Password)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.passwd_lbl.setFont(font)
        self.passwd_lbl.setObjectName(_fromUtf8("passwd_lbl"))
        self.ok_button = QtGui.QPushButton(login)
        self.ok_button.setGeometry(QtCore.QRect(150, 240, 101, 31))
        self.ok_button.setObjectName(_fromUtf8("ok_button"))
        self.ok_button.clicked.connect(self.loginCheck)

        self.welcome_lbl = QtGui.QLabel(login)
        self.welcome_lbl.setGeometry(QtCore.QRect(90, 110, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.welcome_lbl.setFont(font)
        self.welcome_lbl.setObjectName(_fromUtf8("welcome_lbl"))

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        login.setWindowTitle(_translate("login", "Login", None))
        self.user_lbl.setText(_translate("login", "Usuário:", None))
        self.passwd_lbl.setText(_translate("login", "Senha:", None))
        self.ok_button.setText(_translate("login", "Login", None))
        self.welcome_lbl.setText(_translate("login", "Bem-vindo ao SisCursos", None))

    #Mostra uma caixa de diálogo.
    def showMessageBox(self,title,message):
        msgBox = QtGui.QMessageBox()
        msgBox.setIcon(QtGui.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
        msgBox.exec_()

    # Função mostrar o menu principal.
    def menuWindowshow(self):
        self.menuWindow = QtGui.QMainWindow()
        self.ui = Ui_menu()
        self.ui.setupUi(self.menuWindow)
        self.menuWindow.show()

    # Checa se o usuário é autorizado.
    def loginCheck(self):
        db = sqlite3.connect("Database.db")
        username = self.user_ent.text()
        password = self.passwd_ent.text()
        check = db.execute("SELECT * FROM users WHERE username = ? AND password = ?;", (str(username), str(password)))
        if len(check.fetchall()) > 0:
            self.menuWindowshow()
        else:
            self.showMessageBox("Aviso", "Usuário ou senha inválido.")

# Começa a execução do programa.
if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    main = QtGui.QMainWindow()
    ui = Ui_login()
    ui.setupUi(main)
    main.show()

    sys.exit(app.exec_())
