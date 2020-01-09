# -*- coding: utf-8 -*-
'''

#########################
Acme::MetaSyntactic::afke
#########################

****
NAME
****


Acme::MetaSyntactic::afke - Afke's Children


***********
DESCRIPTION
***********


\ *Afke's tiental*\  (\ *Afkes ten*\ ) is a classic Dutch childrens book,
describing the life of the ten children of Afke. This package supplies
the ten names.


***********
CONTRIBUTOR
***********


Abigail


*******
CHANGES
*******



- \*
 
 2012-05-28 - v1.000
 
 Introduced in Acme-MetaSyntactic-Themes version 1.003.
 


- \*
 
 2005-10-24
 
 Submitted by Abigail.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'afke'
DATA = '''\
# names
eeltje watse klaas jetse jouke
wiepkje sietske boukje wiebe sipke\
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


