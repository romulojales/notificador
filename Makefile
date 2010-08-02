SHELL = /bin/bash

DESTDIR = 

BINDIR = $(DESTDIR)/usr/bin
SHAREDIR = $(DESTDIR)/usr/share
LOCALEDIR = $(DESTDIR)/usr/share/locale
VERSION = 1.0
PROGNAME = notificador

all: 
	make -C po

clean:
	find . -name "*.pyc" -delete
	make -C po clean

install:
	mkdir -p $(SHAREDIR)/$(PROGNAME)/$(VERSION)
	mkdir -p $(LOCALEDIR)/pt_BR/LC_MESSAGES
	cp -a src/notificador.py $(BINDIR)/notificador
	chmod  a+x $(BINDIR)/notificador
	cp -a src/alerta $(SHAREDIR)/$(PROGNAME)/$(VERSION)
	cp -a src/utils $(SHARED2IR)/$(PROGNAME)/$(VERSION)
	cp -a src/xmlNotificador $(SHAREDIR)/$(PROGNAME)/$(VERSION)
	cp -a po/notificador.mo $(LOCALEDIR)/pt_BR/LC_MESSAGES
	

uninstall:
	rm -rf /usr/share/$(PROGNAME)
	rm $(LOCALEDIR)/pt_BR/LC_MESSAGES/notificador.mo
	rm $(BINDIR)/notificador
