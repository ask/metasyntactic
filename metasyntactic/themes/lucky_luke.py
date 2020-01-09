# -*- coding: utf-8 -*-
'''

###############################
Acme::MetaSyntactic::lucky_luke
###############################

****
NAME
****


Acme::MetaSyntactic::lucky_luke - Characters from \ *Lucky Luke*\ 


***********
DESCRIPTION
***********


Characters from the comic \ *Lucky Luke*\ , by Morris et. al.


****
BUGS
****


This list isn't complete.


***********
CONTRIBUTOR
***********


Abigail


*******
CHANGES
*******



- \*
 
 2012-08-06 - v1.000
 
 Introduced in Acme-MetaSyntactic-Themes version 1.013.
 


- \*
 
 2005-10-27
 
 Submitted by Abigail.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'lucky_luke'
DATA = '''\
# names
Lucky_Luke Jolly_Jumper Rantanplan
Ma_Dalton Joe_Dalton William_Dalton Jack_Dalton Averell_Dalton
Calamity_Jane Billy_the_Kid Judge_Roy_Bean Jesse_James\
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


