# -*- coding: utf-8 -*-
'''
.. highlight:: perl


############################
Acme::MetaSyntactic::pynchon
############################

****
NAME
****


Acme::MetaSyntactic::pynchon - The Pynchon theme


***********
DESCRIPTION
***********


Character names from Thomas Pynchon's books.

David Landgren not only named all the machines in the \ ``mongueurs.net``\ 
domain (\ ``stencil``\ , \ ``sferics``\  and \ ``profane``\ ) after characters from
Thomas Pynchon's books, but also provided a first list.

The pynchon list will probably grow in future versions, as David goes
through his books.


***********
CONTRIBUTOR
***********


David Landgren.

Introduced in version 0.03, published on January 14, 2005.

Updated by David Landgren in version 0.41, published on September 26, 2005.


********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'pynchon'
DATA = '''\
# names
porpentine slothrop stencil profane godolphin yoyodyne waste
sferics oedipa mondaugen eigenvalue schlozhauer schoenmaker
bongo_shaftsbury maijstral achtfaden sachsa mantissa angevine
anthroresearch apocheir aquilina barkhausen basilisco bergomask beukes
bodine boeblich bondelschwaartz borracho carruthers_pillow chiclitz chobb
contango covess delgado dnubietna dupiro echerze eckstine fairing falange
fauchard fazzo fenice flake fleische foppl gadrulfi gascoigne gebrail
gerfaut geronimo girgis gland gonzi goodfellow gottschalk groomsman
halidom katz khevenhuller_metsch kholsky knoop lazar lepsius leutwein
lowenstein manganese mannaro\
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


