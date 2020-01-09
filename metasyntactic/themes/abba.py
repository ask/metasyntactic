# -*- coding: utf-8 -*-
'''

#########################
Acme::MetaSyntactic::abba
#########################

****
NAME
****


Acme::MetaSyntactic::abba - Singers from the 1970s Swedish pop group


***********
DESCRIPTION
***********


ABBA won the 1974 Eurovision Songfestival for Sweden, which started
their very successful international career that would last into the
early 1980s.


***********
CONTRIBUTOR
***********


Abigail


*******
CHANGES
*******



- \*
 
 2012-05-07 - v1.000
 
 Introduced in Acme-MetaSyntactic-Themes version 1.000.
 


- \*
 
 2005-11-01
 
 Submitted by Abigail.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'abba'
DATA = '''\
# names
Anni_Frid_Lyngstad Bjorn_Ulvaeus Benny_Andersson Agnetha_Faltskog\
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


