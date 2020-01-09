# -*- coding: utf-8 -*-
'''

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


****
BUGS
****


This list is incomplete. I try to drink my way further along, but I forget
where I get to. \ ``%-)``\ 


*******
CHANGES
*******



- \*
 
 2012-05-07 - v1.000
 
 Updated with Chartreuse (incredible omission!), and
 received its own version number in Acme-MetaSyntactic-Themes version 1.000.
 


- \*
 
 2005-12-05
 
 Updated in Acme-MetaSyntactic version 0.51
 (thus closing RT ticket #16256 opened by David Landgren).
 


- \*
 
 2005-10-24
 
 Introduced in Acme-MetaSyntactic version 0.45.
 


- \*
 
 2005-09-08
 
 Submitted by Nicholas Clark.
 



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
drambuie
chartreuse\
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


