# -*- coding: utf-8 -*-
'''
.. highlight:: perl


#########################
Acme::MetaSyntactic::pooh
#########################

****
NAME
****


Acme::MetaSyntactic::pooh - The characters from \ *Winnie-the-Pooh*\  theme


***********
DESCRIPTION
***********


Characters from the classics \ *Winnie-the-Pooh*\  (1926)
and \ *The House at Pooh Corner*\  (1928), by A. A. Milne.


****
BUGS
****


Disney shouldn't have touched Pooh.


*********
NOT A BUG
*********


\ *Winnie-the-Pooh*\  is the correct spelling, no matter what Disney says.


************
CONTRIBUTORS
************


Original contributor: Abigail (late October 2005)

Proposed independently a week later (early November 2005) by Leon Brocard,
with a few additions.

Introduced in version 0.61, published on February 13, 2006.

Updated in version 0.64, published on March 6, 2006.


********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'pooh'
DATA = '''\
# names
Winnie_the_Pooh Christopher_Robin Piglet
Eeyore Owl Rabbit Kanga Roo Tigger
Small Heffalump Woozle
Wizzle Alexander_Beetle Hunny_Bee Jagular
Backson Henry_Pootel Henry_Rush Smallest_of_all Uncle_Robert\
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


