import sqlite3

class Banco():

    def __init__(self):
        self.banco = sqlite3.connect('banco/coletanea.sqlite')
        self.cursor = self.banco.cursor()
        #self.criarTabela()
    
    def criarTabela(self):

        self.cursor.execute("""
        CREATE TABLE coletaneas (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        musica TEXT NOT NULL,
        endereco_musica TEXT NOT NULL,
        numero INTEGER,
        album TEXT NOT NULL,
        trecho TEXT
        );
        """)
        print('tabela criada com sucesso')

    def selecionarDados(self,tipo,pesquisa):

        sql = ("""
                SELECT * FROM coletaneas
                WHERE {} LIKE'%{}%' order by id
                """.format(tipo,pesquisa))

        self.cursor.execute(sql)
        return self.cursor.fetchall()
            
    def inserirDados(self,musica,endereco_musica,numero,album,trecho):
        '''
            parametros:
                nome da musica
                o endereço da musica
                o numero caso seja hinario
                album
        '''
        self.cursor.execute("""
        INSERT INTO coletaneas (musica, endereco_musica, numero, album,trecho)
        VALUES (?,?,?,?,?)
        """,(musica,endereco_musica,numero,album,trecho))

        self.banco.commit()

'''
banco = banco()
banco.inserirDados('testeGrave','video.mp4',1,'teste','teste de grave')
'''


    