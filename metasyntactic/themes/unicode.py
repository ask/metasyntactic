# -*- coding: utf-8 -*-
'''
.. highlight:: perl


############################
Acme::MetaSyntactic::unicode
############################

****
NAME
****


Acme::MetaSyntactic::unicode - The unicode theme


***********
DESCRIPTION
***********


The name of all Unicode characters known to Perl.

Note that since your Perl installation knows all these names, they
are not included in the source of this module (that's the whole point).


***********
CONTRIBUTOR
***********


Philippe "BooK" Bruhat.

Thanks to Sébastien Aperghis-Tramoni for his help in finding
\ *unicore/Name.pl*\ .

Introduced in version 0.50, published on November 28, 2005.

Updated to support more Perl versions in version 0.51, published
on December 5, 2005.


********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'unicode'
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


