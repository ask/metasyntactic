# -*- coding: utf-8 -*-
'''
.. highlight:: perl


####################################
Acme::MetaSyntactic::magicroundabout
####################################

****
NAME
****


Acme::MetaSyntactic::magicroundabout - The Magic Round-About theme


***********
DESCRIPTION
***********


Characters from the Magic Round About children television series.


***********
CONTRIBUTOR
***********


Cédric Bouvier, \ ``<cbouvi@cpan.org>``\ .

Introduced in version 0.24, published on May 30, 2005.


********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::Locale <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aLocale&mode=module>`_.
'''

name = 'magicroundabout'
DATA = '''\
# default
en

# names fr
Ambroise
Azalee
Flappy
Margotte
Pollux
Zebulon

# names en
Brian
Dougal
Dylan
Ermintrude
Florence
Zebedee\
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


