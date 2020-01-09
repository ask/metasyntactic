# -*- coding: utf-8 -*-
'''

##########################
Acme::MetaSyntactic::muses
##########################

****
NAME
****


Acme::MetaSyntactic::muses - Greek Muses


***********
DESCRIPTION
***********


The nine muses from Greek mythology.


************
CONTRIBUTORS
************


Abigail, Philippe Bruhat (BooK)


*******
CHANGES
*******



- \*
 
 2012-05-21 - v1.001
 
 Made multilingual. Added translations for \ *de*\ , \ *en*\ , \ *eo*\ , \ *es*\ ,
 \ *fr*\ , \ *it*\ , \ *la*\  (the default), \ *nl*\ , \ *pl*\ , \ *pt*\ .
 
 Published in Acme-MetaSyntactic-Themes version 1.002.
 


- \*
 
 2012-05-14 - v1.000
 
 Introduced in Acme-MetaSyntactic-Themes version 1.001.
 


- \*
 
 2005-10-24
 
 Submitted by Abigail.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'muses'
DATA = '''\
# default
la
# names de
Kalliope Klio Erato Euterpe Melpomene Polyhymnia Terpsichore Thalia  Urania
# names en
Calliope Clio Erato Euterpe Melpomene Polyhymnia Terpsichore Thalia  Urania
# names eo
Kaliopo  Klio Erato Euterpo Melpomeno Polimnio   Terpsihoro  Talio   Uranio
# names es
Caliope  Clio Erato Euterpe Melpomene Polimnia   Terpsicore  Talia   Urania
# names fr
Calliope Clio Erato Euterpe Melpomene Polymnie   Terpsichore Thalie  Uranie
# names it
Calliope Clio Erato Euterpe Melpomene Polimnia   Tersicore   Talia   Urania
# names la
Calliope Clio Erato Euterpe Melpomene Polyhymnia Terpsichore Thalia  Urania
# names nl
Kalliope Clio Erato Euterpe Melpomene Polyhymnia Terpsichore Thaleia Urania
# names pl
Kalliope Klio Erato Euterpe Melpomene Polihymnia Terpsychora Talia   Urania
# names pt
Caliope  Clio Erato Euterpe Melpomene Polimnia   Terpsicore  Talia   Urania\
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


