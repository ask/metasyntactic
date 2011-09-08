# -*- coding: utf-8 -*-
'''
.. highlight:: perl


################################
Acme::MetaSyntactic::teletubbies
################################

****
NAME
****


Acme::MetaSyntactic::teletubbies - The teletubbies theme


***********
DESCRIPTION
***********


Over the hills and far away, Teletubbies come to play.


***********
CONTRIBUTOR
***********


Philippe "BooK" Bruhat.

Introduced in version 0.23, published on May 23, 2005.


**************
ACKNOWLEDGMENT
**************


Thanks to Jérôme Fenal, for inspiration over IRC.


********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'teletubbies'
DATA = '''\
# names
Tinky_Winky Dipsy Laa_Laa Po
Noo_Noo Trumpets Baby_Sun Narrator\
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


