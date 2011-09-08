# -*- coding: utf-8 -*-
'''
.. highlight:: perl


##############################
Acme::MetaSyntactic::invasions
##############################

****
NAME
****


Acme::MetaSyntactic::invasions - The naval and airborne invasions theme


***********
DESCRIPTION
***********


This list gives some codenames for naval invasions, paradrops and
operations with both a naval invasion component and an airborne
component during World War II. The list includes some operations which
were planned but not executed.

Source: among others, the \ *Codeword Dictionnary*\ , 
Paul Adkins, Motorbooks International
(ISBN 0-7603-00368-1).


***********
CONTRIBUTOR
***********


Jean Forget

Introduced in version 0.92, published on September 18, 2006
(the 62nd anniversary of Market-Garden).


********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'invasions'
DATA = '''\
# names
Al Anvil Avalanche Baytown Coronet Detachment Dragoon Eclipse
Flintlock Gruener_Pfeil Herkules Husky Iceberg Ikarus Jubilee Leopard
Market_Garden Menace Merkur Mi Mo Oboe Olympic Overlord Roundhammer
Roundup Seeloewe Shingle Shoestring Slapstick Sledgehammer Torch
Varsity Victor Watchtower\
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


