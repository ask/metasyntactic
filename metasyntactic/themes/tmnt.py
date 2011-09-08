# -*- coding: utf-8 -*-
'''
.. highlight:: perl


#########################
Acme::MetaSyntactic::tmnt
#########################

****
NAME
****


Acme::MetaSyntactic::tmnt - The Teenage Mutant Ninja Turtles theme


***********
DESCRIPTION
***********


The Teenage Mutant Ninja Turtles are a comic series created in 1984 
by Kevin Eastman and Peter Laird. They have been published as comic
books, television series, and movies.

The official web of Mirage Studios has a lot of information about
the TMNT, see `http://www.ninjaturtles.com/ <http://www.ninjaturtles.com/>`_.


***********
CONTRIBUTOR
***********


Abigail

Introduced in version 0.58, published on January 23, 2006.

Made updatable in version 0.59, published on January 30, 2006.


********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'tmnt'
DATA = '''\
# names
Donatello Leonardo Michelangelo Raphael Master_Splinter April_O_Neil
Casey_Jones The_Shredder Hun Foot_Soldier Krang Bebop Rocksteady
Rat_King Leatherhead Slash Mondo_Gecko Ray_Fillet Wingnut Screwloose
Merdude Tattoo Wyrm Dreadmon Jagwar\
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


