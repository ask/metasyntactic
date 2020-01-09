# -*- coding: utf-8 -*-
'''

###########################
Acme::MetaSyntactic::calvin
###########################

****
NAME
****


Acme::MetaSyntactic::calvin - Characters from Calvin and Hobbes


***********
DESCRIPTION
***********


Characters from the famous comic strip, \ *Calvin and Hobbes*\ ,
by \ *Bill Watterson*\ . The comic ran from November 18th, 1985 till
December 31, 1995, 3150 strips in total.

See `http://en.wikipedia.org/wiki/Calvin_and_Hobbes <http://en.wikipedia.org/wiki/Calvin_and_Hobbes>`_.


*****
QUOTE
*****



.. code-block:: perl

     It's a magical world, Hobbes ol' buddy!
               Let's go exploring!



***********
CONTRIBUTOR
***********


Abigail


*******
CHANGES
*******



- \*
 
 2012-07-16 - v1.000
 
 Introduced in Acme-MetaSyntactic-Themes version 1.010.
 


- \*
 
 2005-11-01
 
 Submitted by Abigail.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'calvin'
DATA = '''\
# names
Calvin Hobbes
Mom Dad 
Susie_Derkins Miss_Wormwood Rosalyn Moe
Principal_Spittle Uncle_Max Mr_Lockjaw
Galaxoid Nebular
Stupendous_Man Spaceman_Spiff Tracer_Bullet Captain_Napalm God\
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


