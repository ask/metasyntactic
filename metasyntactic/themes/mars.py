# -*- coding: utf-8 -*-
'''

#########################
Acme::MetaSyntactic::mars
#########################

****
NAME
****


Acme::MetaSyntactic::mars - The mars theme


***********
DESCRIPTION
***********


This theme provides the list of the names of planet Mars,
as they appear in Kim Stanley Robinson's \ *Mars*\  trigoly.


***********
CONTRIBUTOR
***********


Laurent Gautrot.


*******
CHANGES
*******



- \*
 
 2012-07-31 - v1.000
 
 Introduced in Acme-MetaSyntactic-Themes version 1.012
 (published one day late).
 


- \*
 
 2006-05-31
 
 List proposed by Laurent Gautrot.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'mars'
DATA = '''\
# names
Al_Qahira
Ares
Auqakuh
Bahram
Harmakhis
Hrad
Huo_Hsing
Kasei
Ma_adim
Maja
Mamers
Mangala
Mars
Mawrth
Nirgal
Shalbatanu
Simud
Tiu\
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


