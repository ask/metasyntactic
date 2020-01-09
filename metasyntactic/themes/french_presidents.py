# -*- coding: utf-8 -*-
'''

######################################
Acme::MetaSyntactic::french_presidents
######################################

****
NAME
****


Acme::MetaSyntactic::french_presidents - The presidents of France theme


***********
DESCRIPTION
***********


Presidents of the various French republics.

This list is based on the official lyse list, available at:
`http://www.elysee.fr/la-presidence/les-presidents-de-la-republique-depuis-1848/ <http://www.elysee.fr/la-presidence/les-presidents-de-la-republique-depuis-1848/>`_.
The typograpical errors in the names have been corrected, though.


*****************
FRENCH PRESIDENTS
*****************


The Fifth Republic
==================



- Emmanuel Macron (2017-)



- Franois Hollande (2012-2017)



- Nicolas Sarkozy (2007-2012)



- Jacques Chirac (1995-2007)



- Franois Mitterrand (1981-1995)



- Valry Giscard d'Estaing (1974-1981)



- Alain Poher (1974, interim from 02/04/1974 to 19/05/1974)



- Georges Pompidou (1969-1974)



- Alain Poher (1969, interim from 28/04/1969 to 20/06/1969)



- Charles de Gaulle (1959-1969)




The Fourth Republic
===================



- Ren Coty (1954-1959)



- Vincent Auriol (1947-1954)




The Third Republic
==================



- Albert Lebrun (1932-1940)



- Paul Doumer (1931-1932)



- Gaston Doumergue (1924-1931)



- Alexandre Millerand (1920-1924)



- Paul Deschanel (18 fv-20 sept 1920)



- Raymond Poincar (1913-1920)



- Armand Fallires (1906-1913)



- mile Loubet (1899-1906)



- Flix Faure (1895-1899)



- Jean Casimir-Perier (1894-1895)



- Marie Franois Sadi Carnot (1887-1894)



- Jules Grvy (1879-1887)



- Patrice de Mac Mahon (1873-1879)



- Adolphe Thiers (1871-1873)




The Second Republic
===================



- Louis-Napolon Bonaparte (1848-1851)





***********
CONTRIBUTOR
***********


Philippe Bruhat (BooK)


*******
CHANGES
*******



- \*
 
 2017-06-12 - v1.001
 
 Updated with the latest president, and the new URL for the authoritative list,
 in Acme-MetaSyntactic-Themes version 1.050.
 


- \*
 
 2012-05-07 - v1.000
 
 Introduced in Acme-MetaSyntactic-Themes version 1.000
 (the day after the election of Franois Hollande).
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'french_presidents'
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


