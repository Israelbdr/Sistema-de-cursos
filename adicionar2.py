# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adicionar2.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_adicionarA(object):
    def setupUi(self, adicionarA):
        adicionarA.setObjectName(_fromUtf8("adicionarA"))
        adicionarA.resize(448, 306)
        adicionarA.setStyleSheet(_fromUtf8("background-color: rgb(170, 167, 255);"))
        self.adiciona_button = QtGui.QPushButton(adicionarA)
        self.adiciona_button.setGeometry(QtCore.QRect(170, 270, 75, 23))
        self.adiciona_button.setObjectName(_fromUtf8("adiciona_button"))
        self.adiciona_button.clicked.connect(self.adicionarAlunos)
        self.cpd_ent = QtGui.QLineEdit(adicionarA)
        self.cpd_ent.setGeometry(QtCore.QRect(50, 90, 90, 20))
        self.cpd_ent.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.cpd_ent.setObjectName(_fromUtf8("cpd_ent"))
        self.nome_ent = QtGui.QLineEdit(adicionarA)
        self.nome_ent.setGeometry(QtCore.QRect(100, 140, 113, 20))
        self.nome_ent.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.nome_ent.setObjectName(_fromUtf8("nome_ent"))
        self.telefone_ent = QtGui.QLineEdit(adicionarA)
        self.telefone_ent.setGeometry(QtCore.QRect(70, 190, 113, 20))
        self.telefone_ent.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.telefone_ent.setObjectName(_fromUtf8("telefone_ent"))
        self.email_ent = QtGui.QLineEdit(adicionarA)
        self.email_ent.setGeometry(QtCore.QRect(270, 90, 113, 20))
        self.email_ent.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.email_ent.setObjectName(_fromUtf8("email_ent"))
        self.end_ent = QtGui.QLineEdit(adicionarA)
        self.end_ent.setGeometry(QtCore.QRect(70, 230, 210, 20))
        self.end_ent.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.end_ent.setObjectName(_fromUtf8("end_ent"))
        self.cod_ent = QtGui.QLineEdit(adicionarA)
        self.cod_ent.setGeometry(QtCore.QRect(330, 140, 50, 20))
        self.cod_ent.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.cod_ent.setObjectName(_fromUtf8("cod_ent"))
        self.cep_ent = QtGui.QLineEdit(adicionarA)
        self.cep_ent.setGeometry(QtCore.QRect(270, 190, 90, 20))
        self.cep_ent.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.cep_ent.setObjectName(_fromUtf8("cep_ent"))
        self.cpd_lbl = QtGui.QLabel(adicionarA)
        self.cpd_lbl.setGeometry(QtCore.QRect(20, 80, 30, 40))
        self.cpd_lbl.setObjectName(_fromUtf8("cpd_lbl"))
        self.nome_lbl = QtGui.QLabel(adicionarA)
        self.nome_lbl.setGeometry(QtCore.QRect(20, 130, 80, 40))
        self.nome_lbl.setObjectName(_fromUtf8("nome_lbl"))
        self.telefone_lbl = QtGui.QLabel(adicionarA)
        self.telefone_lbl.setGeometry(QtCore.QRect(20, 190, 47, 13))
        self.telefone_lbl.setObjectName(_fromUtf8("telefone_lbl"))
        self.cep_lbl = QtGui.QLabel(adicionarA)
        self.cep_lbl.setGeometry(QtCore.QRect(240, 180, 30, 40))
        self.cep_lbl.setObjectName(_fromUtf8("cep_lbl"))
        self.email_lbl = QtGui.QLabel(adicionarA)
        self.email_lbl.setGeometry(QtCore.QRect(230, 80, 40, 40))
        self.email_lbl.setObjectName(_fromUtf8("email_lbl"))
        self.end_lbl = QtGui.QLabel(adicionarA)
        self.end_lbl.setGeometry(QtCore.QRect(20, 220, 47, 40))
        self.end_lbl.setObjectName(_fromUtf8("end_lbl"))
        self.cod_lbl = QtGui.QLabel(adicionarA)
        self.cod_lbl.setGeometry(QtCore.QRect(240, 130, 80, 40))
        self.cod_lbl.setObjectName(_fromUtf8("cod_lbl"))

        self.retranslateUi(adicionarA)
        QtCore.QMetaObject.connectSlotsByName(adicionarA)

    def retranslateUi(self, adicionarA):
        adicionarA.setWindowTitle(_translate("adicionarA", "Alunos", None))
        self.adiciona_button.setText(_translate("adicionarA", "Adicionar", None))
        self.cpd_lbl.setText(_translate("adicionarA", "CPD:", None))
        self.nome_lbl.setText(_translate("adicionarA", "Nome do aluno:", None))
        self.telefone_lbl.setText(_translate("adicionarA", "Telefone:", None))
        self.cep_lbl.setText(_translate("adicionarA", "CEP:", None))
        self.email_lbl.setText(_translate("adicionarA", "E-mail:", None))
        self.end_lbl.setText(_translate("adicionarA", "Endereço:", None))
        self.cod_lbl.setText(_translate("adicionarA", "Código do Curso:", None))

    # Mostra uma caixa de diálogo.
    def showMessageBox(self, title, message):
        msgBox = QtGui.QMessageBox()
        msgBox.setIcon(QtGui.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
        msgBox.exec_()

    def adicionarAlunos(self):
        import sqlite3
        db = sqlite3.connect("Database.db")
        cursor = db.cursor()
        if self.cpd_ent.text()=="" or self.nome_ent.text()=="" or self.cep_ent.text()=="" or self.cod_ent.text()=="" or self.end_ent.text()=="":
            self.showMessageBox("Aviso", "Verifique os espaços em branco.")
        else:
            sqlInsert = ("INSERT INTO alunos(cpd, nome_do_aluno, telefone, endereco, cep, email, codigo_do_curso) VALUES ("
                           "?, ?, ?, ?, ?, ?, ?)")
            valores = int(self.cpd_ent.text()), str(self.nome_ent.text()), int(self.telefone_ent.text()), str(self.end_ent.text()),  str(self.cep_ent.text()), str(self.email_ent.text()), int(self.cod_ent.text())
            cursor.execute(sqlInsert, valores)
            self.showMessageBox("Aviso", "Aluno inserido.")
            db.commit()
            db.close()