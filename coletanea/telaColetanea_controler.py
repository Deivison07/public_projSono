from PyQt5 import QtCore, QtGui, QtWidgets 
from coletanea.telaColetanea_view import Ui_Form

class telaCole(QtWidgets.QWidget,Ui_Form):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = telaCole()
    ui.show()
    sys.exit(app.exec_())