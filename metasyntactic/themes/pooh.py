# -*- coding: utf-8 -*-
'''

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


Abigail, Lon Brocard.


*******
CHANGES
*******



- \*
 
 2012-05-07 - v1.000
 
 Received its own version number in Acme-MetaSyntactic-Themes version 1.000.
 


- \*
 
 2006-03-06
 
 Updated in Acme-MetaSyntactic version 0.64.
 


- \*
 
 2006-02-16
 
 Abigail sent a patch with a few additions.
 


- \*
 
 2006-02-13
 
 Introduced in Acme-MetaSyntactic version 0.61.
 


- \*
 
 2005-11-03
 
 Submitted independently by Leon Brocard, with a few additions.
 


- \*
 
 2005-10-27
 
 Submitted by Abigail.
 



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


