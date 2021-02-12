# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadastro.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_form_cadastrar(object):
    def setupUi(self, form_cadastrar):
        form_cadastrar.setObjectName("form_cadastrar")
        form_cadastrar.resize(309, 416)
        form_cadastrar.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(form_cadastrar)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(form_cadastrar)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.campo_nome = QtWidgets.QLineEdit(form_cadastrar)
        self.campo_nome.setObjectName("campo_nome")
        self.horizontalLayout.addWidget(self.campo_nome)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(form_cadastrar)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.campo_album = QtWidgets.QLineEdit(form_cadastrar)
        self.campo_album.setObjectName("campo_album")
        self.horizontalLayout_2.addWidget(self.campo_album)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(form_cadastrar)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.numero_musica = QtWidgets.QSpinBox(form_cadastrar)
        self.numero_musica.setObjectName("numero_musica")
        self.horizontalLayout_3.addWidget(self.numero_musica)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(form_cadastrar)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.campo_arquivo = QtWidgets.QLineEdit(form_cadastrar)
        self.campo_arquivo.setObjectName("campo_arquivo")
        self.horizontalLayout_4.addWidget(self.campo_arquivo)
        self.botao_arquivo = QtWidgets.QToolButton(form_cadastrar)
        self.botao_arquivo.setObjectName("botao_arquivo")
        self.horizontalLayout_4.addWidget(self.botao_arquivo)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(form_cadastrar)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.campo_texto = QtWidgets.QTextEdit(form_cadastrar)
        self.campo_texto.setObjectName("campo_texto")
        self.verticalLayout.addWidget(self.campo_texto)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.botao_salvar = QtWidgets.QPushButton(form_cadastrar)
        self.botao_salvar.setObjectName("botao_salvar")
        self.horizontalLayout_5.addWidget(self.botao_salvar)
        self.botao_limpar = QtWidgets.QPushButton(form_cadastrar)
        self.botao_limpar.setObjectName("botao_limpar")
        self.horizontalLayout_5.addWidget(self.botao_limpar)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.retranslateUi(form_cadastrar)
        QtCore.QMetaObject.connectSlotsByName(form_cadastrar)

    def retranslateUi(self, form_cadastrar):
        _translate = QtCore.QCoreApplication.translate
        form_cadastrar.setWindowTitle(_translate("form_cadastrar", "Form"))
        self.label.setText(_translate("form_cadastrar", "Nome:"))
        self.label_2.setText(_translate("form_cadastrar", "Album:"))
        self.label_3.setText(_translate("form_cadastrar", "Numero:"))
        self.label_4.setText(_translate("form_cadastrar", "Arquivo:"))
        self.botao_arquivo.setText(_translate("form_cadastrar", "..."))
        self.label_5.setText(_translate("form_cadastrar", "Trecho:"))
        self.botao_salvar.setText(_translate("form_cadastrar", "Salvar"))
        self.botao_limpar.setText(_translate("form_cadastrar", "Limpar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form_cadastrar = QtWidgets.QWidget()
    ui = Ui_form_cadastrar()
    ui.setupUi(form_cadastrar)
    form_cadastrar.show()
    sys.exit(app.exec_())
