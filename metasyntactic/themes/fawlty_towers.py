# -*- coding: utf-8 -*-
'''

##################################
Acme::MetaSyntactic::fawlty_towers
##################################

****
NAME
****


Acme::MetaSyntactic::fawlty_towers - Characters and episodes from Fawlty Towers


***********
DESCRIPTION
***********


The main characters and episodes from the British sitcom \ *Fawlty Towers*\ ,
of which 12 episodes where made in the 1975 and 1979.

See `http://www.fawltysite.net/ <http://www.fawltysite.net/>`_.

Cast
====



.. code-block:: perl

  ACTOR                    ROLE
  John Cleese              Basil Fawlty
  Prunella Scales          Sybil Fawlty
  Connie Booth             Polly Sherman
  Andrew Sachs             Manuel
  Ballard Berkely          Major Gowen
  Gilly Flower             Miss Tibbs
  Renee Roberts            Miss Gatsby
  Brian Hall               Terry the Chef



Episodes
========



.. code-block:: perl

  SERIES 1 (1975)          SERIES 2 (1979)
  A Touch of Class         Communication Problems
  The Builders             The Psychiatrist
  The Wedding Party        Waldorf Salad
  The Hotel Inspectors     The Kipper and the Corpse
  Gourmet Night            The Anniversary
  The Germans              Brasil the Rat




***********
CONTRIBUTOR
***********


Abigail


*******
CHANGES
*******



- \*
 
 2012-10-29 - v1.000
 
 Published in Acme-MetaSyntactic-Themes version 1.025.
 


- \*
 
 2012-09-30
 
 Merged both themes in a single one.
 


- \*
 
 2005-11-04
 
 Submitted by Abigail as two separate themes:
 \ *fawlty_towers*\  and \ *fawlty_towers_episodes*\ .
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::MultiList <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aMultiList&mode=module>`_.
'''

name = 'fawlty_towers'
DATA = '''\
# default
characters
# names characters
Basil Sybil Polly Manual Gowen Tibbs Gatsby Terry
# names episodes
A_Touch_of_Class             The_Builders        The_Wedding_Party
The_Hotel_Inspectors         Gourmet_Night       The_Germans
Communication_Problems       The_Psychiatrist    Waldorf_Salad
The_Kipper_and_the_Corpse    The_Anniversary     Brasil_the_Rat\
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


