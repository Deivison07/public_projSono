from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QMessageBox
from cadastro_view import Ui_form_cadastrar
import sqlite3
import os
import shutil


class Main(QtWidgets.QWidget,Ui_form_cadastrar):
    def __init__(self):

        super().__init__()
        self.setupUi(self)

        dirbanco = os.path.normpath('coletanea.sqlite')
        self.banco = sqlite3.connect(dirbanco)
        self.cursor = self.banco.cursor()

        self.botao_salvar.clicked.connect(self.save)
        self.botao_limpar.clicked.connect(self.limpar)
        self.botao_arquivo.clicked.connect(self.pach_arquivo)
    
    def inserirDados(self,musica,endereco_musica,numero,album,trecho):
        '''
            parametros:
                nome da musica
                o endereço da musica
                o numero caso seja hinario
                album
        '''
        end = endereco_musica.split('/')[-1]
        endereco_musica = f'musicas/{album}/{end}'
        self.cursor.execute("""
        INSERT INTO coletaneas (musica, endereco_musica, numero, album,trecho)
        VALUES (?,?,?,?,?)
        """,(musica,endereco_musica,numero,album,trecho))
        try:
            self.banco.commit()

            mensagem = QMessageBox()
            mensagem.setWindowTitle('Sucesso')
            mensagem.setText('Salvo com Sucesso')
            mensagem.setStandardButtons(QMessageBox.Ok)
            mensagem.exec_()

            self.prepara_arquivos(album,musica)
            self.limpar()

        except Exception:
            mensagem = QMessageBox()
            mensagem.setWindowTitle('Erro ao salvar')
            mensagem.setText('Erro inesperado, verifique se algum campo não foi preenchido\n ou a midia selecionada foi sobreescrevida')
            mensagem.setIcon(QMessageBox.Critical)
            mensagem.exec_()
            


    
    def save(self):
        nome = self.campo_nome.text()
        self.album  = self.campo_album.text().upper()
        numero = self.numero_musica.value()
        self.arquivo = self.campo_arquivo.text()
        texto = self.campo_texto.toPlainText()

        self.inserirDados(nome,self.arquivo,numero,self.album,texto)




    
    def limpar(self):
        self.campo_nome.clear()
        self.campo_album.clear()
        self.numero_musica.clear()
        self.campo_arquivo.clear()
        self.campo_texto.clear()

    def pach_arquivo(self):
        arquivo = QtWidgets.QFileDialog.getOpenFileName()
        if arquivo[0] != '':
            self.campo_arquivo.setText(str(arquivo[0]))
            nome = arquivo[0]
            nome = nome.split('/')
            nome = nome[-1]
            nome = nome.split('.')
            nome = nome[0]

            self.campo_nome.setText(nome)
    
    def prepara_arquivos(self,album,arquivo):

        try:
            pach = os.path.normpath(f'../musicas/{album}')
            os.makedirs(pach)
            shutil.copy(self.arquivo, pach)

        except FileExistsError:
            shutil.copy(self.arquivo, pach)

        except:
            mensagem = QMessageBox()
            mensagem.setWindowTitle('Erro ao salvar')
            mensagem.setText('Erro ao criar pasta')
            mensagem.setIcon(QMessageBox.Critical)
            mensagem.exec_()










    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Main()
    ui.show()
    sys.exit(app.exec_())
