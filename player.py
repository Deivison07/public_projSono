import sys
import vlc 
from time import sleep
from PyQt5 import QtWidgets,QtGui 
from TelaInicial import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QDesktopWidget
from PyQt5.QtCore import pyqtSlot, QTimer

    
class Player(QtWidgets.QMainWindow,Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #Tela secundaria
        self.telaSecundaria = QtWidgets.QWidget()

        #Tela principal
        self.listaDeMidia = []
        self.botaoAdicionar.clicked.connect(self.adicionarExterno) # conector botaoAdicionar para função adicionarExterno
        self.botaoRemover.clicked.connect(self.removerItemDePlayList) # conector botaoRemover para função removerItemDePlayList
        self.listaPlaylist.itemClicked.connect(self.itemclicadoPlayList)  # conector listaPlaylist para função removerItemDePlayList
        self.listaPlaylist.itemDoubleClicked.connect(self.midiaParaReproduzirVindoDaLista)
        self.botaoVolume.clicked.connect(self.mutar)
        self.botaoPlay.clicked.connect(self.play)
        self.botaoStop.clicked.connect(self.stop)
        self.slideVolume.sliderMoved.connect(self.volume)
        self.slideMusica.sliderPressed.connect(self.slidePressed)
        self.slideMusica.sliderReleased.connect(self.slideReleased)
        self.slideMusica.sliderMoved.connect(self.mudartempo)
        self.comboMusica.activated.connect(self.mudarFaixaDeAudio)
        self.comboLegenda.activated.connect(self.mudarFaixaDeLegenda)
        self.areaBusca.returnPressed.connect(self.busca)
        self.listaBanco.itemDoubleClicked.connect(self.midiaParaReproduzirVindoDoBanco)
        self.botaoAdicionar_2.clicked.connect(self.itemDoBancoParaPlaylist)
        self.listaBanco.itemClicked.connect(self.itemClicadoBanco)
        self.botaoRedimencionar.clicked.connect(self.redimencionar)
        self.botaoPlayList.clicked.connect(self.playList)
        self.listaTrecho.setVisible(False)

        self.slideMusicaPressionado = 0
        self.botaoRedimencionarEstado = 0
        self.ativarPlayList = False
        self.audios = False
        self.legendas = False


        #reprodutor
        self.player = vlc.Instance()
        
        self.mediaList = self.player.media_list_new()
        self.mediaInstancia = self.player.media_list_new()
        
        self.reprodutorInstance2 = self.player.media_player_new()
        

        self.reprodutorInstance = self.player.media_player_new()
        

        if sys.platform.startswith('linux'): # para linux X Server
            self.reprodutorInstance2.set_xwindow(self.telaSecundaria.winId())
            self.reprodutorInstance.set_xwindow(self.frameVideo.winId())

        elif sys.platform == "win32": # para Windows
            self.reprodutorInstance2.set_hwnd(self.telaSecundaria.winId())
            self.reprodutorInstance.set_hwnd(self.frameVideo.winId())

        elif sys.platform == "darwin": # para MacOS
            self.reprodutorInstance.set_nsobject(int(self.frameVideo.winId()))
            self.reprodutorInstance2.set_nsobject(int(self.telaSecundaria.winId()))

        self.reprodutorInstance.stop()
        self.reprodutorInstance.audio_set_volume(100)
        
        self.reprodutorInstancePlayList = vlc.MediaListPlayer()
        self.reprodutorInstancePlayList.set_media_list(self.mediaList)
        self.reprodutorInstancePlayList.set_media_player(self.reprodutorInstance)

        self.reprodutorInstancePlayListExterno = vlc.MediaListPlayer()
        self.reprodutorInstancePlayListExterno.set_media_list(self.mediaList)
        self.reprodutorInstancePlayListExterno.set_media_player(self.reprodutorInstance2)
        
        #lista a tela secundaria do sistema

        display_monitor = len(QtGui.QGuiApplication.screens()) #quantas telas tem no sistema
        monitor = QDesktopWidget().screenGeometry(1) #propriedades do monitor
        self.telaSecundaria.move(monitor.left(), monitor.top()) #informando para a tela secundaria qual monitor aparecerá
        
        #Eventos
        event_manager = self.reprodutorInstance.event_manager()
        event_manager.event_attach(vlc.EventType.MediaPlayerPlaying, self.reproduzindo)
        event_manager.event_attach(vlc.EventType.MediaPlayerMuted, self.mute)
        event_manager.event_attach(vlc.EventType.MediaPlayerPositionChanged,self.tempo)
        event_manager.event_attach(vlc.EventType.MediaPlayerEndReached,self.fimdaReproducao)
        
        
        #Timer
        self.timer = QTimer(self)
        
    def adicionarExterno(self):
        '''
                adicionar midia externa a playlist
        '''
        self.arquivo = QtWidgets.QFileDialog.getOpenFileName()
        if self.arquivo[0] != '':
            self.listaDeMidia.append(self.arquivo[0])
            #self.mediaList.add_media(self.arquivo[0])

            self.arquivo = self.arquivo[0].split('/')
            self.listaPlaylist.addItem(str(self.arquivo[-1]))

    def removerItemDePlayList(self):
        try:
            item = self.listaPlaylist.row(self.itemClicado)

            del(self.listaDeMidia[item])
            self.mediaList.remove_index(item)
            self.listaPlaylist.takeItem(item)
            
            print(self.listaDeMidia)


        except:
            print('não selecionou nenhum item')
                 
    def itemclicadoPlayList(self,item):
        self.itemClicado = item
    
    def midiaParaReproduzirVindoDaLista(self,arg):
        self.contadorDeMidia = 0
        #remove tudo
        cont = self.mediaList.count()
        for x in range(cont):
            self.mediaList.remove_index(0)

        index = self.listaPlaylist.row(arg)

        #adiciona o que está na lista   
        if self.ativarPlayList:
            
            cont = len(self.listaDeMidia)
            for x in range(cont):
                self.mediaList.add_media(self.listaDeMidia[x])
                self.contadorDeMidia += 1
            self.texto.setText('Execultando modo Playlist') 
            self.reprodutor(index)
        else:
            self.contadorDeMidia = 1
            self.texto.setText('Execultando modo Single') 
            self.mediaList.add_media(self.listaDeMidia[index])
            self.reprodutor(0)
    
    def midiaParaReproduzirVindoDoBanco(self,arg):
        cont = self.mediaList.count()
        self.contadorDeMidia = 1

        for x in range(cont):
            self.mediaList.remove_index(0)
            
        self.arq = self.listaDeMidiaBanco[self.listaBanco.row(arg)]
        self.mediaList.add_media(self.arq)
        self.texto.setText('Execultando modo Single')      
        self.reprodutor(0)  

    def reprodutor(self,index=0):
        
        self.reprodutorInstancePlayList.play_item_at_index(index)
        
        if sys.platform.startswith('linux'): # para linux X Server
            self.reprodutorInstance2.set_xwindow(self.telaSecundaria.winId())
            self.reprodutorInstance.set_xwindow(self.frameVideo.winId())

        elif sys.platform == "win32": # para Windows
            self.reprodutorInstance2.set_hwnd(self.telaSecundaria.winId())
            self.reprodutorInstance.set_hwnd(self.frameVideo.winId())

        elif sys.platform == "darwin": # para MacOS
            self.reprodutorInstance.set_nsobject(int(self.frameVideo.winId()))
            self.reprodutorInstance2.set_nsobject(int(self.telaSecundaria.winId()))

        self.reprodutorInstancePlayListExterno.play_item_at_index(index)
        self.reprodutorInstance2.audio_set_mute(True)

        if self.botaoRedimencionarEstado == True:
            self.telaSecundaria.setVisible(True)

    def reproduzindo(self,event):
        self.botaoPlay.setEnabled(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icones/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botaoPlay.setIcon(icon1)
        self.informacaoMidia()
        
    def informacaoMidia(self):
        self.comboMusica.clear()

        self.audios = self.reprodutorInstance.audio_get_track_description()
        self.legendas = self.reprodutorInstance.video_get_spu_description()

        audio = [list(Tuple) for Tuple in self.audios]
        print(audio)
        
        for faixas_audio in audio:
            print(faixas_audio)

            self.comboMusica.addItem(str(faixas_audio[1].decode('UTF-8')))
        self.comboMusica.setCurrentIndex(1)

        self.comboLegenda.clear()

        legendas = [list(Tuple) for Tuple in self.legendas]

        for faixas_legenda in legendas:
            self.comboLegenda.addItem(str(faixas_legenda[1].decode('UTF-8')))
        self.comboLegenda.setCurrentIndex(1)
        
    def play(self):

        if self.reprodutorInstance.is_playing():
            self.reprodutorInstance.pause()
            self.reprodutorInstance2.pause()
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap("icones/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.botaoPlay.setIcon(icon1)
        else:
            print('não play')
            self.reprodutorInstance.play()
            self.reprodutorInstance2.play()

    def stop(self):
        
        self.reprodutorInstance.stop() #para player principal


        self.telaSecundaria.setVisible(False)
        self.reprodutorInstance2.set_position(0) #o player da tela secundaria não da stop e sim fica invisivel na posição 0
        self.reprodutorInstance2.pause()
        #self.botaoRedimencionar.setChecked(False)
        
        #self.botaoPlay.setEnabled(False)

        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icones/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botaoPlay.setIcon(icon1)
        self.slideMusica.setValue(0)

        self.comboLegenda.clear()
        self.comboMusica.clear()
        
    def mute(self,event):
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icones/iconfinder-volume-mute-sound-speaker-audio-4593175_122269.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botaoVolume.setIcon(icon1)
            
    def mutar(self):
        if self.reprodutorInstance.audio_get_mute():
            self.reprodutorInstance.audio_set_mute(False)
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap("icones/iconfinder-volume-max-sound-speaker-audio-4593170_122277.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.botaoVolume.setIcon(icon1)
        else:
            self.reprodutorInstance.audio_set_mute(True)
            
    def volume(self,arg):
        self.reprodutorInstance.audio_set_volume(arg)
    
    def tempo(self,event):
        if self.slideMusicaPressionado == False:
            self.slideMusica.setValue(self.reprodutorInstance.get_position()*100)

    def slidePressed(self):
        self.slideMusicaPressionado = True

    def slideReleased(self):
        self.slideMusicaPressionado = False
        
    def mudartempo(self,arg):

        self.reprodutorInstance.set_position(arg/100)
        self.reprodutorInstance2.set_position(arg/100)

    def fimdaReproducao(self,event):
        self.slideMusica.setValue(0)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icones/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botaoPlay.setIcon(icon1)
        self.botaoPlay.setEnabled(False)
        self.contadorDeMidia-=1
        try:
            if self.contadorDeMidia == 0:
                self.telaSecundaria.setVisible(False)
        except Exception:
            print('erro na contagem de midia')
         
    def mudarFaixaDeAudio(self,arg):


        if arg == 0:
            self.reprodutorInstance.audio_set_track(-1)
            self.reprodutorInstance2.audio_set_track(-1) # é usado -1 porque o vlc usa esse indice para desabilitar o audio

        else:
            self.reprodutorInstance.audio_set_track(arg)
            self.reprodutorInstance2.audio_set_mute(True)
    
    def mudarFaixaDeLegenda(self,arg):

        if arg == 0:
            self.reprodutorInstance.video_set_spu(-1)
            self.reprodutorInstance2.video_set_spu(-1) # é usado -1 porque o vlc usa esse indice para desabilitar o audio
        else:
            self.reprodutorInstance.video_set_spu(arg)
            self.reprodutorInstance2.video_set_spu(arg)
    
    def busca(self):

        self.listaBanco.clear()
        self.listaDeMidiaBanco = []

        texto = self.areaBusca.text()
        indice = self.comboBanco.currentIndex()
        tipo  = self.comboBanco.itemText(indice).lower()

        itens = self.bancoDeDados.selecionarDados(tipo,texto)

        for faixas in itens:
            self.listaBanco.addItem(faixas[1])
            self.listaDeMidiaBanco.append(faixas[2])

    def itemDoBancoParaPlaylist(self):
        try:
            item = self.listaDeMidiaBanco[self.listaBanco.row(self.itemBanco)]
            self.listaDeMidia.append(item)
            self.mediaList.add_media(item)
            
            self.listaPlaylist.addItem(self.itemBanco.text())
        except Exception:
            print(Exception)
        
    def itemClicadoBanco(self,arg):
        self.itemBanco = arg
    
    def redimencionar(self,arg):
        print(arg)
        self.botaoRedimencionarEstado = arg
        if arg:
            self.telaSecundaria.setVisible(True)
            self.telaSecundaria.showFullScreen()
        else:
            self.telaSecundaria.setVisible(False)

    def playList(self,arg):
        self.ativarPlayList = arg


