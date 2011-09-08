# -*- coding: utf-8 -*-
'''
.. highlight:: perl


###############################
Acme::MetaSyntactic::summerwine
###############################

****
NAME
****


Acme::MetaSyntactic::summerwine - The 'Last of the Summer Wine' theme


***********
DESCRIPTION
***********


Characters in \ *Last of the Summer Wine*\ , the longest-running sitcom in the
world.  Only the 'main' name by which each character is addressed is used
(nickname, Christian name, or surname depending on the character) so that they
make better identifiers.


***********
CONTRIBUTOR
***********


Smylers, who paid �42 for the privilege at the YAPC Europe 2006 auction
in Birmingham.

This theme was chosen because \ *Last of the Summer Wine*\  is set in Smylers's
home town of Holmfirth (in West Yorkshire in the UK), the main character names
are quite fun to use as identifiers, and it was an unlikely theme to be
included otherwise.  Having minor characters called 'Pearl' and 'Smiler' is a
bonus.

Introduced in version 0.99, published on November 6, 2006.


********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'summerwine'
DATA = '''\
# names
compo
clegg
foggy
seymour
truly
nora
ivy
sid
wally
wesley
crusher
howard
pearl
marina
edie
glenda
barry
eli
auntie
smiler
billy
roz
tom
entwistle
alvin
nellie\
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


