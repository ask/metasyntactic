# -*- coding: utf-8 -*-
'''
.. highlight:: perl


##########################
Acme::MetaSyntactic::chess
##########################

****
NAME
****


Acme::MetaSyntactic::chess - The chess pieces theme


***********
DESCRIPTION
***********


The six Chess pieces, in various languages.


***********
CONTRIBUTOR
***********


Abigail.

Introduced in version 0.59, published on January 30, 2006.


********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'chess'
DATA = '''\
# default
en
# names en
king      queen     bishop    knight    rook      pawn
# names nl
koning    dame      loper     paard     toren     pion
# names de
Konig     Dame      Laufer    Springer  Turm      Bauer
# names fr
roi       dame      fou       cavalier  tour      pion
# names eo
rego      damo      kuriero   cevalo    turo      peono
# names la
rex       regina    alfinus   eques     rochus    pedes\
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


