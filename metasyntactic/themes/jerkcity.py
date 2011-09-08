# -*- coding: utf-8 -*-
'''
.. highlight:: perl


#############################
Acme::MetaSyntactic::jerkcity
#############################

****
NAME
****


Acme::MetaSyntactic::jerkcity - The Jerkcity theme


***********
DESCRIPTION
***********


Character names and other keywords from the popular (at least
on #perl) webcomic \ *jerkcity*\ .

See `http://www.jerkcity.com/ <http://www.jerkcity.com/>`_ for details.


***********
CONTRIBUTOR
***********


Rafael Garcia-Suarez.

Introduced in version 0.37, published on August 29, 2005.


********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'jerkcity'
DATA = '''\
# names
Atandt Bung Deuce Dick Effigy Hanford Harriet Jean_Charles Net Ozone
Pants Rands Spigot T HUGLAGHALGHALGHAL gay dicks dongs rape piss\
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


