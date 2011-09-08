# -*- coding: utf-8 -*-
'''
.. highlight:: perl


###############################
Acme::MetaSyntactic::good_omens
###############################

****
NAME
****


Acme::MetaSyntactic::good_omens - The Good Omens theme


***********
DESCRIPTION
***********


This list gives the names of the characters from
Neil Gaiman and Terry Pratchett's novel, \ *Good Omens*\ .

Source: \ *Good Omens*\ 

A Narrative of Certain Events occurring in the
last eleven years of human history, in strict accordance as shall
be shewn with:

\ *The Nice and Accurate Prophecies of Agnes Nutter*\ 

Compiled and edited, with Footnotes of an Educational Nature
and Precepts for the Wise,
by Neil Gaiman and Terry Pratchett.


*****************
DRAMATIS PERSONAE
*****************


SUPERNATURAL BEINGS
===================



God
 
 God
 


Metatron
 
 The Voice of God
 


Aziraphale
 
 An angel, and part-time rare book dealer
 


Satan
 
 A Fallen Angel; the Adversary
 


Beelzebub
 
 A Likewise Fallen Angel and Prince of Hell
 


Hastur
 
 A Fallen Angel and Duke of Hell
 


Ligur
 
 Likewise a Fallen Angel and Duke of Hell
 


Crowley
 
 An Angel who did not so much Fall as Saunter Vaguely Downwards
 



APOCALYPTIC HORSEPERSONS
========================



DEATH
 
 Death
 


War
 
 War
 


Famine
 
 Famine
 


Pollution
 
 Pollution
 



HUMANS
======



Thou-Shalt-Not-Commit-Adultery Pulsifer
 
 A Witchfinder
 


Agnes Nutter
 
 A Prophetess
 


Newton Pulsifer
 
 Wages Clerk and Witchfinder Private
 


Anathema Device
 
 Practical Occultist and Professional Descendant
 


Shadwell
 
 Witchfinder Sergeant
 


Madame Tracy
 
 Painted Jezebel [mornings only, Thursdays by arrangement] and Medium
 


Sister Mary Loquacious
 
 A Satanic Nun of the Chattering Order of St. Beryl
 


Mr Young
 
 A Father
 


Mr Tyler
 
 A Chairman of a Residents' Association
 


A Delivery Man




THEM
====



ADAM
 
 An Antichrist
 


Pepper
 
 A Girl
 


Wensleydale
 
 A Boy
 


Brian
 
 A Boy
 


Full Chorus of Tibetans, Aliens, Americans, Atlanteans and other rare and strange Creatures of the Last Days.


AND
===



Dog
 
 Satanical hellhound and cat-worrier
 




***********
CONTRIBUTOR
***********


Jean Forget.

Introduced in version 0.97, published on October 23, 2006.


********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'good_omens'
DATA = '''\
\
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


