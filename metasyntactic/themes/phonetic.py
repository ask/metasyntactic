# -*- coding: utf-8 -*-
'''
.. highlight:: perl


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


***********
CONTRIBUTOR
***********


Michel Rodriguez provided the first list (NATO official phonetic alphabet).

Added Swahili and English on request of David Landgren, thus closing
RT ticket #14276.
While I was at it, I also added French, German and Italian.

Introduced in version 0.08, published on February 7, 2005.

Updated to handle multilingual phonetics in version 0.38,
published on September 5, 2005.

Updated (German fix by Gisbert W. Selke) in version 0.74, published on
May 15, 2006.

Updated with the Dutch list by Abigail in version 0.91, published on
September 11, 2006.


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
alpha   bravo charlie  delta echo foxtrot golf  hotel  india juliet  kilo
lima    mike  november oscar papa quebec  romeo sierra tango uniform victor
whiskey xray  yankee   zulu
# names en
Able Baker Charlie Dog   Edward Fox   George How  Item  Jiga   King    Love
Mike Nan   Oboe   Peter  Queen  Roger Sugar  Tape Uncle Victor William X_Ray
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


