# -*- coding: utf-8 -*-
'''
.. highlight:: perl


###########################
Acme::MetaSyntactic::crypto
###########################

****
NAME
****


Acme::MetaSyntactic::crypto - The crypto theme


***********
DESCRIPTION
***********


The classic characters from crypto and protocol
communications texts.

The list in 0.04 was based on:
`http://www.cacr.math.uwaterloo.ca/~dstinson/CS_758/2003/lec23.ps <http://www.cacr.math.uwaterloo.ca/~dstinson/CS_758/2003/lec23.ps>`_.

The list has been updated with information from:
`http://www.disappearing-inc.com/A/alice.html <http://www.disappearing-inc.com/A/alice.html>`_
`http://en.wikipedia.org/wiki/Alice_and_Bob <http://en.wikipedia.org/wiki/Alice_and_Bob>`_


************
CONTRIBUTORS
************


Idea by Anonymous \ ``<nobody@nowhere.org>``\ . See ticket #9725 on
`http://rt.cpan.org/ <http://rt.cpan.org/>`_.

Guy Widloecher provided some more items and links. See the
same ticket on RT.

Introduced in version 0.04, published on January 15, 2005.

Updated in version 0.28, published on June 27, 2005.


********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'crypto'
DATA = '''\
# names
alice
bob
charlie
doris dave
eve ellen
fred frank
ginger
harry
irene isaac ivan
janet justin
mallory mallet matilda
pat peggy plod
oscar
sam
trudy trent
vanna victor
walter\
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


