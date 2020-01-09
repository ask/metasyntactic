# -*- coding: utf-8 -*-
'''

#########################
Acme::MetaSyntactic::lotr
#########################

****
NAME
****


Acme::MetaSyntactic::lotr - The Lord of the Rings theme


***********
DESCRIPTION
***********


Many characters of J. R. R. Tolkien's \ *Lord of the Rings*\  bear several
names. This theme collects some of the main characters names.

The names of Sauron, Gandalf and Aragorn come from Robert Foster's \ *Complete Guide to Middle-Earth*\ .
Turin's names were found in \ *The Silmarillion*\ .


***********
CONTRIBUTOR
***********


Jean Forget


*******
CHANGES
*******



- \*
 
 2012-05-07 - v1.000
 
 Received its own version number in Acme-MetaSyntactic-Themes version 1.000.
 


- \*
 
 2006-06-19
 
 Introduced in Acme-MetaSyntactic version 0.79.
 


- \*
 
 2005-09-12
 
 Jean Forget provided the names of Turin and Sauron.
 


- \*
 
 2005-08-05
 
 Jean Forget provided the idea for the theme,
 along with the names of Gandalf and Aragorn.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::MultiList <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aMultiList&mode=module>`_.
'''

name = 'lotr'
DATA = '''\
# default
sauron
# names sauron
Sauron
Thauron
Gorthaur_the_Cruel
Sauron_the_Deceiver
the_Lord_of_the_Earth
the_Enemy
the_Master
the_Dark_Power
the_Dark_Lord
the_Lord_of_Mordor
the_Dark_Lord_of_Mordor
the_Power_of_the_Black_Land
the_Black_Master
the_Black_One
the_Lord_of_Barad_dur
the_Lord_of_the_Dark_Tower
the_Shadow
the_Great_Eye
the_Red_Eye
the_Eye_of_Barad_dur
the_Lidless_Eye
the_Evil_Eye
the_Nameless
the_Nameless_One
the_Nameless_Eye
He
Him
the_Lord_of_the_Ring
the_Lord_of_the_Rings
the_Ring_Maker
the_Black_Hand
# names gandalf
Gandalf
Mithrandir
Grey_Wanderer
Grey_Pilgrim
Tharkun
Incanus
Gandalf_Greyhame
Stormcrow
Lathspell
the_Grey_Fool
the_Enemy_of_Sauron
the_White_Rider
Olorin
# names aragorn
Aragorn
Elessar
Elfstone
Strider
Telcontar
Isildur_s_Heir
the_Renewer
Longshanks
Wing_foot
# names turin
Turin
Neithian
Gorthol
Argwaen_son_of_Urmarth
Adanedhel
Mormegil
Wildman_of_the_Woods
Turambar
Dagnir_Glaurunga\
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


