# -*- coding: utf-8 -*-
'''

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


*******
CHANGES
*******



- \*
 
 2012-07-23 - v1.001
 
 \ ``use strict``\  to make Acme-MetaSyntactic-Themes version 1.011
 satisfy all required CPANTS kwalitee tests.
 


- \*
 
 2012-05-07 - v1.000
 
 Received its own version number in Acme-MetaSyntactic-Themes version 1.000.
 


- \*
 
 2005-06-05
 
 Introduced in Acme-MetaSyntactic version 0.77.
 



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


