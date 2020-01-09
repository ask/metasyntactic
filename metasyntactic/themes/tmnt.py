# -*- coding: utf-8 -*-
'''

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


*******
CHANGES
*******



- \*
 
 2012-05-07
 
 Received its own version number in Acme-MetaSyntactic-Themes version 1.000.
 


- \*
 
 2006-01-30
 
 Made updatable in Acme-MetaSyntactic version 0.59.
 


- \*
 
 2006-01-23
 
 Introduced in Acme-MetaSyntactic version 0.58.
 


- \*
 
 2005-10-26
 
 Submitted by Abigail.
 


Source URL and list updated in v1.001, published in Acme-MetaSyntactic-Theme
1.002, on May 21, 2012.


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
Merdude Tattoo Wyrm Dreadmon Jagwar Dragon_Lord Venus_de_Milo\
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


