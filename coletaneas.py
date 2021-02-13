from PyQt5 import QtGui, QtWidgets, QtCore 
#self.lista_coletanea.setIconSize(QtCore.QSize(172, 250))
from coletanea.telaColetanea_controler import telaCole

class coletanea():
	"""docstring for coletanea"""
	def __init__(self):

		self.instanciaTela = telaCole()
		#self.instanciaTela.listWidget.itemClicked.connect(self.passou)
		self.instanciaTela.listWidget.itemDoubleClicked.connect(self.reproduzirColetanea)


		self.lista_coletanea.setIconSize(QtCore.QSize(172, 250))
		self.lista_coletanea.clear()

		self.lista_coletanea.itemClicked.connect(self.coletanea_clicada)
		self.lista_resultado_coletaneas = [ item[0] for item in self.bancoDeDados.pesquisa_album()]
		
		for item_coletanea in self.lista_resultado_coletaneas:
			self.add_item_coletanea(item_coletanea)
		
		
	def add_item_coletanea(self,nome):

	    item = QtWidgets.QListWidgetItem()
	    icone = QtGui.QIcon()
	    icone.addPixmap(QtGui.QPixmap(f"iconesColetanea/{nome}.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
	    item.setIcon(icone)
	    item.setText(f'{nome}'.upper())
	    self.lista_coletanea.addItem(item)

	def coletanea_clicada(self,item):
		self.instanciaTela.show()

	def reproduzirColetanea(self):
		self.reproduzirSimples('teste.webm')

		
    