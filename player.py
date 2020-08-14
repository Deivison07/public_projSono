import vlc 
from PyQt5 import QtWidgets,QtGui 
from TelaInicial import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QDesktopWidget
from PyQt5.QtCore import pyqtSlot, QTimer

    
class player():

    def __init__(self):
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

        self.slideMusicaPressionado = 0


        #reprodutor
        self.player = vlc.Instance()
        self.mediaList = self.player.media_list_new()
        
        self.reprodutorInstance2 = self.player.media_player_new()
        self.reprodutorInstance2.set_hwnd(self.telaSecundaria.winId())

        self.reprodutorInstance = self.player.media_player_new()
        self.reprodutorInstance.set_hwnd(self.frameVideo.winId())

        #lista a tela secundaria do sistema

        display_monitor = len(QtGui.QGuiApplication.screens())
        monitor = QDesktopWidget().screenGeometry(1)
        self.telaSecundaria.move(monitor.left(), monitor.top())
        
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
            self.arquivo = self.arquivo[0].split('/')
            self.listaPlaylist.addItem(str(self.arquivo[-1]))

    def removerItemDePlayList(self):
        try:

            del(self.listaDeMidia[self.listaPlaylist.row(self.itemClicado)])
            self.listaPlaylist.takeItem(self.listaPlaylist.row(self.itemClicado))
            
            print(self.listaDeMidia)


        except:
            print('não selecionou nenhum item')
                 
    def itemclicadoPlayList(self,item):
        self.itemClicado = item
    
    def midiaParaReproduzirVindoDaLista(self,arg):
    
        arq = self.listaDeMidia[self.listaPlaylist.row(arg)] 
        self.reprodutor(arq)
    
    def midiaParaReproduzirVindoDoBanco(self,arg):
        arq = self.listaDeMidiaBanco[self.listaBanco.row(arg)]
        self.reprodutor(arq)

    def reprodutor(self,arg):
        
        self.midia = self.player.media_new(arg) #caminho do arquivo para ser execultado
        self.midia.parse() # essaa função tem que ser execultada para que os dados possam ser obtidos

        #segundo reprodutor
        self.reprodutorInstance2.set_hwnd(self.telaSecundaria.winId())
        self.reprodutorInstance2.set_media(self.midia)
        self.reprodutorInstance2.play()
        self.reprodutorInstance2.audio_set_mute(True)

        #self.telaSecundaria.setVisible(True)
        #self.telaSecundaria.showFullScreen()
        
        #primeiro reprodutor
        self.reprodutorInstance.set_media(self.midia)
        self.reprodutorInstance.play()
        self.reprodutorInstance.set_hwnd(self.frameVideo.winId())
        
        
        self.timer.timeout.connect(self.informacaoMidia)
        self.timer.start(500)

    def reproduzindo(self,event):

        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icones/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botaoPlay.setIcon(icon1)
        #self.telaSecundaria.show()
    
    def informacaoMidia(self):
        self.audios = self.reprodutorInstance.audio_get_track_description()
        self.legendas = self.reprodutorInstance.video_get_spu_description()
        print(self.audios)

        self.comboMusica.clear()
        
        audio = [list(Tuple) for Tuple in self.audios]
        
        for faixas_audio in audio:
            self.comboMusica.addItem(str(faixas_audio[1]))
        self.comboMusica.setCurrentIndex(1)

        self.comboLegenda.clear()

        legendas = [list(Tuple) for Tuple in self.legendas]

        for faixas_legenda in legendas:
            self.comboLegenda.addItem(faixas_legenda[1].decode('UTF-8'))
        self.comboLegenda.setCurrentIndex(1)
        
        self.timer.stop()

    def play(self):

        if self.reprodutorInstance.is_playing():
            self.reprodutorInstance.pause()
            self.reprodutorInstance2.pause()
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap("icones/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.botaoPlay.setIcon(icon1)
        else:
            self.reprodutorInstance.play()
            self.reprodutorInstance2.play()
            self.timer.timeout.connect(self.informacaoMidia)
            self.timer.start(500)
   
    def stop(self):
        
        self.reprodutorInstance.stop() #para player principal


        self.telaSecundaria.setVisible(False)
        self.reprodutorInstance2.set_position(0) #o player da tela secundaria não da stop e sim fica invisivel na posição 0
        self.reprodutorInstance2.pause()
        

        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icones/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botaoPlay.setIcon(icon1)
        self.slideMusica.setValue(0)

        self.comboLegenda.clear()
        self.comboMusica.clear()
        self.botaoRedimencionar.setChecked(False)

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
    
    def mudarFaixaDeAudio(self,arg):
        print(arg)

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
            self.listaPlaylist.addItem(self.itemBanco.text())
        except Exception:
            print(Exception)
        
    def itemClicadoBanco(self,arg):
        self.itemBanco = arg
    
    def redimencionar(self,arg):
        if arg:
            self.telaSecundaria.setVisible(True)
            self.telaSecundaria.showFullScreen()
        else:
            self.telaSecundaria.setVisible(False)

        