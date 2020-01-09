# -*- coding: utf-8 -*-
'''

############################
Acme::MetaSyntactic::bottles
############################

****
NAME
****


Acme::MetaSyntactic::bottles - Bottle sizes, kings, patriarchs and private eyes


***********
DESCRIPTION
***********


Names for wine and champagne bottles of different sizes.

This list is a mixed bag containing ancient kings,
biblical patriarchs and an Hawaiian private eye.

Yet, some people pretend this list is a companion
to `Acme::MetaSyntactic::booze <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3abooze&mode=module>`_.

Sources:


- \*
 
 `http://fr.wikipedia.org/wiki/Vin_de_Champagne#Flacons <http://fr.wikipedia.org/wiki/Vin_de_Champagne#Flacons>`_,
 


- \*
 
 `http://www.diracdelta.co.uk/science/source/b/o/bottle/source.html <http://www.diracdelta.co.uk/science/source/b/o/bottle/source.html>`_,
 


- \*
 
 `http://damngoodwine.com/botts1.htm <http://damngoodwine.com/botts1.htm>`_,
 


- \*
 
 `http://www.champagnemagic.com/sizes.htm <http://www.champagnemagic.com/sizes.htm>`_,
 


- \*
 
 `http://www.ebrew.com/primarynews/wine_bottle_sizes.htm <http://www.ebrew.com/primarynews/wine_bottle_sizes.htm>`_,
 


- \*
 
 `http://www.awinestore.com/big_bottles.htm <http://www.awinestore.com/big_bottles.htm>`_.
 



************
CONTRIBUTORS
************


Abigail, Jean Forget.


*******
CHANGES
*******



- \*
 
 2012-09-10 - v1.000
 
 Merged both versions of the module in a single one,
 published in Acme-MetaSyntactic-Themes version 1.018.
 


- \*
 
 2006-08-09
 
 Submitted by Jean Forget, as a multilist with French and English bottle names.
 


- \*
 
 2005-11-01
 
 Submitted by Abigail.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::Locale <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aLocale&mode=module>`_.
'''

name = 'bottles'
DATA = '''\
# default
en
# names en
split                quarter_bottle   piccolo
half_bottle          demiboite
bottle               fifth
magnum
marie_jean
double_magnum        jeroboam
rehoboam
imperial             methusalem       methusalah
salmanazar
balthazar
nebuchadnezzar
solomon              melchior
sovereign
primat
# names fr
bouteille
magnum
jeroboam
rehoboam
mathusalem
salmanazar
balthazar
nabuchodonosor\
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


