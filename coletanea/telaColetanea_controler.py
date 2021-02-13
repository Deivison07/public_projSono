from PyQt5 import QtCore, QtGui, QtWidgets 
from coletanea.telaColetanea_view import Ui_Form
import os

class telaCole(QtWidgets.QWidget,Ui_Form):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def montarTelaColetanea(self,imagem,lista):
    	#imagem
    	self.label.clear()
    	path = os.path.normpath(f"iconesColetanea/{imagem}.jpg")
    	self.label.setPixmap(QtGui.QPixmap(path))

    	#lista
    	print(lista)
    	self.listWidget.clear()
    	for item in lista:
    		self.listWidget.addItem(str(item))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = telaCole()
    ui.show()
    sys.exit(app.exec_())