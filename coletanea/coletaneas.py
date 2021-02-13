from PyQt5 import QtGui, QtWidgets, QtCore 
#self.lista_coletanea.setIconSize(QtCore.QSize(172, 250))
from coletanea.telaColetanea_controler import telaCole
import os

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
	    icone.addPixmap(QtGui.QPixmap(os.path.normpath(f"iconesColetanea/{nome}.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.On)
	    item.setIcon(icone)
	    item.setText(f'{nome}'.upper())
	    self.lista_coletanea.addItem(item)
	    self.imagem = nome

	def coletanea_clicada(self,item):
		self.lista_coletanea_nome = []
		self.lista_coletanea_endereco = []
		self.lista_coletanea = self.bancoDeDados.selecionarColetanea(pesquisa= item.text())
		
		for listaItem in self.lista_coletanea:
			self.lista_coletanea_nome.append(str(listaItem[1]))
			self.lista_coletanea_endereco.append(listaItem[2])

		self.instanciaTela.montarTelaColetanea(self.imagem,self.lista_coletanea_nome)
		self.instanciaTela.show()

	def reproduzirColetanea(self,item):
		index = self.instanciaTela.listWidget.row(item)
		self.reproduzirSimples(self.lista_coletanea_endereco[index])

		
    