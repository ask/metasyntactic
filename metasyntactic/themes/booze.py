# -*- coding: utf-8 -*-
'''
.. highlight:: perl


##########################
Acme::MetaSyntactic::booze
##########################

****
NAME
****


Acme::MetaSyntactic::booze - The booze theme (not for teetotalers)


***********
DESCRIPTION
***********


Types of alcoholic beverages.


***********
CONTRIBUTOR
***********


Nicholas Clark, after seeing BooK's talk at YAPC::Europe 2005 and amazed
that there was such an obvious omission.

Introduced in version 0.45, published on October 24, 2005.

Updated in version 0.51 (thus closing RT ticket #16256 opened by David
Landgren), published on December 5, 2005.


****
BUGS
****


This list is incomplete. I try to drink my way further along, but I forget
where I get to. \ ``%-)``\ 


********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'booze'
DATA = '''\
# names
beer
cider
perry
stout
porter
lager
wine
gin
rum
vodka
whisky
whiskey
port
sherry
absinthe
ale
mead
brandy
champagne
ouzo
martini
vermouth
suze
tequila
amaretto
drambuie\
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


