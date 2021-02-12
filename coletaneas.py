from PyQt5 import QtGui, QtWidgets, QtCore 
#self.lista_coletanea.setIconSize(QtCore.QSize(172, 250))

class coletanea():
	"""docstring for coletanea"""
	def __init__(self):

		self.lista_coletanea.setIconSize(QtCore.QSize(172, 250))
		self.lista_coletanea.clear()
		#self.add_item_coletanea('adoradores')
		self.lista_coletanea.itemClicked.connect(self.coletanea_clicada)
		
		
	def add_item_coletanea(self,nome):

	    item = QtWidgets.QListWidgetItem()
	    icone = QtGui.QIcon()
	    icone.addPixmap(QtGui.QPixmap(f"iconesColetanea/{nome}.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
	    item.setIcon(icone)
	    item.setText(f'{nome}'.upper())
	    self.lista_coletanea.addItem(item)

	def coletanea_clicada(self,item):
		print(item.text())
    