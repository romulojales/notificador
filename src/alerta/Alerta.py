#-*-coding: UTF -8-*-
import sys
from Icone import Icone
from Notificador import Notificador
import os.path

__author__="Rômulo de Barros Correia Jales"
__date__ ="$30/07/2010 13:58:14$"

class Alerta:
    def __init__(self,icone=None, programa=None,parametros=None,tempoEspera=2,tempoExibicao=20,titulo="Notificador",mensagem=None,arquivoInibidor=None):
        self.icone = icone
        self.programa = programa
        self.parametros = parametros
        self.tempoEspera = tempoEspera
        self.tempoExibicao = tempoExibicao
        self.titulo = titulo
        self.mensagem = mensagem
        self.arquivoInibidor = arquivoInibidor

def alertar(alerta,autoInibir):
    if os.path.isfile(os.path.expanduser("~/.megalinux/%s"%alerta.arquivoInibidor)):
        print "Alerta inibido"
        sys.exit(0)
    else:
        if os.path.isfile(alerta.icone) and (alerta.icone is not None):
            if os.path.isfile(alerta.programa) and (alerta.programa is not None):
                if (alerta.tempoEspera  is not None) and (alerta.tempoExibicao is not None):
                    icone = Icone(icone=alerta.icone,programa=alerta.programa,parametros=alerta.parametros,arquivoInibidor=alerta.arquivoInibidor,autoInibir=autoInibir)
                    Notificador(tempoEspera=alerta.tempoEspera,tempoExibicao=alerta.tempoExibicao,titulo=alerta.titulo,mensagem=alerta.mensagem,icone=icone)
            else:
                raise Exception("Programa \"%s\" não encontrado."%alerta.programa)
        else:
            raise Exception("Arquivo de ícone \"%s\" não encontrado."%alerta.icone)
