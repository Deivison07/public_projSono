# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'telaColetanea.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.ApplicationModal)
        Form.resize(621, 542)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.boxColetanea = QtWidgets.QGroupBox(Form)
        self.boxColetanea.setMinimumSize(QtCore.QSize(603, 524))
        self.boxColetanea.setMaximumSize(QtCore.QSize(603, 524))
        self.boxColetanea.setTitle("")
        self.boxColetanea.setObjectName("boxColetanea")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.boxColetanea)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.boxColetanea)
        self.groupBox.setTabletTracking(False)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setEnabled(False)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayoutColetanea = QtWidgets.QHBoxLayout()
        self.horizontalLayoutColetanea.setObjectName("horizontalLayoutColetanea")
        self.horizontalLayoutColetanea_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayoutColetanea_2.setObjectName("horizontalLayoutColetanea_2")
        self.imagemColetanea = QtWidgets.QLabel(self.boxColetanea)
        self.imagemColetanea.setMinimumSize(QtCore.QSize(301, 421))
        self.imagemColetanea.setMaximumSize(QtCore.QSize(301, 421))
        self.imagemColetanea.setFrameShape(QtWidgets.QFrame.Box)
        self.imagemColetanea.setText("")
        self.imagemColetanea.setPixmap(QtGui.QPixmap("iconesColetanea/adoradores.jpg"))
        self.imagemColetanea.setScaledContents(True)
        self.imagemColetanea.setObjectName("imagemColetanea")
        self.horizontalLayoutColetanea_2.addWidget(self.imagemColetanea)
        self.horizontalLayoutColetanea.addLayout(self.horizontalLayoutColetanea_2)
        self.verticalLayoutColetanea = QtWidgets.QVBoxLayout()
        self.verticalLayoutColetanea.setObjectName("verticalLayoutColetanea")
        self.boatoColetanea = QtWidgets.QToolButton(self.boxColetanea)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icones/add-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boatoColetanea.setIcon(icon)
        self.boatoColetanea.setObjectName("boatoColetanea")
        self.verticalLayoutColetanea.addWidget(self.boatoColetanea, 0, QtCore.Qt.AlignRight)
        self.listaColetanea = QtWidgets.QListWidget(self.boxColetanea)
        self.listaColetanea.setMinimumSize(QtCore.QSize(256, 421))
        self.listaColetanea.setMaximumSize(QtCore.QSize(256, 421))
        self.listaColetanea.setStyleSheet("")
        self.listaColetanea.setObjectName("listaColetanea")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.listaColetanea.addItem(item)
        self.verticalLayoutColetanea.addWidget(self.listaColetanea)
        self.horizontalLayoutColetanea.addLayout(self.verticalLayoutColetanea)
        self.verticalLayout.addLayout(self.horizontalLayoutColetanea)
        self.horizontalLayout_2.addWidget(self.boxColetanea)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "<- Voltar"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Adoradores</span></p></body></html>"))
        self.boatoColetanea.setText(_translate("Form", "..."))
        __sortingEnabled = self.listaColetanea.isSortingEnabled()
        self.listaColetanea.setSortingEnabled(False)
        item = self.listaColetanea.item(0)
        item.setText(_translate("Form", "Teu santo nome"))
        self.listaColetanea.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
