from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QApplication, QDesktopWidget
from TelaInicial import Ui_MainWindow
import player
from banco import Banco
import coletaneas

class Main(player.Player,coletaneas.coletanea):
    
    def __init__(self):
        super().__init__()
        #player.Player.__init__(self)
        coletaneas.coletanea.__init__(self)
        self.bancoDeDados = Banco()

        
    def closeEvent(self, event): #evento de fechamento de programa
        self.telaSecundaria.close()
        
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Main()
    display_monitor = len(QtGui.QGuiApplication.screens())
    monitor = QDesktopWidget().screenGeometry(0)
    ui.move(monitor.left(), monitor.top())
    ui.show()
    sys.exit(app.exec_())



