# -*- coding: utf-8 -*-
'''

##########################
Acme::MetaSyntactic::bible
##########################

****
NAME
****


Acme::MetaSyntactic::bible - Bible books


***********
DESCRIPTION
***********


List of bible books (King James version).


***********
CONTRIBUTOR
***********


Abigail


*******
CHANGES
*******



- \*
 
 2012-10-08 - v1.000
 
 Published in Acme-MetaSyntactic-Themes version 1.022.
 


- \*
 
 2005-10-24
 
 Submitted by Abigail.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'bible'
DATA = '''\
# names
genesis exodus leviticus numbers deuteronomy joshua judges ruth i_samuel
ii_samuel i_kings ii_kings i_chronicles ii_chronicles ezra nehemiah esther
job psalms proverbs ecclesiastes song_of_solomon isaiah jeremiah
lamentations ezekiel daniel hosea joel amos obadiah jonah micah nahum
habakkuk zephaniah haggai zechariah malachi

matthew mark luke john acts_of_the_apostles romans i_corinthians
ii_corinthians galatians ephesians philippians colossians i_thessalonians
ii_thessalonians i_timothy ii_timothy titus philemon hebrews james
i_peter ii_peter i_john ii_john iii_john jude revelation\
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


