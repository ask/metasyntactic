# -*- coding: utf-8 -*-
'''

##########################
Acme::MetaSyntactic::tarot
##########################

****
NAME
****


Acme::MetaSyntactic::tarot - Tarot cards


***********
DESCRIPTION
***********


Tarot decks consist of 78 different cards - a 22 card \ *Major Arcana*\ ,
and 4 14-card suits forming the \ *Minor Arcana*\ . The suits in the
minor arcana as \ *Wands*\ , \ *Cups*\ , \ *Swords*\  and \ *Pentacles*\ . Ranks
start with \ *Ace*\ , then go from 2 to 10 inclusive, then \ *Page*\ ,
\ *Knight*\ , \ *Queen*\  and \ *King*\ . In the Major Arcana, we find:
\ *Fool*\ , \ *Magician*\ , \ *High Priestess*\ , \ *Empress*\ , \ *Emperor*\ ,
\ *Hierophant*\ , \ *Lovers*\ , \ *Chariot*\ , \ *Strength*\ , \ *Hermit*\ ,
\ *Wheel of Fortune*\ , \ *Justice*\ , \ *Hanged Man*\ , \ *Death*\ , \ *Temperance*\ ,
\ *Devil*\ , \ *Tower*\ , \ *Star*\ , \ *Moon*\ , \ *Sun*\ , \ *Judgement*\ , and finally,
\ *World*\ .

Source: `http://www.learntarot.com/ <http://www.learntarot.com/>`_


***********
CONTRIBUTOR
***********


Abigail


*******
CHANGES
*******



- \*
 
 2012-06-11 - v1.000
 
 Introduced in Acme-MetaSyntactic-Themes version 1.005.
 


- ,\*
 
 2005-11-01
 
 Submitted by Abigail.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'tarot'
DATA = '''\
# names
Fool Magician High_Priestess Empress Emperor Hierophant Lovers
Chariot Strength Hermit Wheel_of_Fortune Justice Hanged_Man Death
Temperance Devil Tower Star Moon Sun Judgement World
Wand Cup Sword Pentacle Page Knight Queen King Ace\
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


