# -*- coding: utf-8 -*-
'''
.. highlight:: perl


############################
Acme::MetaSyntactic::browser
############################

****
NAME
****


Acme::MetaSyntactic::browser - The "browser" theme


***********
DESCRIPTION
***********


Some famous web browsers.

Evolt.org maintains a browser archive at `http://browsers.evolt.org/ <http://browsers.evolt.org/>`_.
The information in the archive was not used to create this list (but
may be in the future).


************
CONTRIBUTORS
************


Philippe "BooK" Bruhat, Sébastien Aperghis-Tramoni, Rafaël Garcia-Suarez.

Introduced in version 0.05, published on January 16, 2005.

Updated in version 0.70, published on April 17, 2006.

Updated in version 0.96, published on October 16, 2006.


********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'browser'
DATA = '''\
# names
mozilla netscape msie mosaic links lynx w3m opera galeon konqueror safari
camino dillo amaya arachne omniweb planetweb voyager seamonkey iceweasel\
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


