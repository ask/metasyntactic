# -*- coding: utf-8 -*-
'''

########################
Acme::MetaSyntactic::foo
########################

****
NAME
****


Acme::MetaSyntactic::foo - The foo theme


***********
DESCRIPTION
***********


The classic. This is the default theme.

As from version 0.85, this theme is multilingual.


************
CONTRIBUTORS
************


Philippe "BooK" Bruhat.

Jrme Fenal and Sbastien Aperghis-Tramoni contributed to the French theme.

Dutch theme contributed by Abigail.

Introduced in Acme-MetaSyntactic version 0.01, published on January 14, 2005.

Merged in the French \ ``toto``\  theme (which was therefore removed from
\ ``Acme::MetaSyntactic``\ ), and added the Dutch theme in version 0.85,
published on July 31, 2006.

Received its own version number for Acme-MetaSyntactic version 1.000,
published on May 7, 2012.

References
==========



- RFC 3092 - \ *Etymology of "Foo"*\ 



- Leesplankje - Dutch Reading Board
 
 The words on the \ *reading boards*\  of the \ *Hoogeveen method*\ , in use in
 Dutch schools from 1905 till the 1950s. The words on the board are often
 used by Dutch programmers to fill the roles of \ *foo*\ , \ *bar*\ , and \ *baz*\ .
 




********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::Locale <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aLocale&mode=module>`_.
'''

name = 'foo'
DATA = '''\
# default
en
# names en
foo    bar   baz  foobar fubar qux  quux corge grault
garply waldo fred plugh  xyzzy thud
# names fr
toto titi tata tutu pipo
bidon test1 test2 test3
truc chose machin chouette bidule
# names nl
aap noot mies wim zus jet
teun vuur gijs lam kees bok
weide does hok duif schapen\
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


