# -*- coding: utf-8 -*-
'''
.. highlight:: perl


########################
Acme::MetaSyntactic::pie
########################

****
NAME
****


Acme::MetaSyntactic::pie - The pie theme


***********
DESCRIPTION
***********


A list of English pies.

"Isle of Skye" is, apparently cockney rhyming slang for pie.


***********
CONTRIBUTOR
***********


Nicholas Clark

Introduced in version 0.86, published on August 7, 2006.


********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'pie'
DATA = '''\
# names
apple
cherry
mince
steak_and_kidney
chicken_and_mushroom
beef_and_ale
pumpkin
lemon_merengue
pecan
Isle_of_Skye\
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


