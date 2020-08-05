import vlc 
from PyQt5 import QtWidgets,QtGui
from TelaInicial import Ui_MainWindow
import time

class player():

    def __init__(self):

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

        self.comboMusica.currentIndexChanged.connect(self.mudarFaixaDeAudio)

        self.player = vlc.Instance()

        self.mediaList = self.player.media_list_new()
        self.reprodutorInstance = self.player.media_player_new()
        self.reprodutorInstance2 = self.player.media_player_new()
        self.reprodutorInstance.set_hwnd(self.frameVideo.winId())

        event_manager = self.reprodutorInstance.event_manager()
        event_manager.event_attach(vlc.EventType.MediaPlayerPlaying, self.reproduzindo)
        event_manager.event_attach(vlc.EventType.MediaPlayerMuted, self.mute)
        event_manager.event_attach(vlc.EventType.MediaPlayerPositionChanged,self.tempo)
        event_manager.event_attach(vlc.EventType.MediaPlayerEndReached,self.fimdaReproducao)
         

        self.slideMusicaPressionado = 0

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

    def reprodutor(self,arg):
        
        self.midia = self.player.media_new(arg) #caminho do arquivo para ser execultado
        self.midia.parse() # essaa função tem que ser execultada para que os dados possam ser obtidos

        self.reprodutorInstance.set_media(self.midia)
        self.reprodutorInstance.play()

        time.sleep(0.5)
        self.audios = self.reprodutorInstance.audio_get_track_description()
        self.legendas = self.reprodutorInstance.video_get_spu_description()

        self.comboMusica.clear()
        self.comboLegenda.clear()

        audio =[list(Tuple) for Tuple in self.audios]
        
        legendas =[list(Tuple) for Tuple in self.legendas]

        for faixas_audio in audio:
            self.comboMusica.addItem(faixas_audio[1].decode('UTF-8'))
        
        for faixas_legenda in legendas:
            self.comboLegenda.addItem(faixas_legenda[1].decode('UTF-8'))


        self.comboMusica.setCurrentIndex(1)
        self.comboLegenda.setCurrentIndex(1)
        '''
        #segundo reprodutor
        self.reprodutorInstance2.set_media(self.midia)
        self.reprodutorInstance2.play()
        '''

    def play(self):
        if self.reprodutorInstance.is_playing():
            self.reprodutorInstance.pause()
            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap("icones/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.botaoPlay.setIcon(icon1)
        else:
            self.reprodutorInstance.play()
    
    def reproduzindo(self,event):
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icones/pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botaoPlay.setIcon(icon1)

    def stop(self):
        self.reprodutorInstance.stop()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icones/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botaoPlay.setIcon(icon1)
        self.slideMusica.setValue(0)

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

    def fimdaReproducao(self,event):
        self.slideMusica.setValue(0)
    
    def mudarFaixaDeAudio(self,arg):
        if arg == 0:
            self.reprodutorInstance.audio_set_track(-1) # é usado -1 porque o vlc usa esse indice para desabilitar o audio

        else:
            self.reprodutorInstance.audio_set_track(arg)