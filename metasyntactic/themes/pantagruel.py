# -*- coding: utf-8 -*-
'''
.. highlight:: perl


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

List taken from \ *Pantagruel*\ , chapter 2, by Maistre Françoys Rabelais.


***********
CONTRIBUTOR
***********


Rafael Garcia-Suarez

Introduced in version 0.72, published on May 1, 2006.


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
data = parse_data(DATA)


def default():
    try:
        if 'default' in data:
            return data['default'][0]
    except KeyError, IndexError:
        pass
    return 'en'


def all():
    acc = set()
    for category, names in data['names'].iteritems():
        if names:
            acc |= names
    return acc


def names(category=None):
    if not category:
        category = default()
    if category == ':all':
        return list(all())
    return list(data['names'][category])


def random(n=1, category=None):
    got = names(category)
    if got:
        shuffle(got)
        if n == 1:
            return choice(got)
        return got[:n]

def sections():
    return set(data['names'].keys())


