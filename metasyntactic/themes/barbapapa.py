# -*- coding: utf-8 -*-
'''

##############################
Acme::MetaSyntactic::barbapapa
##############################

****
NAME
****


Acme::MetaSyntactic::barbapapa - The Barbapapa theme


***********
DESCRIPTION
***********


The Barbapapa family consists of 9 members, 7 children and 2 adults.
This cartoon series was created by French architect Annette Tison and
her American husband Talus Taylor in 1970. First as comic books, and
later as a television series.

The official Barbapapa web site is at `http://www.barbapapa.fr/ <http://www.barbapapa.fr/>`_.


************
CONTRIBUTORS
************


Abigail, Philippe Bruhat (BooK).


**********
DEDICATION
**********


Philippe dedicates this module to his niece Enora. Merry Christmas!


*******
CHANGES
*******



- \*
 
 2012-05-07 - v1.000
 
 Updated with the Italian, Spanish and Slovene version, and
 received its own version number in Acme-MetaSyntactic-Themes version 1.000.
 


- \*
 
 2005-12-26
 
 Introduced in Acme-MetaSyntactic version 0.54.
 


- \*
 
 2005-10-25
 
 Submitted by Abigail with seven languages (English, French, Dutch, German,
 Finnish, Polish and Swedish).
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::Locale <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aLocale&mode=module>`_.
'''

name = 'barbapapa'
DATA = '''\
# default
fr
# names fr
Barbapapa Barbamama  Barbabelle Barbotine    Barbalala  Barbidou Barbidur   Barbibul    Barbouille
# names en
Barbapapa Barbamama  Barbabelle Barbalib     Barbalala  Barbazoo Barbabravo Barbabright Barbabeau
# names nl
Barbapapa Barbamama  Barbabella Barbabientje Barbalala  Barbabee Barbaborre Barbabenno  Barbabob
# names de
Barbapapa Barbamama  Barbabella Barbaletta   Barbalala  Barbakus Barbawum   Barbarix    Barbabo
# names fi
Barbapapa Barbamama  Barbabelle Barbalib     Barbalala  Barbazoo Barbabravo Barbabright Barbabeau
# names pl
Barbapapa Barbamama  Barbabelle Barbotine    Barbalala  Barbidou Barbidur   Barbibul    Barbouille
# names sv
Barbapapa Barbamama  Barbafin   Barbabok     Barbalala  Barbazoo Barbastark Barbaflink  Barbaskon
# names it
Barbapapa Barbamamma Barbabella Barbottina   Barbalalla Barbazoo Barbaforte Barbabravo  Barbabarba
# names es
Barbapapa Barbamama  Barbabella Barbalib     Barbalala  Barbazoo Barbabravo Barbabrillo Barbabello
# names sl
Barbapapa Barbamama  Barbalepa  Barbabrala   Barbalala  Barbazoo Barbabravo Barbaplus   Barbazal\
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


