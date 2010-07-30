#-*-coding: UTF -8-*-
import libxml2
import re
import os.path

__author__="Rômulo de Barros Correia Jales"
__date__ ="$03/12/2008 17:05:25$"

class ProdutorXml:
    def __init__(self,opcoes=None):
        if opcoes is not None:
            self.__setNomeXml(opcoes.xml)
            self.__setPrograma(opcoes.programa)
            self.__setParametros(opcoes.para)
            self.__setIcone(opcoes.icone)
            self.__setTitulo(opcoes.titulo)
            self.__setMensagem(opcoes.mensagem)
            self.__setInibidor(opcoes.inibidor)
            self.__setEspera(opcoes.espera)
            self.__setExibicao(opcoes.exibicao)
        else:
            self.__setNomeXml()
            self.__setPrograma()
            self.__setParametros()
            self.__setIcone()
            self.__setTitulo()
            self.__setMensagem()
            self.__setInibidor()
            self.__setEspera()
            self.__setExibicao()
            
        self.__criarXml()

    def __setNomeXml(self,nome=None):
        self.nomeXml = nome
        if self.nomeXml is None:
            self.nomeXml = raw_input("\nDigite o nome do arquivo para gravar os dados: ")
            valido = False
            while  not valido:
                if (os.path.isfile(self.nomeXml)):
                    print "\nEste nome de arquivo já existe."
                    self.nomeXml = raw_input("Digite o nome do arquivo para gravar os dados: ")
                elif len(self.nomeXml) is 0:
                    print "\nVocê precisa digitar o nome do arquivo."
                    self.nomeXml = raw_input("Digite o nome do arquivo para gravar os dados: ")
                elif " " in self.nomeXml:
                    print "\nO nome do arquivo não pode conter espaços."
                    self.nomeXml = raw_input("Digite o nome do arquivo para gravar os dados: ")
                else:
                    valido = True

    def __setPrograma(self,programa=None):
        self.programa=programa
        if self.programa is None:
            self.programa = raw_input("\nDigite o caminho absoluto do programa que será acionado pelo notificador: ")
            valido = False
            while not valido:
                if len( self.programa ) is 0:
                    print "\nVocê precisa digitar o nome do programa."
                    self.programa = raw_input("Digite o caminho absoluto do programa do contexto da notificação: ")
                elif " " in self.programa:
                    print "\nNão pode conter espaços no programa"
                    self.programa = raw_input("Digite o caminho absoluto do programa do contexto da notificação: ")
                else:
                    valido = True

    def __setParametros(self,parametros=None):
        self.parametros=parametros
        if self.parametros is None:
            self.parametros = raw_input("\nDigite o parametros, caso necessário, do programa: ")

    def __setIcone(self,icone=None):
        self.icone = icone
        if self.icone is None:
            self.icone = raw_input("\nDigite o caminho absoluto para o ícone a ser exibido no alerta: ")
            valido = False
            while not valido:
                if len(self.icone) is 0:
                    print "\nVocê precisa especificar o arquivo do icone"
                    self.icone = raw_input("Digite o caminho absoluto para o ícone a ser exibido no alerta: ")
                elif " " in self.icone:
                    print "\nNão pode conter espaços no nome do ícone"
                    self.icone = raw_input("Digite o caminho absoluto para o ícone a ser exibido no alerta: ")
                else:
                    valido = True

    def __setTitulo(self,titulo=None):
        self.titulo = titulo
        if self.titulo is None:
            self.titulo = raw_input("\nDigite o título do alerta: ")

    def __setMensagem(self,mensagem=None):
        self.mensagem =mensagem
        if self.mensagem is None:
            self.mensagem = raw_input("\nDigite a mensagem de exibição do alerta: ")
            while len(self.mensagem) is 0:
                print "\nVocê precisa digitar uma mensagem"
                self.mensagem = raw_input("Digite a mensagem de exibição do alerta: ")

    def __setInibidor(self,inibidor=None):
        self.inibidor = inibidor
        if self.inibidor is None:
            self.inibidor =raw_input("\nDigite o nome do arquivo inibidor do alerta: ")
            valido = False
            while not valido:
                if len(self.inibidor) is 0:
                    print "\nVocê precisa digitar o nome do arquivo inibidor!"
                    self.inibidor =raw_input("Digite o nome do arquivo inibidor do alerta: ")
                elif " " in self.inibidor:
                    print "\nNão pode conter espaço no nome do arquivo inibidor!"
                    self.inibidor =raw_input("Digite o nome do arquivo inbidor do alerta: ")
                else:
                    valido = True
    def __setEspera(self,espera=None):
        self.espera = espera
        if self.espera is None:
            self.espera = raw_input("\nDigite o tempo em segundos de espera para exibir o alerta após o login. [10]: ")
            valido = False
            while not valido:
                if len(self.espera) is 0:
                    self.espera = str(10)
                    valido = True
                elif len(re.findall("[a-z]| ",self.espera,re.I))>0:
                    print "\nO tempo de espera só pode conter números"
                    self.espera = raw_input("Digite o tempo em segundos de espera para exibir o alerta após o login. [10]: ")
                else:
                    valido = True
    def __setExibicao(self,exibicao):
        self.exibicao = exibicao
        if self.exibicao is None:
                self.exibicao = raw_input("\nDigite o tempo em segundo do qual a mensagem será exibida. [20]: ")
                valido = False
                while not valido:
                    if len(self.exibicao) is 0:
                        self.exibicao = str(20)
                        valido = True
                    elif len(re.findall("[a-z]| ",self.exibicao,re.I))>0:
                        print "\nO tempo de espera só pode conter números"
                        self.exibicao = raw_input("Digite o tempo em segundo do qual a mensagem será exibida. [20]: ")
                    else:
                        valido = True
                        
    def __criarXml(self):
               #Criar o xml
                doc = libxml2.newDoc("1.0")
                dominio = doc.newChild(None,"domain",None)
                dominio.newProp("type","notificador")
                programa = dominio.newChild(None,"programa",None)
                programa.addChild(doc.newDocText(self.programa))
                parametros = dominio.newChild(None,"parametros",None)
                parametros.addChild(doc.newDocText(self.parametros))
                icone = dominio.newChild(None,"icone",None)
                icone.addChild(doc.newDocText(self.icone))
                titulo = dominio.newChild(None,"titulo",None)
                titulo.addChild(doc.newDocText(self.titulo))
                mensagem = dominio.newChild(None,"mensagem",None)
                mensagem.addChild(doc.newDocText(self.mensagem))
                arquivoInibidor = dominio.newChild(None,"arquivoInibidor",None)
                arquivoInibidor.addChild(doc.newDocText(self.inibidor))
                tempoEspera = dominio.newChild(None,"tempoEspera",None)
                tempoEspera.addChild(doc.newDocText(self.espera))
                tempoExibicao = dominio.newChild(None,"tempoExibicao",None)
                tempoExibicao.addChild(doc.newDocText(self.exibicao))
                
                #Salva o xml no arquivo
                arquivo = open(self.nomeXml,"w")
                arquivo.write(doc.serialize(None, 1))
                arquivo.close()

                print "Arquivo gerado com sucesso!"
