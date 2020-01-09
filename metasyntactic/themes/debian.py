# -*- coding: utf-8 -*-
'''

###########################
Acme::MetaSyntactic::debian
###########################

****
NAME
****


Acme::MetaSyntactic::debian - The debian theme


***********
DESCRIPTION
***********


This theme lists all the Debian codenames. So far they have been
characters taken from the movie \ *Toy Story*\  by Pixar.

Source: `http://www.debian.org/doc/manuals/debian-faq/ch-ftparchives.en.html#s-sourceforcodenames <http://www.debian.org/doc/manuals/debian-faq/ch-ftparchives.en.html#s-sourceforcodenames>`_.


***********
CONTRIBUTOR
***********


Philippe Bruhat (Book).


*******
CHANGES
*******



- \*
 
 2019-07-29 - v1.004
 
 Added \ ``bullseye``\  and \ ``bookworm``\  to the list of Debiam codenames.
 Published in Acme-MetaSyntactic-Themes version 1.053.
 


- \*
 
 2018-10-29 - v1.003
 
 Added \ ``buster``\  to the list of Debian codenames.
 Published in Acme-MetaSyntactic-Themes version 1.052.
 


- \*
 
 2015-06-08 - v1.002
 
 Added \ ``stretch``\  to the list of Debian codenames.
 Published in Acme-MetaSyntactic-Themes version 1.046.
 


- \*
 
 2013-06-17 - v1.001
 
 Added \ ``jessie``\  to the list of Debian codenames.
 Published in Acme-MetaSyntactic-Themes version 1.033.
 


- \*
 
 2012-05-07 - v1.000
 
 Updated with the new Debian versions since 2007, and
 received its own version number in Acme-MetaSyntactic-Themes version 1.000.
 


- \*
 
 2005-05-02
 
 Introduced in Acme-MetaSyntactic version 0.20.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'debian'
DATA = '''\
# names
buzz rex bo
hamm slink potato
woody sarge etch
lenny squeeze wheezy
jessie stretch buster
bullseye bookworm
sid\
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


