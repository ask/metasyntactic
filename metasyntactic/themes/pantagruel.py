# -*- coding: utf-8 -*-
'''

###############################
Acme::MetaSyntactic::pantagruel
###############################

****
NAME
****


Acme::MetaSyntactic::pantagruel - The Pantagruel theme


***********
DESCRIPTION
***********


Pantagruel's genealogy.

List taken from \ *Pantagruel*\ , chapter 2, by Maistre Franoys Rabelais.


***********
CONTRIBUTOR
***********


Rafael Garcia-Suarez


*******
CHANGES
*******



- \*
 
 2012-05-14 - v1.001
 
 Updated with an \ ``=encoding``\  pod command in version 1.001.
 


- \*
 
 2012-05-07 - v1.000
 
 Received its own version number in Acme-MetaSyntactic-Themes version 1.000.
 


- \*
 
 2006-05-01
 
 Introduced in Acme-MetaSyntactic version 0.72.
 


- \*
 
 2006-03-23
 
 Initial list proposed by Rafal Garcia-Suarez.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'pantagruel'
DATA = '''\
# names
Chalbroth
Sarabroth
Faribroth
Hurtaly
Nembroth
Athlas
Goliath
Eryx
Titius
Eryon
Polyphemus
Cacus
Etion
Enceladus
Ceus
Typhoeus
Aloeus
Othus
Aegeon
Briareus
Porphyrio
Adamastor
Anteus
Agatho
Porus
Aranthas
Gabbara
Goliath_de_Secundille
Offot
Artachees
Oromedon
Gemmagog
Sisyphus
Hercules
Enay
Fierabras
Morguan
Fracassus
Ferragus
Happemousche
Bolivorax
Longys
Gayoffe
Maschefain
Brulefer
Engoulevent
Galehaut
Myrelangault
Galaffre
Falourdin
Roboastre
Sortibrant_de_Conimbres
Brushant_de_Mommiere
Bruyer
Mabrun
Foutasnon
Hacquelebac
Vitdegrain
Grantgousier
Gargantua
Pantagruel\
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


