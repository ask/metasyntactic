# -*- coding: utf-8 -*-
'''

###############################
Acme::MetaSyntactic::barbarella
###############################

****
NAME
****


Acme::MetaSyntactic::barbarella - Characters from the movie


***********
DESCRIPTION
***********


According to `http://www.hollywoodcomics.com/forestbbd.html <http://www.hollywoodcomics.com/forestbbd.html>`_, 
Jean-Claude Forest created the character of Barbarella for \ *V-Magazine*\ 
in 1962. Barbarella was an immediate runaway bestseller and was soon
translated in a dozen countries. Not long after, it was adapted into
a major motion picture, starring Jane Fonda, for which Forest acted as
design consultant.

This theme lists the main characters from the 1968 movie, \ *Barbarella*\ ,
starring Jane Fonda.

The list is taken from `http://www.imdb.com/title/tt0062711/fullcredits <http://www.imdb.com/title/tt0062711/fullcredits>`_.


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
 
 2006-01-16
 
 Introduced in Acme-MetaSyntactic version 0.57.
 


- \*
 
 2005-10-26
 
 Submitted by Abigail.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_,
'''

name = 'barbarella'
DATA = '''\
# names
Barbarella Pygar The_Great_Tyrant Durand_Durand Professor_Ping
President_of_Earth Captain_Moon Captain_Sun Stomoxys Glossina
Dildano Mark_Hand\
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


