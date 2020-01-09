# -*- coding: utf-8 -*-
'''

##########################
Acme::MetaSyntactic::alice
##########################

****
NAME
****


Acme::MetaSyntactic::alice - Alice in Wonderland/Through the Looking Glass


***********
DESCRIPTION
***********


Characters from both \ *Alice in Wonderland*\  and \ *Through the Looking Glass*\ .

References:
`http://en.wikipedia.org/wiki/Alice%27s_Adventures_in_Wonderland <http://en.wikipedia.org/wiki/Alice%27s_Adventures_in_Wonderland>`_,
`http://en.wikipedia.org/wiki/Through_the_Looking-Glass <http://en.wikipedia.org/wiki/Through_the_Looking-Glass>`_.


***********
CONTRIBUTOR
***********


Abigail


**********
DEDICATION
**********


Philippe dedicates this module to his eldest daughter, Alice,
for her fifth birthday.


*******
CHANGES
*******



- \*
 
 2012-06-18 - v1.000
 
 Introduced in Acme-MetaSyntactic-Themes version 1.006.
 


- \*
 
 2012-06-12
 
 Alice Bruhat-Souche turns 5.
 


- \*
 
 2005-10-24
 
 Submitted by Abigail.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_,
'''

name = 'alice'
DATA = '''\
# names
alice alice_s_sister white_rabbit dinah mouse duck dodo lory eaglet
bill_the_lizard caterpillar fish_footman frog_footman duchess baby
cook cheshire_cat march_hare hatter dormouse two five seven king_of_hearts
queen_of_hearts knave_of_hearts gryphon mock_turtle jurymen

hatta haigha jabberwocky red_queen white_queen tweedledum tweedledee
walrus carpenter humpty_dumpty lion unicorn red_knight white_knight
red_king black_kitten white_kitten \
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


