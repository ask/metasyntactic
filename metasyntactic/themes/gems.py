# -*- coding: utf-8 -*-
'''

#########################
Acme::MetaSyntactic::gems
#########################

****
NAME
****


Acme::MetaSyntactic::gems - The gem stones theme


***********
DESCRIPTION
***********


A list of gem stones, as given by
`http://http://en.wikipedia.org/wiki/Gemstone <http://http://en.wikipedia.org/wiki/Gemstone>`_.


***********
CONTRIBUTOR
***********


Abigail


*******
CHANGES
*******



- \*
 
 2012-05-07
 
 Received its own version number in Acme-MetaSyntactic-Themes version 1.000.
 


- \*
 
 2006-02-06
 
 Introduced in Acme-MetaSyntactic version 0.60.
 


- \*
 
 2005-10-27
 
 Submitted by Abigail.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'gems'
DATA = '''\
# names
agate alexandrite amber amethyst ammolite andalusite aquamarine axinite
benitoite beryl bone cassiterite chrysoberyl chrysocolla chrysoprase
citrine clinohumite coral diamond emerald feldspar garnet girasol hematite
iolite ivory jade jadeite jasper jet kornerupine kunzite lapis_lazuli
lignite malachite moonstone mother_of_pearl nephrite obsidian olivine
opal pearl peridot pyrite quartz ruby sapphire spinel sugilite tanzanite
tiger_s_eye topaz tortoiseshell tourmaline turquoise zircon zoisite\
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


