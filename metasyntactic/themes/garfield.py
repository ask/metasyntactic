# -*- coding: utf-8 -*-
'''

#############################
Acme::MetaSyntactic::garfield
#############################

****
NAME
****


Acme::MetaSyntactic::garfield - The Garfield theme


***********
DESCRIPTION
***********


Characters from the comic \ *Garfield*\ , by Jim Davis. First appeared
on June 19, 1978, and still running today. Garfield appears in, or
has appeared in, over 2500 newspapers.

This list does not include characters which only appeared in the
television shows. This may be a bug.


***********
CONTRIBUTOR
***********


Abigail


*******
CHANGES
*******



- \*
 
 2012-05-07
 
 Received its own version number in Acme-MetaSyntactic-Themes version 1.000.
 


- \*
 
 2006-02-20
 
 Introduced in Acme-MetaSyntactic version 0.62.
 


- \*
 
 2005-10-27
 
 Submitted by Abigail.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'garfield'
DATA = '''\
# names
Garfield Odie Jon_Arbuckle
Arlene Pooky Nermal Mom Dad Doc_Boy Grandma Lyman Irma Liz
Herman_Post Hubert Rea Ellen Caped_Avenger 
Squeak Floyd Guido Clive Stretch
Second_Helping Sushi\
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


