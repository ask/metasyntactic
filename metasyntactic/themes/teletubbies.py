# -*- coding: utf-8 -*-
'''

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


**************
ACKNOWLEDGMENT
**************


Thanks to Jrme Fenal, for inspiration over IRC.


*******
CHANGES
*******



- \*
 
 2012-05-14 - v1.001
 
 Updated with an \ ``=encoding``\  pod command
 in Acme-MetaSyntactic-Themes version 1.001.
 


- \*
 
 2012-05-07 - v1.000
 
 Received its own version number in Acme-MetaSyntactic-Themes version 1.000.
 


- \*
 
 2005-05-23
 
 Introduced in Acme-MetaSyntactic version 0.23.
 



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


