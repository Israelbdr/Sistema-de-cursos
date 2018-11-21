# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adicionar.ui'
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

class Ui_adicionarC(object):
    def setupUi(self, adicionar):
        adicionar.setObjectName(_fromUtf8("adicionar"))
        adicionar.resize(497, 347)
        adicionar.setStyleSheet(_fromUtf8("background-color:rgb(170, 167, 255)"))
        self.ok_button = QtGui.QPushButton(adicionar)
        self.ok_button.setGeometry(QtCore.QRect(210, 260, 75, 23))
        self.ok_button.setObjectName(_fromUtf8("ok_button"))
        self.codigo_ent = QtGui.QLineEdit(adicionar)
        self.codigo_ent.setGeometry(QtCore.QRect(110, 140, 113, 20))
        self.codigo_ent.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.codigo_ent.setObjectName(_fromUtf8("codigo_ent"))
        self.nome_ent = QtGui.QLineEdit(adicionar)
        self.nome_ent.setGeometry(QtCore.QRect(340, 140, 113, 20))
        self.nome_ent.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255)"))
        self.nome_ent.setObjectName(_fromUtf8("nome_ent"))
        self.horario_ent = QtGui.QLineEdit(adicionar)
        self.horario_ent.setGeometry(QtCore.QRect(100, 180, 120, 20))
        self.horario_ent.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255)"))
        self.horario_ent.setObjectName(_fromUtf8("horario_ent"))
        self.codigo_lbl = QtGui.QLabel(adicionar)
        self.codigo_lbl.setGeometry(QtCore.QRect(20, 140, 90, 13))
        self.codigo_lbl.setObjectName(_fromUtf8("codigo_lbl"))
        self.nome_lbl = QtGui.QLabel(adicionar)
        self.nome_lbl.setGeometry(QtCore.QRect(260, 140, 80, 20))
        self.nome_lbl.setObjectName(_fromUtf8("nome_lbl"))
        self.horario_lbl = QtGui.QLabel(adicionar)
        self.horario_lbl.setGeometry(QtCore.QRect(20, 180, 80, 20))
        self.horario_lbl.setObjectName(_fromUtf8("horario_lbl"))
        self.data_lbl = QtGui.QLabel(adicionar)
        self.data_lbl.setGeometry(QtCore.QRect(260, 180, 100, 20))
        self.data_lbl.setObjectName(_fromUtf8("data_lbl"))
        self.data_ent = QtGui.QLineEdit(adicionar)
        self.data_ent.setGeometry(QtCore.QRect(350, 180, 113, 20))
        self.data_ent.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.data_ent.setObjectName(_fromUtf8("data_ent"))

        self.retranslateUi(adicionar)
        QtCore.QMetaObject.connectSlotsByName(adicionar)

    def retranslateUi(self, adicionar):
        adicionar.setWindowTitle(_translate("adicionar", "Cursos", None))
        self.ok_button.setText(_translate("adicionar", "Adicionar", None))
        self.codigo_lbl.setText(_translate("adicionar", "Código do Curso:", None))
        self.nome_lbl.setText(_translate("adicionar", "Nome do Curso:", None))
        self.horario_lbl.setText(_translate("adicionar", "Carga Horária:", None))
        self.data_lbl.setText(_translate("adicionar", "Data de Cadastro:", None))

    def adicionarCursos(self):
        import sqlite3
        db = sqlite3.connect("Database.db")
        cursor = db.cursor()
        if self.codigo_ent.text()=="" or self.nome_ent=="" or self.horario_ent=="" or self.data_ent=="":
            self.showMessageBox("Aviso", "Verifique os espaços em branco.")
        else:
            sqlInsert = ("INSERT INTO cursos(codigo_do_curso, nome_do_curso, data_de_cadastro, carga_horaria)"
                         " VALUES (?, ?, ?, ?)")
            valores = (int(self.codigo_ent.text()), str(self.nome_ent.text()), str(self.data_ent.text()), str(self.horario_ent))
            cursor.execute(sqlInsert, valores)
            self.showMessageBox("Aviso", "Curso inserido.")
            db.commit()
            db.close()