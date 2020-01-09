# -*- coding: utf-8 -*-
'''

###########################
Acme::MetaSyntactic::zodiac
###########################

****
NAME
****


Acme::MetaSyntactic::zodiac - The zodiac theme


***********
DESCRIPTION
***********


Zodiacal signs from various parts of the world.

In Western and Vedic astonomy (and astrology), zodiacal signs are
constellations in front of which the sun passes, as seen from earth.
Traditional Western zodiac signs are based on the Babylonian observations,
and contain 12 signs. However, these observations are three millenia
out of date, and in reality, the sun passes in front of thirteen
constellation.

This theme has four categories:


- Western/Tradional
 
 Contains the twelve signs most people are familiar with.
 This is the default category.
 


- Western/Real
 
 The thirteen constellations the sun actually passes in front of.
 


- Vedic
 
 The names of the constellations as they are known in India.
 


- Chinese
 
 The signs of the Chines zodiac. They have no relation with constellations.
 


Default category is \ *Western/Traditional*\ .


***********
CONTRIBUTOR
***********


Abigail


*******
CHANGES
*******



- \*
 
 2012-05-07 - v1.000
 
 Included with its own version number
 in Acme-MetaSyntactic-Themes version 1.000.
 


- \*
 
 2006-05-13
 
 Submitted by Abigail.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::MultiList <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aMultiList&mode=module>`_.
'''

name = 'zodiac'
DATA = '''\
# default 
Western/Traditional
# names Western Traditional
Aries Taurus Gemini Cancer Leo Virgo Libra Scorpio
Sagittarius Capricornus Aquarius Pisces
# names Western Real
Aries Taurus Gemini Cancer Leo Virgo Libra Scorpio Ophiuchus
Sagittarius Capricornus Aquarius Pisces
# names Vedic
Mesha Vrishabha Mithuna Karka Simha Kanya Tula Vrishchika Dhanus
Makara Kumbha Meena
# names Chinese
Rat Ox Tiger Rabbit Dragon Snake Horse Goat Monkey Rooster Dog Boar\
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


