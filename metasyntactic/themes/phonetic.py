# -*- coding: utf-8 -*-
'''

#############################
Acme::MetaSyntactic::phonetic
#############################

****
NAME
****


Acme::MetaSyntactic::phonetic - The phonetic theme


***********
DESCRIPTION
***********


Several phonetic alphabets.

Most of them come from this list:
`http://montgomery.cas.muohio.edu/meyersde/PhoneticAlphabets.htm <http://montgomery.cas.muohio.edu/meyersde/PhoneticAlphabets.htm>`_


************
CONTRIBUTORS
************


Michel Rodriguez, Philippe Bruhat (BooK), David Landgren, Gisbert W. Selke,
Abigail, Olivier Mengu, Jean Forget.


*******
CHANGES
*******



- \*
 
 2012-05-07 - v1.000
 
 Updated with small fixes for categories \ ``x-nato``\  and \ ``en``\ , and
 received its own version number in Acme-MetaSyntactic-Themes version 1.000.
 


- \*
 
 2012-04-26
 
 Jean Forget requested that "tare" is used instead of "tare" for the
 English list (RT #50160).
 


- \*
 
 2009-10-01
 
 Olivier Mengu spotted a typo in the \ ``x-nato``\  list (RT #50160).
 


- \*
 
 2006-09-11
 
 Updated in Acme-MetaSyntactic version 0.91.
 


- \*
 
 2006-09-10
 
 Abigail sent a patch adding the Dutch list.
 


- \*
 
 2006-05-15
 
 Updated in Acme-MetaSyntactic version 0.74.
 


- \*
 
 2006-05-10
 
 Gisbert W. Selke sent a fix for the German version.
 


- \*
 
 2005-09-05
 
 Updated to handle multilingual phonetics in Acme-MetaSyntactic version 0.38
 While I was at it, I also added French, German and Italian.
 


- \*
 
 2005-08-23
 
 David Landgren requested Swahili and English (RT #14276).
 


- \*
 
 2005-02-07
 
 Introduced in Acme-MetaSyntactic version 0.08.
 


- \*
 
 2005-01-16
 
 Michel Rodriguez provided the first list (NATO official phonetic alphabet).
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::Locale <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aLocale&mode=module>`_.
'''

name = 'phonetic'
DATA = '''\
# default
x-nato
# names x-nato
alfa    bravo charlie  delta echo foxtrot golf  hotel  india juliett kilo
lima    mike  november oscar papa quebec  romeo sierra tango uniform victor
whiskey xray  yankee   zulu
# names en
Able Baker Charlie Dog   Edward Fox   George How  Item  Jiga   King    Love
Mike Nan   Oboe   Peter  Queen  Roger Sugar  Tare Uncle Victor William X_Ray
Yoke Zebra
# names sw
Ali    Banda  Chakechake Dodoma Entebe Fumba Gogo Homa Imba   Jambo KenyaLala
Mama   Nakuru Ona        Punda  Kyela  Rangi Simu Tatu Uganda Vitu  Wali
Eksrei Yai    Zanzibar
# names fr
Anatole Berthe Celestin Desire  Eugene  Emile  Francois Gaston Henri Irma
Joseph  Kleber Louis    Marcel  Nicolas Oscar  Pierre  Quintal Raoul Suzanne
Therese Ursule Victor   William Xavier  Yvonne Zoe
# names de
Anton     Bertha Caesar  Dora   Emil    Friedrich Gustav    Heinrich Ida
Jakob     Konrad Ludwig  Martha Nordpol Otto      Paula     Quelle   Richard
Siegfried Schule Theodor Ulrich Viktor  Wilhelm   Xanthippe Ypsilon  Zeppelin
# names it
Ancona Bologna Como    Domodossola Empoli Firenze  Genova Hacca        Imola
Jolly  Kappa   Livorno Milano      Napoli Otranto  Pisa   Quartomiglio Roma
Savona Torino  Udine   Venezia     Wagner Xilofono York   Zara
# names nl
Anna    Anton    Bernard Cornelis Dirk     Eduard   Ferdinand Gerard
Hendrik Izaak    Jan     Karel    Lodewijk Marie    Nico      Otto
Pieter  Quotient Rudolf  Simon    Teunis   Theodoor Utrecht   Victor
Willem  Xantippe Ypsilon IJsbrand Zaandam\
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


