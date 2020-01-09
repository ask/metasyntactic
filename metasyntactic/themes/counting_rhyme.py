# -*- coding: utf-8 -*-
'''

###################################
Acme::MetaSyntactic::counting_rhyme
###################################

****
NAME
****


Acme::MetaSyntactic::counting_rhyme - The counting rhyme theme


***********
DESCRIPTION
***********


Based on popular children counting rhymes, mostly used to decide roles
in games (who'll be the wolf?)


*************
FULL VERSIONS
*************


English
=======



.. code-block:: perl

     Eeny, meeny, miny, moe
     Catch a tiger by the toe
     If he hollers let him go,
     Eeny, meeny, miny, moe.



French
======



.. code-block:: perl

     Am, stram, gram,
     Pique et pique et colgram
     Bourre, bourre et ratatam
     Am, stram, gram.



Dutch
=====



.. code-block:: perl

     Iene, miene, mutte,
     tien pond grutten,
     tien pond kaas,
     Iene, miene, mutte,
     is de baas.



German
======



.. code-block:: perl

     Eene, Meene, Muh, und raus bist du
     Eene, Meene, Maus, und du bist raus
     Eene, Meene, Meck, und du bist weg
     Weg bist du noch lange nicht,
     sag mir erst wie alt du bist.




************
CONTRIBUTORS
************


Xavier Caron, Paul-Christophe Varoutas, Abigail, Yanick and Anja Champoux.


*******
CHANGES
*******



- \*
 
 2012-05-14 - v1.001
 
 Updated with an \ ``=encoding``\  pod command in Acme-Meta version 1.001.
 


- \*
 
 2012-05-07 - v1.000
 
 Received its own version number in Acme-MetaSyntactic-Themes version 1.000.
 


- \*
 
 2006-04-03
 
 Updated with the German theme in Acme-MetaSyntactic version 0.68.
 


- \*
 
 2006-03-24
 
 Yanick Champoux provided a patch to add a German countring rhyme (RT #18330).
 


- \*
 
 2005-11-07
 
 Updated with the Dutch theme in Acme-MetaSyntactic version 0.47.
 


- \*
 
 2005-10-25
 
 Abigail provided a patch to add a Dutch counting rhyme.
 


- \*
 
 2005-09-12
 
 Patched a typo in Acme-MetaSyntactic version 0.39.
 


- \*
 
 2005-07-11
 
 Introduced in Acme-MetaSyntactic version 0.30.
 
 Xavier Caron proposed the idea in French, and Paul-Christophe Varoutas
 provided the English version.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::Locale <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aLocale&mode=module>`_.
'''

name = 'counting_rhyme'
DATA = '''\
# default
en
# names en 
eenie meeny miny moe
catch a tiger by the toe 
if he hollers let him go 
# names fr
am stram gram
pique et colegram
bourre ratatam
# names nl 
iene miene mutte
tien pond grutten
kaas is de baas
# names de
eene meene muh und raus bist du 
maus meck weg 
noch lange nicht 
sag mir erst wie alt\
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


