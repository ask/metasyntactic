# -*- coding: utf-8 -*-
'''
.. highlight:: perl


#############################
Acme::MetaSyntactic::olympics
#############################

****
NAME
****


Acme::MetaSyntactic::olympics - Olympic cities theme


***********
DESCRIPTION
***********


This theme lists the cities who have hosted, or will host, Olympic Games.
Cities for both the Summer and Winter games are listed.

The list comes from `http://www.olympic.org/ <http://www.olympic.org/>`_.

The following cities have held, or will hold, the Olympic games.


.. code-block:: perl

     Summer Games
     ============
 
     2012   London
     2008   Beijing
     2004   Athens
     2000   Sydney
     1996   Atlanta
     1992   Barcelona
     1988   Seoul
     1984   Los Angeles
     1980   Moscow
     1976   Montreal
     1972   Munich
     1968   Mexico City
     1964   Tokyo
     1960   Rome
     1956   Melbourne
     1952   Helsinki
     1948   London
     1936   Berlin
     1932   Los Angeles
     1928   Amsterdam
     1924   Paris
     1920   Antwerp
     1912   Stockholm
     1908   London
     1904   St. Louis
     1900   Paris
     1896   Athens
 
 
     Winter Games
     ============
 
     2010   Vancouver
     2006   Torino
     2002   Salt Lake City
     1998   Nagano
     1994   Lillehammer
     1992   Albertville
     1988   Calgary
     1984   Sarajevo
     1980   Lake Placid
     1976   Innsbruck
     1972   Sapporo
     1968   Grenoble
     1964   Innsbruck
     1960   Squaw Valley
     1956   Cortina d'Ampezzo
     1952   Oslo
     1948   St. Moritz
     1936   Garmisch-Partenkirchen
     1932   Lake Placid
     1928   St. Moritz
     1924   Chamonix



***********
CONTRIBUTOR
***********


Abigail

Introduced in version 0.82, published on July 10, 2006.


********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'olympics'
DATA = '''\
\
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


