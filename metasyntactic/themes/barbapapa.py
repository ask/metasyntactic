# -*- coding: utf-8 -*-
'''
.. highlight:: perl


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


***********
CONTRIBUTOR
***********


Abigail

Introduced in version 0.54, published on December 26, 2005.


**********
DEDICATION
**********


Philippe dedicates this module to his niece Enora. Merry Christmas!


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
Barbapapa Barbamama Barbabelle Barbalala Barbibul Barbidou Barbidur
Barbotine Barbouille
# names en
Barbapapa Barbamama Barbabravo Barbabright Barbazoo Barbabeau Barbabelle
Barbalala Barbalib
# names nl
Barbapapa Barbamama Barbabenno Barbabella Barbabientje Barbaborre
Barbabob Barbabee Barbalala
# names de
Barbapapa Barbamama Barbabella Barbaletta Barbarix Barbawum Barbabo
Barbakus Barbalala
# names fi
Barbapapa Barbamama Barbabravo Barbalib Barbazoo Barbabelle Barbalala
Barbabright Barbabeau
# names pl
Barbapapa Barbamama Barbabelle Barbalala Barbibul Barbidou Barbidur
Barbotine Barbouille
# names sv
Barbapapa Barbamama Barbazoo Barbalala Barbabok Barbaskon Barbafin
Barbaflink Barbastark\
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


