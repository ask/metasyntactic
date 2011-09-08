# -*- coding: utf-8 -*-
'''
.. highlight:: perl


##########################
Acme::MetaSyntactic::buffy
##########################

****
NAME
****


Acme::MetaSyntactic::buffy - The Buffy theme


***********
DESCRIPTION
***********


The characters from London.pm's favorite serial.
Courtesy of `http://buffyology.johnhorner.nu/ <http://buffyology.johnhorner.nu/>`_.


***********
CONTRIBUTOR
***********


Rafael Garcia-Suarez.

Introduced in version 0.09, published on February 7, 2005.


********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'buffy'
DATA = '''\
# names
Adam Angel Anya Buffy Cordelia Darla Dawn Drusilla Faith Giles Glory
Jenny Jonathan Joyce Kendra Oz Snyder Prof_Walsh Riley Spike Tara
The_Master The_Mayor Warren Wesley Willow Xander\
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


