# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from adicionar import Ui_adicionarC
from adicionar2 import Ui_adicionarA

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

        # Setup do menu das tabelas.
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidget.setGeometry(QtCore.QRect(20, 80, 711, 151))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(1)
        self.tableWidget.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(20)

        # Setup do botão consultar.
        self.consulta_button = QtGui.QPushButton(self.centralwidget)
        self.consulta_button.setGeometry(QtCore.QRect(20, 30, 90, 30))
        self.consulta_button.setObjectName(_fromUtf8("consulta_button"))
        self.consulta_button.clicked.connect(self.mostrarTabela)
        self.tableWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)

        # Setup do botão Adicionar.
        self.adiciona_button = QtGui.QPushButton(self.centralwidget)
        self.adiciona_button.setGeometry(QtCore.QRect(80, 410, 90, 30))
        self.adiciona_button.setObjectName(_fromUtf8("adiciona_button"))
        self.adiciona_button.clicked.connect(self.adicionaWindow)

        # Setup do botão Alterar.
        self.alterar_button = QtGui.QPushButton(self.centralwidget)
        self.alterar_button.setGeometry(QtCore.QRect(490, 410, 90, 30))
        self.alterar_button.setObjectName(_fromUtf8("alterar_button"))

        # Setup do botão Remover.
        self.remover_button = QtGui.QPushButton(self.centralwidget)
        self.remover_button.setGeometry(QtCore.QRect(610, 410, 90, 30))
        self.remover_button.setObjectName(_fromUtf8("remover_button"))
        # self.remover_button.clicked.connect(self.removerTabela)

        # Setup da label de inserção de novas linhas
        self.insira_lbl = QtGui.QLabel(self.centralwidget)
        self.insira_lbl.setGeometry(QtCore.QRect(20, 350, 220, 40))
        self.insira_lbl.setObjectName(_fromUtf8("insira_lbl"))

        # Setup da label de alterar/remover linhas existentes.
        self.altera_lbl = QtGui.QLabel(self.centralwidget)
        self.altera_lbl.setGeometry(QtCore.QRect(470, 360, 250, 20))
        self.altera_lbl.setObjectName(_fromUtf8("altera_lbl"))

        # Setup do combobox para seleção de tabelas.
        self.colunas_box = QtGui.QComboBox(self.centralwidget)
        self.colunas_box.setGeometry(QtCore.QRect(130, 30, 211, 31))
        self.colunas_box.setEditable(False)
        self.colunas_box.setObjectName(_fromUtf8("colunas_box"))
        self.colunas_box.addItem("Alunos")
        self.colunas_box.addItem("Cursos")

        # Setup do botão de limpar a tabela.
        self.apagar_button = QtGui.QPushButton(self.centralwidget)
        self.apagar_button.setGeometry(QtCore.QRect(610, 30, 120, 30))
        self.apagar_button.setObjectName(_fromUtf8("apagar_button"))
        self.apagar_button.clicked.connect(self.apagarTabela)
        menu.setCentralWidget(self.centralwidget)


        self.retranslateUi(menu)
        QtCore.QMetaObject.connectSlotsByName(menu)



    #Função para limpar as entradas na tabela.
    def apagarTabela(self):
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)

    def retranslateUi(self, menu):
        menu.setWindowTitle(_translate("menu", "Tabelas", None))
        self.consulta_button.setText(_translate("menu", "Consultar", None))
        self.apagar_button.setText(_translate("menu", "Limpar tela", None))
        self.adiciona_button.setText(_translate("menu", "Adicionar", None))
        self.alterar_button.setText(_translate("menu", "Alterar", None))
        self.remover_button.setText(_translate("menu", "Remover", None))
        self.insira_lbl.setText(_translate("menu", "Deseja inserir uma nova linha? Clique abaixo", None))
        self.altera_lbl.setText(_translate("menu", "Deseja alterar um linha já existente? Clique abaixo", None))

    # Função para mostrar a tabela.
    def mostrarTabela(self):
        import sqlite3
        db = sqlite3.connect("Database.db")
        cursor = db.cursor()

        # Função pra setar qual tabela será exibida.
        if self.colunas_box.currentText() == "Alunos":
            result = cursor.execute("SELECT * FROM alunos;")
            self.tableWidget.setColumnCount(7)
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
            self.tableWidget.setColumnCount(4)
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
        db.commit()
        db.close()

    # Função para remover uma tupla da tabela
    # def removerTabela(self):
    #     import sqlite3
    #     db = sqlite3.connect("Database.py")
    #     cursor = db.cursor()
    #     if self.tableWidget.selectedItems()
    #         self.showMessageBox("Aviso", "Você não selecionou nenhuma linha.")
        # else:

    def adicionaWindow(self):
        if self.colunas_box.currentText() == "Alunos":
            self.adiciona_button.clicked.connect(self.adicionaAlunosWindowshow)
        else:
            self.adiciona_button.clicked.connect(self.adicionaCursoWindowshow)

    # Função mostrar o menu de inserção na tabela Cursos.
    def adicionaCursoWindowshow(self):
        self.adicionaCWindow = QtGui.QDialog()
        self.ui = Ui_adicionarC()
        self.ui.setupUi(self.adicionaCWindow)
        self.adicionaCWindow.show()

    # Função mostrar o menu de inserção na tabela Alunos.
    def adicionaAlunosWindowshow(self):
        self.adicionaAWindow = QtGui.QDialog()
        self.ui = Ui_adicionarA()
        self.ui.setupUi(self.adicionaAWindow)
        self.adicionaAWindow.show()

    # Mostra uma caixa de diálogo.
    def showMessageBox(self, title, message):
        msgBox = QtGui.QMessageBox()
        msgBox.setIcon(QtGui.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
        msgBox.exec_()