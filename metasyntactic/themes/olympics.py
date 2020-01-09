# -*- coding: utf-8 -*-
'''

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

The list was originally fetched from `http://www.olympic.org/ <http://www.olympic.org/>`_.

The following cities have held, or will hold, the Olympic games:


.. code-block:: perl

     Summer Games
     ============
 
     2020   Tokyo
     2016   Rio de Janeiro
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
     1904   Saint-Louis
     1900   Paris
     1896   Athens
 
 
     Winter Games
     ============
 
     2018   Pyeongchang
     2014   Sochi
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
     1948   Saint-Moritz
     1936   Garmisch-Partenkirchen
     1932   Lake Placid
     1928   Saint-Moritz
     1924   Chamonix



************
CONTRIBUTORS
************


Abigail, Philippe Bruhat.


*******
CHANGES
*******



- \*
 
 2013-09-16 - v1.002
 
 Turned into a multilist, with all combinations of year and seasons
 as categories and the location for the 2020 summer olympics
 in Acme-MetaSyntactic-Themes version 1.036.
 


- \*
 
 2012-05-14 - v1.001
 
 Updated by Abigail in Acme-MetaSyntactic-Themes version 1.001.
 


- \*
 
 2012-05-07 - v1.000
 
 Updated with recent future Olympic cities, and
 received its own version number in Acme-MetaSyntactic-Themes version 1.000.
 


- \*
 
 2006-07-10
 
 Introduced in Acme-MetaSyntactic version 0.82.
 


- \*
 
 2006-01-26
 
 Submitted by Abigail.
 



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


