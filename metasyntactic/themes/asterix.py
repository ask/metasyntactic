# -*- coding: utf-8 -*-
'''

############################
Acme::MetaSyntactic::asterix
############################

****
NAME
****


Acme::MetaSyntactic::asterix - Asterix the Gaul


***********
DESCRIPTION
***********


Characters from the famous French cartoon, created by Goscinny and Uderzo.

Languages
=========


Supported languages:
\ *en*\ , \ *en_us*\ , \ *fr*\ , \ *nl*\ , \ *de*\ , \ *es*\ , \ *gl*\ , \ *hu*\ , \ *la*\ , \ *pt*\ , \ *sv*\ .

Reference sites:
`http://en.wikipedia.org/wiki/Asterix <http://en.wikipedia.org/wiki/Asterix>`_,
`http://asterix.openscroll.org/characters.html <http://asterix.openscroll.org/characters.html>`_.



***********
CONTRIBUTOR
***********


Abigail


*******
CHANGES
*******



- \*
 
 2012-10-01 - v1.000
 
 Published in Acme-MetaSyntactic-Themes version 1.021.
 


- \*
 
 2005-10-25
 
 Submitted by Abigail, with the names translated in 11 languages.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::Locale <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aLocale&mode=module>`_.
'''

name = 'asterix'
DATA = '''\
# default
fr
# names en
Asterix
Obelix
Dogmatix
Getafix
Vitalstatistix
Impedimenta
Cacofonix
Fulliautomatix
Unhygienix
Bacteria
Geriatrix

Julius_Caesar
Cleopatra
Brutus
Postaldistrix
Picanmix
Redbeard
Pegleg
Boy
Panacea
Ekonomikrisis
Tragicomix
Tremendelirius
Drinklikafix
# names en_us
Asterix
Obelix
Dogmatix
Magigimmix
Arthritix Macroeconomix
Belladonna
Malacoustix
Fulliautomatix
Epidemix
Bacteria
Geriatrix

Julius_Caesar
Cleopatra
Brutus
Postaldistrix
Picanmix
Redbeard
Pegleg
Boy
Panacea
Ekonomikrisis
Tragicomix
Tremendelirius
Drinklikafix
# names fr
Asterix
Obelix
Idefix
Panoramix
Abraracourcix
Bonemine
Assurancetourix
Cetautomatix
Ordralfabetix
Ielosubmarine
Agecanonix

Jules_Cesar
Cleopatre
Brutus
Pneumatix
Keskonrix
Barbe_Rouge

Baba
Falbala
Epidemais


Zaza
Aplusbegalix
Amerix
Caius_Bonus
# names nl
Asterix
Obelix
Idefix
Panoramix
Abraracourcix Heroix

Assurancetourix Kakofonix
# names de
Alkoholix
Asterix
Astronomix
Automatix
Claudius_Bockschus
Costa_Y_Bravo
Brutus
Julius_Casar
Tullius_Destruktivus
Eleonoradus
Falbala
Gelatine
Grautvornix
Gutemine
Homoopatix
Acidix_Hydrochloridix
Idefix
Jellosubmarine
Kantine
Lucius_Keuchhustus
Kleopatra
Majestix
Olaf_Maulaf
Methusalix
Miraculix
Moralelastix
Nixalsverdrus Hotelterminus
Numerobis
Obelix
Orthopadix
Osolemirnix
Ozeanix
Praline
Processus
Feistus_Raclettus
Gaius_Raffcus
Rohrpostix
Salamix
Studicus
Taubenus
Technokratus
Teefax
Tragicomix
Troubadix
Vaseline
Verleihnix
Agrippus_Virus
Vreneli
Volligbaf
Zechine
# names es
Asterix
Obelix
Panoramix
Asuranceturix
Abraracurcix
Karabella
Ordenalfabetix
Esautomatix
Edadepiedrix
Idefix Ideafix
Julio_Cesar
Cleopatra
# names gl
Asterix
Obelix
Panoramix
Abraracurcix Abrazopartidix
Karabella
Asuracenturix Seguroatodoriesguix
Ideafix Idefix
# names hu
Asterix
Obelix
Mirnixdirnix
Magicoturmix
Hasarengazfix
Hangianix
Messesaglix
Sokadikix
# names la
Asterix
Obelix
Idefix
Miraculix
Maiestix
Troubadix
# names pt
Asterix
Obelix
Chatotorix
Abracurcix
Ideiafix
Panoramix
# names sv
Asterix
Obelix
Idefix
Miraculix
Troubadix
Majestix
Senilix
Smidefix
Crabbofix
Bonemine
Fru_Crabbofix
Julius_Caesar\
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


