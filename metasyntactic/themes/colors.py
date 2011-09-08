# -*- coding: utf-8 -*-
'''
.. highlight:: perl


###########################
Acme::MetaSyntactic::colors
###########################

****
NAME
****


Acme::MetaSyntactic::colors - The colors theme


***********
DESCRIPTION
***********


This theme is just an alias of the \ ``colours``\  theme, to please the
speakers of the various dialects of English. \ ``;-)``\ 


***********
CONTRIBUTOR
***********


Philippe Bruhat

Introduced in version 0.77, published on June 5, 2006.


********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::Alias <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aAlias&mode=module>`_,
`Acme::MetaSyntactic::colours <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3acolours&mode=module>`_.
'''

name = 'colors'
DATA = '''\
\
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


