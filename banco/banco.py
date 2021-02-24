import sqlite3
import os


class Banco:
    def __init__(self):

        dirbanco = os.path.normpath("banco/coletanea.sqlite")
        self.banco = sqlite3.connect(dirbanco)
        self.cursor = self.banco.cursor()
        # self.criarTabela()

    def criarTabela(self):

        self.cursor.execute(
            """
        CREATE TABLE coletaneas (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        musica TEXT NOT NULL,
        endereco_musica TEXT NOT NULL,
        numero INTEGER,
        album TEXT NOT NULL,
        trecho TEXT
        );
        """
        )
        print("tabela criada com sucesso")

    def selecionarDados(self, tipo, pesquisa):

        sql = """
                SELECT * FROM coletaneas
                WHERE {} LIKE'%{}%' order by numero
                """.format(
            tipo, pesquisa
        )

        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def pesquisa_album(self, album=0):
        
        if album == 0:
            sql = """ SELECT DISTINCT album FROM coletaneas order by id """
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        
        else:
            sql = """ SELECT DISTINCT album FROM coletaneas WHERE album LIKE '%{}%' order by id """.format(str(album))
            self.cursor.execute(sql)
            return self.cursor.fetchall()


    def selecionarColetanea(self, pesquisa):
        sql = """
                SELECT * FROM coletaneas
                WHERE album == '{}'  order by numero
                """.format(
            pesquisa
        )

        self.cursor.execute(sql)
        return self.cursor.fetchall()


"""
banco = banco()
banco.inserirDados('testeGrave','video.mp4',1,'teste','teste de grave')
"""
