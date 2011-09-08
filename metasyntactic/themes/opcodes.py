# -*- coding: utf-8 -*-
'''
.. highlight:: perl


############################
Acme::MetaSyntactic::opcodes
############################

****
NAME
****


Acme::MetaSyntactic::opcodes - The Perl opcodes theme


***********
DESCRIPTION
***********


The names of the Perl opcodes. They are given by the
\ ``Opcode``\  module.


***********
CONTRIBUTOR
***********


Abigail

Introduced in version 0.53, published on December 19, 2005.


**********
DEDICATION
**********


This module is dedicated to Perl, which turned 18 years old the day
before this release was published.


********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'opcodes'
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


