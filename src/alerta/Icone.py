#-*-coding: UTF -8-*-
from alerta.Menu import Menu
import gtk
import sys
import os

__author__="Rômulo de Barros Correia Jales"
__date__ ="$30/07/2010 13:58:14$"

class Icone(gtk.StatusIcon):

    def __init__(self,icone,programa,parametros,arquivoInibidor,autoInibir):
        gtk.StatusIcon.__init__(self)
        self.set_visible(True)
        self.set_from_file(icone)
        self.autoInibir = autoInibir
        self.arquivoInibidor  = arquivoInibidor
        __menu = Menu(programa,self.arquivoInibidor)
        self.__executeId = self.connect("activate",self.executarPrograma,programa,parametros)
        self.__menuId = self.connect("popup-menu",__menu.exibir)
        
    def executarPrograma(self,icon,programa,parametros):
        args = []
        args.append(programa)
        if parametros is not None:
            lista = parametros.split()
            for i in lista:
                args.append(i)
        try:
            if self.autoInibir:
                 open(os.path.expanduser("~/.megalinux/%s"%self.arquivoInibidor),"w").close()
            os.execvp(programa,args)
            sys.exit(0)
        except Exception,e:
            print e
