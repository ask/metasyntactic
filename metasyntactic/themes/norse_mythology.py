# -*- coding: utf-8 -*-
'''

####################################
Acme::MetaSyntactic::norse_mythology
####################################

****
NAME
****


Acme::MetaSyntactic::norse_mythology - Characters from Norse mythology


***********
DESCRIPTION
***********


A selection of characters from Norse mythology.


*******
SOURCES
*******


Among others:


- \*
 
 \ *La Saga de Gunnld*\ ,
 written by Svava Jakobsdottir,
 translated into French and annotated by Rgis Boyer
 and published by Jos Corti
 (ISBN 2-7143-0801-5).
 


- \*
 
 \ *The Viking Gods*\  (excerpts from the prose Edda)
 written by Snorri Sturluson,
 translated into English by Jean Young,
 edited by Jon Thorisson,
 published by Gudrun
 (ISBN 9979-856-78-5).
 



************
CONTRIBUTORS
************


Abigail, Jean Forget.


*******
CHANGES
*******



- \*
 
 2012-05-14 - v1.001
 
 Updated with an \ ``=encoding``\  pod command
 in Acme-MetaSyntactic-Themes version 1.001.
 


- \*
 
 2012-05-07 - v1.000
 
 Received its own version number in Acme-MetaSyntactic-Themes version 1.000.
 


- \*
 
 2006-06-26
 
 Updated by Jean Forget in Acme-MetaSyntactic version 0.80.
 
 Jean provided his bibliographic references.
 


- \*
 
 2006-05-22
 
 Introduced in Acme-MetaSyntactic version 0.75, with categories
 \ *dwarves*\ , \ *giants*\ , \ *gods*\ , \ *valkyries*\ , \ *worlds*\ .
 


- \*
 
 2005-11-03
 
 Abigail submitted five more lists for `Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_,
 all sharing a common element: Norse Mythology.
 
 The lists were Gods, Giants, Dwarves, Valkyries and Worlds.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::MultiList <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aMultiList&mode=module>`_.
'''

name = 'norse_mythology'
DATA = '''\
# default
gods
# names dwarves
Ai Alf Althjof An Andvari Aurvang Austri Bifur Bofur Bombur Brokk Dain
Dolgthrasir Dori Draupnir Duf Durin Dvalin Eikinskjaldi Eitri Fili Fith Fjalar
Frar Frosti Fraeg Fundin Galarr Gandalf Ginnar Gloin Hannar Haugspori Heptifili
Hlevang Hor Hornbori Ivaldi Jari Kili Lit Lofar Loni Mjothvitnir Motsognir
Nain Nali Nar Niping Nithi Nori Northri Nyi Nyr Nyrath Onar Ori Rathvith
Regin Skafith Skirfir Suthri Suttung Sviur Thekk Thorin Thrain Thror Vestri Vigg
Vindalf Virfir Vit Yngvi
# names giants
AEgir Baugi Bergelmir Bestla Bolthorn Farbauti Geirrod Gerd Gilling Gjalp Greip
Gunnlod Gymir Hrod Hrungnir Hymir Ivaldi Jarnsaxa Kari Narve Loki Mimir
Olvaldi Saxa Skadi Surtur Suttung Thiazi Thrudgelmir Thrym Utgardaloki
Vafthrudnir Ymir
# names gods
AEgir Andhrimnir Aurvandil Balder Borr Bragi Buri Dagr Delling Eir
Elli Fjorgvin Forseti Freyja Freyr Frigg Fulla Gefjun Hel Heimdall Hermodr
Hlin Hodr Hoenir Huldra Idunn Jord Kvasir Laga Lofn Loki Magni
Mani Miming Mimir Modi Nanna Nerthus Njord Nott Od Odin Ottar Ran Rind
Saga Sif Sigyn Sjofn Skadi Snotra Sol Thor Thrud Tyr Ullr Vali Var Ve
Vidar Vili Volundur Vor
# names valkyries
Brynhildr Geirahod Geiravor Geirdriful Geirskogul Geironul Godthjod Gunnlod Gunnr
Gudr Goll Gondul Herfjotur Herja Hildr Hjalmthrimul Hjorthrimul Hlokk Hrist
Hrund Mist Randgnid Randgridr Reginleif Radgridr Sanngridr Sigrdrifa
Sigrun Skalmold Skeggold Skuld Skogul Sveid Svipul Svava THrima THrudr THogn
# names humans
Embla Kvasir
# names norns
Urdur Verdandi Skuld
# names worlds
Alfheim Asgard Vanaheim
Jotunheimr Midgardr Nidavellir
Helheim Muspelheim Niflheim
Yggdrasil
# names animals
Audhumla Fenrir Garm Heidrun Hraesvelgur Hrimfaxi Huginn
Midgardsorm Muninn Ratatoskr Saehrimnir Skinfaxi Sleipnir
# names objects
Bodn Draupnir Gjoll Gungnir Hlidskjalf Hringhorni Mjolnir Odrerir Rati
Skidbladnir Sogn
# names places
Bifrost Bilskirnir Breidablik Fensalir Folkvangar Ginnungagap
Gladsheim Glitnir Gnipa Hel Himinbjorg Hnitbjorg Idavoll Nastrand
Noatung Sessrumnir Thrudvangar Thrymheim Valaskjalf Valhalla Vingolf
# names events
Fimbul Ragnarok\
'''

from metasyntactic.base import parse_data
from random import choice, shuffle
from six import iteritems
data = parse_data(DATA)


def default():
    try:
        if 'default' in data:
            return data['default'][0]
    except (KeyError, IndexError):
        pass
    return 'en'


def all():
    acc = set()
    for category, names in iteritems(data['names']):
        if names:
            acc |= names
    return acc


def names(category=None):
    if not category:
        category = default()
    if category == ':all':
        return list(all())
    category = category.replace('/', ' ')
    return list(data['names'][category])


def random(n=1, category=None):
    got = names(category)
    if got:
        shuffle(got)
        if n == 1:
            return choice(got)
        return got[:n]

def categories():
    return set(data['names'])


