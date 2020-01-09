# -*- coding: utf-8 -*-
'''

##################################
Acme::MetaSyntactic::us_presidents
##################################

****
NAME
****


Acme::MetaSyntactic::us_presidents - The presidents of the USA theme


***********
DESCRIPTION
***********


Presidents of the USA.

This list is based on the official White House list, available at:
`https://www.whitehouse.gov/1600/Presidents <https://www.whitehouse.gov/1600/Presidents>`_.


***********
CONTRIBUTOR
***********


Abigail


*******
CHANGES
*******



- \*
 
 2017-06-12 - v1.001
 
 Updated with the new US president since 2012
 in Acme-MetaSyntactic-Themes version 1.050.
 


- \*
 
 2012-05-07 - v1.000
 
 Updated with the new US president since 2008, and
 received its own version number in Acme-MetaSyntactic-Themes version 1.000.
 


- \*
 
 2006-01-16
 
 Updated (correction of a typo) by Abigail again
 in Acme-MetaSyntactic version 0.57.
 


- \*
 
 Introduced in Acme-MetaSyntactic version 0.52, published on December 12, 2005.
 


- \*
 
 2005-10-20
 
 Submitted by Abigail.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'us_presidents'
DATA = '''\
# names
Abraham_Lincoln
Andrew_Jackson
Andrew_Johnson
Barack_Obama
Benjamin_Harrison
Calvin_Coolidge
Chester_Arthur
Donald_J_Trump
Dwight_Eisenhower
Franklin_D_Roosevelt
Franklin_Pierce
George_H_W_Bush
George_W_Bush
George_Washington
Gerald_Ford
Grover_Cleveland
Harry_S_Truman
Herbert_Hoover
James_Buchanan
James_Garfield
James_Madison
James_Monroe
James_Polk
Jimmy_Carter
John_Adams
John_Kennedy
John_Quincy_Adams
John_Tyler
Lyndon_Johnson
Martin_Van_Buren
Millard_Fillmore
Richard_Nixon
Ronald_Reagan
Rutherford_Hayes
Theodore_Roosevelt
Thomas_Jefferson
Ulysses_Grant
Warren_Harding
William_Clinton
William_Henry_Harrison
William_Howard_Taft
William_McKinley
Woodrow_Wilson
Zachary_Taylor\
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


