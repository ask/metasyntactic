# -*- coding: utf-8 -*-
'''
.. highlight:: perl


###########################
Acme::MetaSyntactic::oulipo
###########################

****
NAME
****


Acme::MetaSyntactic::oulipo - The Oulipo theme


***********
DESCRIPTION
***********


This theme contains the initials of the members of the French literary
group Oulipo, created by Raymond Queneau (RQ) and François Le Lionnais
(FLL) in 1960. These initials are commonly used in place of a member's
full name.

See the official Oulipo web site at `http://www.oulipo.net/ <http://www.oulipo.net/>`_.


***********
CONTRIBUTOR
***********


Philippe "BooK" Bruhat (co-creator of the first Oulipo web site, back
in 1995).

Introduced in version 0.28, published on June 27, 2005.


********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'oulipo'
DATA = '''\
# names
NA  MB  VB  JB  CB  AB  PB  IC  FC  BC  RC  SC
MD  JD  LE  FF  PF  AG  MG  JJ  AL  FLL HLT JL
HM  MM  IM  OP  GP  RQ  JQ  PR  JR  OS  AMS\
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


