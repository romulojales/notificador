#-*-coding: UTF -8-*-
import pynotify
import gobject

__author__="Rômulo de Barros Correia Jales"
__date__ ="$03/12/2008 14:36:49$"

class Notificador:
    def __init__(self,tempoEspera,tempoExibicao,titulo,mensagem,icone):
        """Tempos em segundos"""
        pynotify.init(titulo)
        self.__note = pynotify.Notification(titulo, mensagem,"dialog-warning")
        self.__note.attach_to_status_icon(icone)
        if tempoExibicao <= 1:
            tempoExibicao = 5
        gobject.timeout_add(tempoExibicao*1000,self.notificar,tempoEspera)
        
    def notificar(self,tempoEspera):
        self.__note.set_timeout(tempoEspera*1000)
        self.__note.show()
