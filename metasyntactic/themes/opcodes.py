# -*- coding: utf-8 -*-
'''

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
Opcode module.


************
CONTRIBUTORS
************


Abigail, Philippe Bruhat (BooK)


**********
DEDICATION
**********


This module is dedicated to Perl, which turned 18 years old the day
before this release was published.


*******
CHANGES
*******



- \*
 
 2012-05-07 - v1.000
 
 Received its own version number in Acme-MetaSyntactic-Themes version 1.000.
 


- \*
 
 2005-12-19
 
 Introduced in Acme-MetaSyntactic version 0.53, with the opcodes obtained
 automatically from the Opcode module.
 


- \*
 
 2005-10-25
 
 Submitted by Abigail as a simple list, with the \ ``OP_``\  prefix removed.
 



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


