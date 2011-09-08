# -*- coding: utf-8 -*-
'''
.. highlight:: perl


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

Introduced in version 0.64, published on March 6, 2006.


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


