#!/usr/bin/python
#-*-coding: UTF-8 -*-
# license: GPLv2
import sys
import gtk
import os.path
import gettext

__author__ = "Rômulo de Barros Correia Jales"
__date__    ="$03/12/2008 13:58:14$"

libDir = "/usr/share/notificador/1.1/"

if not libDir in sys.path:
	sys.path.append(libDir)

gettext.bindtextdomain('notificador','/usr/share/locale')
gettext.textdomain('notificador')

def main():
    from utils.opcoes import OptionParser
    from utils.opcoes import OptionGroup
    from xmlNotificador.Consumidor import consumirXml
    from xmlNotificador.Produtor import ProdutorXml
    
    parser = OptionParser(usage="%prog [-a <arquivo>|-ma <arquivo>|-c [opções]|-h]",version="%prog 1.0.0",prog="notificador")

    parser.add_option("-a","--arquivo",metavar="ARQUIVO",dest="arquivo",help="Escreva o caminho do arquivo para notificar")
    parser.add_option("-m","--auto-inibicao",action="store_true",dest="autoInibicao",help="Passe este parametro para inibir o alerta assim que o usuário clicar no ícone.")
    parser.add_option("-c","--criar-xml",action="store_true",dest="criarXml",help="Cria um xml para uma nova notificação.")
    
    grupoCriar = OptionGroup(parser,"Opções de -c","Use estas opções junto com a flag -c para criar XML usando a interface captativa")
    grupoCriar.add_option("-n","--arquivo-xml",metavar="ARQUIVO",dest="xml",help="O nome do arquivo para gravar o xml.")
    grupoCriar.add_option("-p","--programa",metavar="PROGRAMA",dest="programa",help="O programa a ser executado.")
    grupoCriar.add_option("--para",metavar="PARAMETROS",dest="para",help="O parametros do programa.")
    grupoCriar.add_option("-i","--icone",metavar="ARQUIVO",dest="icone",help="O ícone a ser exibido.")
    grupoCriar.add_option("-t","--titulo",metavar="TITULO",dest="titulo",help="O titulo do alerta.")
    grupoCriar.add_option("-g","--mensagem",metavar="MENSAGEM",dest="mensagem",help="Digite a mensagem do alerta, entre aspas a fim de aceitar mais de uma palavra")
    grupoCriar.add_option("-b","--arquivo-inibidor",metavar="ARQUIVO",dest="inibidor",help="O arquivo inibidor do alerta.")
    grupoCriar.add_option("-s","--tempo-espera",metavar="TEMPO",dest="espera",help="O tempo de espera para exibir o alerta.")
    grupoCriar.add_option("-e","--tempo-exibicao",metavar="TEMPO",dest="exibicao",help="O tempo de exibição da mensagem de alerta.")

    parser.add_option_group(grupoCriar)

    (options,args) = parser.parse_args()
    
    if options.criarXml:
        ProdutorXml(options)
    elif options.arquivo:
        if os.path.isfile(options.arquivo):
            consumirXml(options.arquivo,options.autoInibicao)
            gtk.main()
        else:
            parser.error("Não foi possível encontrar o arquivo: \"%s\". Tente passar o caminho absoluto ou relativo do mesmo"%options.arquivo)
    else:
        print parser.get_usage()
        
if __name__ == "__main__":
	try:
		if(not os.path.exists(os.path.expanduser("~/.megalinux"))):
			os.mkdir(os.path.expanduser("~/.megalinux"))
		main()
		sys.exit(0)
	except Exception,e:
		print "Erro não esperado:\n%s"%e
		sys.exit(1)
