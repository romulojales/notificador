#-*-coding: UTF -8-*-
import gtk

fechar = gtk.RESPONSE_CLOSE
ok     = gtk.RESPONSE_OK
cancel = gtk.RESPONSE_CANCEL
sim    = gtk.RESPONSE_YES
nao    = gtk.RESPONSE_NO

__author__="Rômulo de Barros Correia Jales"
__date__ ="$30/07/2010 13:58:14$"


class Erro(gtk.MessageDialog):
	
    def __init__(self,msg,titulo):
        gtk.MessageDialog.__init__(self,None,gtk.DIALOG_MODAL,gtk.MESSAGE_ERROR,gtk.BUTTONS_CLOSE,titulo)
        #self.set_properties("skip-taskbar-hint",True)
        self.format_secondary_text(msg)
        self.set_icon_name("error")
        self.run()
        self.destroy()
        
class Aviso(gtk.MessageDialog):
	
	def __init__(self,msg,titulo):
		gtk.MessageDialog.__init__(self,None,gtk.DIALOG_MODAL,gtk.MESSAGE_WARNING,gtk.BUTTONS_OK_CANCEL,titulo)
		self.set_icon_name("warning")
		self.format_secondary_text(msg)
    
class Info(gtk.MessageDialog):
	def __init__(self,msg,titulo):
		gtk.MessageDialog.__init__(self,None,gtk.DIALOG_MODAL,gtk.MESSAGE_INFO,gtk.BUTTONS_OK,titulo)
		self.set_icon_name("info")
		self.format_secondary_text(msg)
		self.set_icon_name("info")
		self.run()
		self.destroy()
		
class Questao(gtk.MessageDialog):
		
	def __init__(self,msg,titulo):
		gtk.MessageDialog.__init__(self,None,gtk.DIALOG_MODAL,gtk.MESSAGE_QUESTION,	gtk.BUTTONS_YES_NO,titulo)
		self.set_icon_name("question")
		self.format_secondary_text(msg)
	
