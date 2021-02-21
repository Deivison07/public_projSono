from PyQt5 import QtGui, QtWidgets, QtCore 
#self.lista_coletanea.setIconSize(QtCore.QSize(172, 250))
from coletanea.telaColetanea_controler import telaCole
import os

class coletanea():
	"""docstring for coletanea"""
	def __init__(self):

		self.instanciaTela = telaCole()
		#self.instanciaTela.listWidget.itemClicked.connect(self.passou)
		self.listaColetanea.itemActivated.connect(self.reproduzirColetanea)

		self.lista_coletanea.setIconSize(QtCore.QSize(172, 250))
		self.lista_coletanea.clear()

		self.lista_coletanea.itemActivated.connect(self.coletanea_clicada)
		self.pushButton.clicked.connect(self.voltar_coletanea)

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
	    

	def coletanea_clicada_pop_up(self,item):

		self.lista_coletanea_nome = []
		self.lista_coletanea_endereco = []
		self.lista_coletanea = self.bancoDeDados.selecionarColetanea(pesquisa= item.text())
		imagem = item.text()

		for listaItem in self.lista_coletanea:

			self.lista_coletanea_nome.append(str(listaItem[1]))
			self.lista_coletanea_endereco.append(listaItem[2])

		self.montarTelaColetanea(imagem,self.lista_coletanea_nome)
		

	def reproduzirColetanea(self,item):
		try:
			index = self.listaColetanea.row(item)
			self.reproduzirSimples(self.lista_coletanea_endereco[index])
		except Exception:
			pass

	def coletanea_clicada(self,item):

		self.boxListaColetanea.close()
		self.lista_coletanea_nome = []
		self.lista_coletanea_endereco = []
		self.lista_coletanea = self.bancoDeDados.selecionarColetanea(pesquisa= item.text())
		imagem = item.text()
		for listaItem in self.lista_coletanea:
			self.lista_coletanea_nome.append(str(listaItem[1]))
			self.lista_coletanea_endereco.append(listaItem[2])

		self.montarTelaColetanea(imagem,self.lista_coletanea_nome)
		
		self.boxColetanea.show()

	def voltar_coletanea(self):

		self.boxColetanea.close()
		self.boxListaColetanea.show()
		
	def montarTelaColetanea(self,imagem,lista):

		self.label.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">{imagem}</span></p></body></html>")
		self.imagemColetanea.clear()
		path = os.path.normpath(f"iconesColetanea/{imagem}.jpg")
		self.imagemColetanea.setPixmap(QtGui.QPixmap(path))

		#lista
		self.listaColetanea.clear()
		for item in lista:
			self.listaColetanea.addItem(str(item))


    