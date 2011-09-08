# -*- coding: utf-8 -*-
'''
.. highlight:: perl


#########################
Acme::MetaSyntactic::groo
#########################

****
NAME
****


Acme::MetaSyntactic::groo - The Groo the Wanderer theme


***********
DESCRIPTION
***********


A list of characters from the \ *Groo the Wanderer*\  long-running
comic-book authored by Sergio Aragonès and Mark Evanier.

If you are interested in Groo, you should have a look at
`http://www.groo.com/ <http://www.groo.com/>`_, `http://www.povonline.com/ <http://www.povonline.com/>`_ and
`http://www.sergioaragones.com/ <http://www.sergioaragones.com/>`_.


***********
CONTRIBUTOR
***********


Philippe "BooK" Bruhat.

Introduced in version 0.27, published on June 21, 2005.

Corrected a typo in version 0.82, published on July 10, 2006.


********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'groo'
DATA = '''\
# names
Groo Rufferto Sage Chakaal Minstrel Grooella Arba Dakarba Arcadio
Taranto Pal Drumm Mulch Scribe Weaver Gravito Granny_Groo Pipil_Khan
The_Witch_of_Kaan Captain_Ahax\
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


