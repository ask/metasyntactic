# -*- coding: utf-8 -*-
'''

####################################
Acme::MetaSyntactic::magicroundabout
####################################

****
NAME
****


Acme::MetaSyntactic::magicroundabout - The Magic Round-About theme


***********
DESCRIPTION
***********


Characters from the Magic Round About children television series.


***********
CONTRIBUTOR
***********


Cdric Bouvier, \ ``<cbouvi@cpan.org>``\ .


*******
CHANGES
*******



- \*
 
 2012-05-14 - v1.001
 
 Updated with an \ ``=encoding``\  pod command in version 1.001.
 


- \*
 
 2012-05-07 - v1.000
 
 Received its own version number in Acme-MetaSyntactic-Themes version 1.000.
 


- \*
 
 2005-05-30
 
 Introduced in Acme-MetaSyntactic version 0.24.
 


- \*
 
 2005-04-06
 
 Submitted by Cdric Bouvier.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::Locale <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aLocale&mode=module>`_.
'''

name = 'magicroundabout'
DATA = '''\
# default
en

# names fr
Ambroise
Azalee
Flappy
Margotte
Pollux
Zebulon

# names en
Brian
Dougal
Dylan
Ermintrude
Florence
Zebedee\
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


