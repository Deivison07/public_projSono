from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QApplication, QDesktopWidget
from TelaInicial import Ui_MainWindow
import player
from banco import banco

class main(player.player):
    
    def __init__(self):
        super().__init__()
        player.player.__init__(self)
        self.bancoDeDados = banco()
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = main()
    display_monitor = len(QtGui.QGuiApplication.screens())
    monitor = QDesktopWidget().screenGeometry(0)
    ui.move(monitor.left(), monitor.top())
    ui.show()
    sys.exit(app.exec_())


