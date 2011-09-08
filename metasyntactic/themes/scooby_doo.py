# -*- coding: utf-8 -*-
'''
.. highlight:: perl


###############################
Acme::MetaSyntactic::scooby_doo
###############################

****
NAME
****


Acme::MetaSyntactic::scooby_doo - The Scooby Doo theme


***********
DESCRIPTION
***********


Characters from the Scooby-Doo serial.


***********
CONTRIBUTOR
***********


Michel Rodriguez

Introduced in version 0.78, published on June 12, 2006.


********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::Locale <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aLocale&mode=module>`_.
'''

name = 'scooby_doo'
DATA = '''\
# default
en
# names en
Scooby_Doo Shaggy Daphne Velma Freddy Scrappy_Doo Scooby_Dum   Scooby_Dee
# names fr
Scooby_Doo Sammy Daphne  Vera  Fred   Scrappy_Doo Oncle_Scooby\
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


