# -*- coding: utf-8 -*-
'''

############################
Acme::MetaSyntactic::antlers
############################

****
NAME
****


Acme::MetaSyntactic::antlers - The antler theme


***********
DESCRIPTION
***********


Kinds of moose and other antlered, er, moose.


***********
CONTRIBUTOR
***********


Gaal Yahas.


*******
CHANGES
*******



- \*
 
 2012-05-07 - v1.000
 
 Received its own version number in Acme-MetaSyntactic-Themes version 1.000.
 


- \*
 
 2005-10-31
 
 Introduced in Acme-MetaSyntactic version 0.46.
 


- \*
 
 2005-09-16
 
 Submitted by Gaal Yahas.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'antlers'
DATA = '''\
# names
moose elk caribou wapiti alces_alces deer hirvi eland oryx antler
velvet_antler\
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


