# -*- coding: utf-8 -*-
'''

###########################
Acme::MetaSyntactic::trigan
###########################

****
NAME
****


Acme::MetaSyntactic::trigan - The \ *The Trigan Empire*\  theme


***********
DESCRIPTION
***********


Characters from the British comic \ *The Trigan Empire*\ , written
mainly by Mike Butterworth with beautiful artwork by \ *Don Lawrence*\ .
The comic ran from 1965 till 1982.

Learn all about it on `http://www.trigan.com/ <http://www.trigan.com/>`_.


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
 
 2006-03-06
 
 Introduced in Acme-MetaSyntactic version 0.64.
 


- \*
 
 2005-10-27
 
 Submitted by Abigail.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'trigan'
DATA = '''\
# names
Trigo Brag Klud Peric Janno Keren Roffa Salvia Kassar Ursa Argo Rilla Nikka\
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


