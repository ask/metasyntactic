# -*- coding: utf-8 -*-
'''

###########################
Acme::MetaSyntactic::smurfs
###########################

****
NAME
****


Acme::MetaSyntactic::smurfs - Smurfs


***********
DESCRIPTION
***********


Various of the smurfs (and supporting characters).


***********
CONTRIBUTOR
***********


Abigail


*******
CHANGES
*******



- \*
 
 2012-07-23 - v1.000
 
 Introduced in Acme-MetaSyntactic-Themes version 1.011.
 


- \*
 
 2006-05-16
 
 Theme proposed independently by Flavio Poletti.
 


- \*
 
 2005-11-01
 
 Submitted by Abigail.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'smurfs'
DATA = '''\
# names
Airborne Alchemist Baby Baker Balthazar Bashful Brainy Clockwork
Clumsy Dabbler Doc Dopey Dreamy Farmer Finance Fisher Gargamel
Grandpa Greedy Grouchy Handy Harmony Hefty Johan Jokey King Miner
Nanny Nat Nosey Painter Papa Poet Princess_Salvina Reflection
Sassette Scaredy Sleepy Sloppy Slouchy Smoogle Smurfette Sneezy
Sweepy Tailor Timid Tracker Vanity Weakling Wild Wooley\
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


