from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QApplication, QDesktopWidget
from player.player import Player
from banco.banco import Banco
from coletanea.coletaneas import coletanea


class Main(Player,coletanea):
    
    def __init__(self):
        super().__init__()
        self.bancoDeDados = Banco()
        coletanea.__init__(self)
        


        
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



