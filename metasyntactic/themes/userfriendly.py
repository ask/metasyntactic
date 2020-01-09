# -*- coding: utf-8 -*-
'''

#################################
Acme::MetaSyntactic::userfriendly
#################################

****
NAME
****


Acme::MetaSyntactic::userfriendly - The \ *User Friendly*\  theme


***********
DESCRIPTION
***********


Characters from the web comic \ *User Friendly*\ . The daily comic first
appeared on November 17, 1997, and is drawn by Illiad.

Read it at `http://www.userfriendly.org/ <http://www.userfriendly.org/>`_.


***********
CONTRIBUTOR
***********


Abigail


*******
CHANGES
*******



- \*
 
 2012-05-07 - v1.000
 
 Received its own version number in Acme-MetaSyntactic-Themes version 1.000.
 


- \*
 
 2006-05-15
 
 Introduced in Acme-MetaSyntactic version 0.74.
 


- \*
 
 2005-10-27
 
 Submitted by Abigail.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'userfriendly'
DATA = '''\
# names
A_J The_Chief Dust_Puppy Erwin Greg Mike Miranda Pitr Sid Smiling_Man Stef
Artur BSD_Daemon Clippy Cobb Mr_Cola Crud_Puppy Cthulhu Hillary Matt
Pearl Tanya Tux\
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


