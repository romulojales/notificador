#-*-coding: UTF -8-*-
from alerta.Alerta import Alerta
from alerta.Alerta import alertar
import os.path
import libxml2

__author__="Rômulo de Barros Correia Jales"
__date__ ="$03/12/2008 17:05:35$"

def consumirXml(arq,autoInibir):
    if os.path.isfile(arq):
        alerta = Alerta()
        try:
            obj = open(arq,'r')
        except Exception,e:
            print "Erro ao abrir o notificador:\n%s"%e

        doc = obj.read()
        obj.close()
        xml = libxml2.parseDoc(doc)

        raiz = xml.children
       
        if (raiz.prop("type") !=  "notificador"):
            raise Exception("Este arquivo não contém as configurações de uma notificação")
        else:
            elementos = raiz.children
            elementos =  elementos.next
            while( elementos is not None):
                if  elementos.name == "programa":
                    alerta.programa =elementos.content
                elif elementos.name == "parametros":
                    alerta.parametros =elementos.content
                elif elementos.name == "icone":
                    alerta.icone = elementos.content
                elif elementos.name == "titulo":
                     alerta.titulo = elementos.content
                elif elementos.name =="mensagem":
                    alerta.mensagem = elementos.content
                elif elementos.name == "arquivoInibidor":
                    if elementos.content is "":
                        raise Exception("O nome do arquivo inibidor não pode está vazio")
                    elif " " in elementos.content:
                        raise Exception("O nome do arquivo inibidor não pode conter espaços")
                    else:
                        alerta.arquivoInibidor = elementos.content

                elif elementos.name == "tempoEspera":
                    alerta.tempoEspera = int(elementos.content)
                elif elementos.name == "tempoExibicao":
                    alerta.tempoExibicao = int(elementos.content)
                    
                elementos =  elementos.next
                
            alertar(alerta,autoInibir)