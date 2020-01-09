# -*- coding: utf-8 -*-
'''

############################
Acme::MetaSyntactic::planets
############################

****
NAME
****


Acme::MetaSyntactic::planets - The planets theme


***********
DESCRIPTION
***********


The nine planets of our solar system.

The status of the newly discovered Kuiper belt object (2003 UB313) is
still not determined (and therefore, not officially named), and hence,
not classified as a planet.

Pluto is not a planet any more.


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
 
 2006-08-28
 
 Updated to remove Pluto in Acme-MetaSyntactic version 0.89.
 


- \*
 
 2006-05-15
 
 Updated to 42 languages by Abigail in Acme-MetaSyntactic version 0.74.
 


- \*
 
 2006-05-08
 
 Made multilingual in Acme-MetaSyntactic version 0.73.
 


- \*
 
 2006-02-27
 
 Introduced in Acme-MetaSyntactic version 0.63.
 


- \*
 
 2005-10-27
 
 Submitted by Abigail.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::Locale <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aLocale&mode=module>`_.
'''

name = 'planets'
DATA = '''\
# default
en
# names af
Mercurius Venus Aarde Mars Jupiter Saturnus Uranus Neptunus
# names als
Merkur Venus Erde Mars Jupiter Saturn Uranus Neptun
# names bs
Merkur Venera Zemlja Mars Jupiter Saturn Uran Neptun
# names ca
Mercuri Venus Terra Mart Jupiter Saturn Ura Neptu
# names da
Merkur Venus Jorden Mars Jupiter Saturn Uranus Neptun
# names de
Merkur Venus Erde Mars Jupiter Saturn Uranus Neptun
# names en
Mercury Venus Earth Mars Jupiter Saturn Uranus Neptune
# names eo
Merkuro Venuso Tero Marso Jupitero Saturno Urano Neptuno
# names es
Mercurio Venus Tierra Marte Jupiter Saturno Urano Neptuno
# names et
Merkuur Veenus Maa Marss Jupiter Saturn Neptuun Uraan
# names eu
Mercurius Artizar Lurra Mars Jupiter Saturno Uranus Neptuno
# names fi
Merkurius Venus Maa Mars Jupiter Saturnus Uranus Neptunus
# names fr
Mercure Venus Terre Mars Jupiter Saturne Uranus Neptune
# names fur
Mercuri Bielestele Tiere Mart Gjiove Saturni Nettun Uran
# names gl
Mercurio Venus Terra Marte Xupiter Saturno Urano Neptuno
# names hr
Merkur Venera Zemlja Mars Jupiter Saturn Uran Neptun
# names hu
Merkur Venusz Fold Mars Jupiter Szaturnusz Uranusz Neptunusz
# names ia
Mercurio Venus Terra Marte Jupiter Saturno Urano Neptuno
# names id
Merkurius Venus Bumi Mars Jupiter Saturnus Neptunus Uranus
# names it
Mercurio Venere Terra Marte Giove Saturno Uranio Nettuno
# names ku
Tir Gelawej Erd Behram Bercis Keywan Uranus Neptun
# names kw
Mergher Gwener Norvys Meurth Yow Sadorn Ouranos Nevyon
# names la
Mercurius Venus Terra Mars Iuppiter Saturnus Uranus Neptunus
# names lb
Merkur Venus Aerd Mars Jupiter Saturn Uranus Neptun
# names lt
Merkurijus Venera Zeme Marsas Jupiteris Saturnas Uranas Neptunas
# names ms
Utarid Zuhrah Bumi Marikh Musytari Zuhal Uranus Neptun
# names mt
Merkurju Venere Dinja Marte Gove Saturnu Uranju Nettunu
# names nap
Mercurio Venere Terra Marte Giove Saturno Urano Nettuno
# names nds
Merkur Venus Eer Mars Jupiter Saturn Uranus Neptun
# names nl
Mercurius Venus Aarde Mars Jupiter Saturnus Uranus Neptunus
# names nn
Merkur Venus Jorda Mars Jupiter Saturn Uranus Neptun
# names no
Merkur Venus Jorden Mars Jupiter Saturn Uranus Neptun
# names nrm
Mertchure Venus Terre Mars Jupiter Saturne Uranus Nepteune
# names pam
Mercury Venus Yatu Jupiter Saturn Uranus Neptune
# names pl
Merkury Wenus Ziemia Mars Jowisz Saturn Uran Neptun
# names pt
Mercurio Venus Terre Marte Jupiter Saturno Urano Netuno
# names ro
Mercur Venus Pamant Marte Jupiter Saturn Uranus Neptun
# names scn
Mercuriu Veniri Terra Marti Giovi Saturnu Uranu Nettunu
# names sh
Merkur Venera Zemlja Mars Jupiter Saturn Uran Neptun
# names sv
Merkurius Venus Jorden Mars Jupiter Saturnus Uranus Neptunus
# names tl
Merkuryo Venus Daigdig Marte Jupiter Saturno Urano Neptuno
# names tpi
Makuri Vinas Graun Mas Jupita Saten Yuranas Neptun
# names tr
Merkur Venus Yer Mars Jupiter Saturn Uranus Neptun\
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


