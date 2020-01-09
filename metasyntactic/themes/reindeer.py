# -*- coding: utf-8 -*-
'''

#############################
Acme::MetaSyntactic::reindeer
#############################

****
NAME
****


Acme::MetaSyntactic::reindeer - Santa's Reindeer


***********
DESCRIPTION
***********


The names of Santa's Reindeer. Note spelling variations exists, and
the inclusion of Rudolf is doubtful.

See `https://en.wikipedia.org/wiki/Santa_Claus%27s_reindeer <https://en.wikipedia.org/wiki/Santa_Claus%27s_reindeer>`_


***********
CONTRIBUTOR
***********


Abigail


*******
CHANGES
*******



- \*
 
 2012-05-21 - v1.000
 
 Introduced in Acme-MetaSyntactic-Themes version 1.002.
 


- \*
 
 2005-10-24
 
 Submitted by Abigail.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'reindeer'
DATA = '''\
# names
dasher dancer prancer vixen comet
cupid donner blitzen rudolf\
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


