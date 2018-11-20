# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
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

class Ui_menu(object):
    def setupUi(self, menu):
        menu.setObjectName(_fromUtf8("menu"))
        menu.resize(746, 480)
        self.centralwidget = QtGui.QWidget(menu)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidget.setGeometry(QtCore.QRect(20, 80, 711, 151))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(20)
        self.consulta_button = QtGui.QPushButton(self.centralwidget)
        self.consulta_button.setGeometry(QtCore.QRect(20, 30, 90, 30))
        self.consulta_button.setObjectName(_fromUtf8("consulta_button"))
        self.consulta_button.clicked.connect(self.mostrarTabelaAlunos)
        self.tableWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        # self.tableWidget.customContextMenuRequested.connect(self.menuContextual)

        self.colunas_box = QtGui.QComboBox(self.centralwidget)
        self.colunas_box.setGeometry(QtCore.QRect(130, 30, 211, 31))
        self.colunas_box.setEditable(False)
        self.colunas_box.setObjectName(_fromUtf8("colunas_box"))
        self.colunas_box.insertItem(0, "Alunos")
        self.colunas_box.insertItem(1, "Cursos")
        self.colunas_box.currentText()
        self.apagar_button = QtGui.QPushButton(self.centralwidget)
        self.apagar_button.setGeometry(QtCore.QRect(610, 30, 120, 30))
        self.apagar_button.setObjectName(_fromUtf8("apagar_button"))
        self.apagar_button.clicked.connect(self.apagarTabela)
        menu.setCentralWidget(self.centralwidget)


        self.retranslateUi(menu)
        QtCore.QMetaObject.connectSlotsByName(menu)


    #Função para limpar a tabela de suas entradas
    def apagarTabela(self):
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)

    def retranslateUi(self, menu):
        menu.setWindowTitle(_translate("menu", "Tabelas", None))
        self.consulta_button.setText(_translate("menu", "Consultar", None))
        self.apagar_button.setText(_translate("menu", "Limpar tela", None))

    # def menuContextual(self, posicao):
    #     arrayDados = self.tableWidget.selectecIndexes()
    #     if arrayDados:
    #         menu = QMenu()
    #         iGrupo = QtGui.QActionGroup(self)
    #         iGrupo.setExclusive(True)
    #         menu.addAction(QtGui.QAction("Copiar tudo", iGrupo))
    #         colunas = [self.tableWidget.horizontalHeaderItem(coluna).text(),
    #                    for coluna in range(self.tableWidget.columnCount())
    #                    if not self.tableWidget.isColumnHidden(coluna)]
    #

    # Função para mostrar a tabela.
    def mostrarTabelaAlunos(self):
        import sqlite3
        db = sqlite3.connect("Database.db")
        cursor = db.cursor()

        # Função pra setar qual tabela será exibida.
        if self.colunas_box.currentText == "Alunos":
            result = cursor.execute("SELECT * FROM alunos;")
            nomeColunas = ("CPD", "Nome do aluno", "Telefone", "Endereço", "CEP", "Email", "Código do curso")
            self.tableWidget.setHorizontalHeaderLabels(nomeColunas)
            self.tableWidget.setColumnCount(7)
            row = 0

            for arrayDados in result:
                self.tableWidget.setRowCount(row + 1)
                self.tableWidget.setItem(row, 0, QtGui.QTableWidgetItem(str(arrayDados[0])))
                self.tableWidget.setItem(row, 1, QtGui.QTableWidgetItem(str(arrayDados[1])))
                self.tableWidget.setItem(row, 2, QtGui.QTableWidgetItem(str(arrayDados[2])))
                self.tableWidget.setItem(row, 3, QtGui.QTableWidgetItem(str(arrayDados[3])))
                self.tableWidget.setItem(row, 4, QtGui.QTableWidgetItem(str(arrayDados[4])))
                self.tableWidget.setItem(row, 5, QtGui.QTableWidgetItem(str(arrayDados[5])))
                self.tableWidget.setItem(row, 6, QtGui.QTableWidgetItem(str(arrayDados[6])))
                row += 1
        else:
            result = cursor.execute("SELECT * FROM cursos;")
            nomeColunas = ("Código do Curso", "Nome do Curso", "Carga Horária", "Data de cadastro")
            self.tableWidget.setHorizontalHeaderLabels(nomeColunas)
            self.tableWidget.setColumnCount(4)
            row = 0

            for arrayDados in result:
                self.tableWidget.setRowCount(row + 1)
                self.tableWidget.setItem(row, 0, QtGui.QTableWidgetItem(str(arrayDados[0])))
                self.tableWidget.setItem(row, 1, QtGui.QTableWidgetItem(str(arrayDados[1])))
                self.tableWidget.setItem(row, 2, QtGui.QTableWidgetItem(str(arrayDados[2])))
                self.tableWidget.setItem(row, 3, QtGui.QTableWidgetItem(str(arrayDados[3])))
                row += 1