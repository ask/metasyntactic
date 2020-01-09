# -*- coding: utf-8 -*-
'''

##########################
Acme::MetaSyntactic::screw
##########################

****
NAME
****


Acme::MetaSyntactic::screw - The screw drives theme


***********
DESCRIPTION
***********


This theme lists different screw drive types.

See `https://en.wikipedia.org/wiki/Screw_drive <https://en.wikipedia.org/wiki/Screw_drive>`_.


***********
CONTRIBUTOR
***********


Abigail


*******
CHANGES
*******



- \*
 
 2012-09-17 - v1.000
 
 Expanded the list thanks to Wikipedia,
 and published in Acme-MetaSyntactic-Themes version 1.019.
 


- \*
 
 2006-05-13
 
 Submitted by Abigail.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'screw_drives'
DATA = '''\
# names
square
hex
pentagon
thumbscrew
slot
cross cross_recess
Phillips
Frearson Reed_and_Prince
French_recess BNAE_NFL22_070
JIS_B_1012
Mortorq
Pozidriv
Supadriv
Robertson Scrulox
hex_socket Allen
hexalobular_socket Torx star_drive
TTAP
Phillips_square Quadrex Deck_Mate
breakaway_head
Bristol
clutch clutch_type_A clutch_type_G
claw
double_hex
line ALR2 ALR3 ALR4 ALR5 ALR6 ALH2 ALH3 ALH4 ALH5 ALH6 ALR3T
one_way
pentalobe
polydrive
spanner snake_eyes
spline
Torq_set
TA
TP3
tri_wing triangular_slotted tri_groove Opsit
Triple_square XZN
protruding_obstacle\
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


