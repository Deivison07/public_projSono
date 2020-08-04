from PyQt5 import QtCore, QtGui, QtWidgets
from TelaInicial import Ui_MainWindow
import player

class main(QtWidgets.QMainWindow, Ui_MainWindow, player.player):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        player.player.__init__(self)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = main()
    ui.show()
    sys.exit(app.exec_())

