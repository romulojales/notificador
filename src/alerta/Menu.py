#-*-coding: UTF -8-*-
import sys
import os
from utils.Dialogos import sim
from utils.Dialogos import Questao
import gtk

__author__="Rômulo de Barros Correia Jales"
__date__ ="$30/07/2010 13:58:14$"

class Menu(gtk.Menu):
    def __init__(self,programa,arquivoInibidor):
        gtk.Menu.__init__(self)
        sair= gtk.MenuItem()
        hbox = gtk.HBox(True)
        label = gtk.Label("Sair")
        imagem = gtk.Image()
        imagem.set_from_stock(gtk.STOCK_QUIT,4)
        hbox.add(imagem)
        hbox.add(label)
        sair.add(hbox)
        sair.connect("activate",self.__sair,programa,arquivoInibidor)
        self.attach(sair,0,1,0,1)
        self.show_all()

    def __sair(self,item, programa,arquivoInibidor):
        dialogo = Questao("Você deseja fechar este alerta?",os.path.basename(programa))
        check = gtk.CheckButton("Exibir este alerta novamente")
        check.set_active(True)
        dialogo.vbox.add(check)
        check.show()
        resposta =  dialogo.run()
        
        if not check.get_active():
            if not os.path.exists(os.path.expanduser("~/.megalinux")):
                os.mkdir(os.path.expanduser("~/.megalinux"))
            arquivo = open(os.path.expanduser("~/.megalinux/%s"%arquivoInibidor),"w");
            arquivo.close();

        dialogo.destroy()
        if (resposta == sim):
            sys.exit(0)

    def exibir(self,icone,botao,tempo):
        self.popup(None,None,gtk.status_icon_position_menu,botao,tempo,icone)
