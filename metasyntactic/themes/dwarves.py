# -*- coding: utf-8 -*-
'''
.. highlight:: perl


############################
Acme::MetaSyntactic::dwarves
############################

****
NAME
****


Acme::MetaSyntactic::dwarves - The seven dwarves theme


***********
DESCRIPTION
***********


Snow-White seven dwarves.


************
CONTRIBUTORS
************


Antoine Hulin (January 2005).
Proposed again by Abigail (October 2005).
Proposed yet again by Xavier Caron (October 2005).

I definitely \ *had*\  to include this list! \ ``:-)``\ 

Introduced in version 0.48, published on November 14, 2005.

Updated by Abigail (added Danish, German, Spanish, Finnish, Hungarian,
Italian, Norwegian, Portuguese and Swedish) in version 0.74, published
on May 15, 2006.


********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::Locale <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aLocale&mode=module>`_.
'''

name = 'dwarves'
DATA = '''\
# default
en
# names da
Brille     Lystig      Gnavpot     Dumpe       Sovnig      Prosit      Flovmand
# names de
Chef       Happy       Brummbar    Seppl       Schlafmutz  Hatschi     Pimpel
# names en
Doc        Happy       Grumpy      Dopey       Sleepy      Sneezy      Bashfull
# names es
Sabio      Feliz       Grunon      Tontin      Dormilon    Alergico    Romantico
# names fi
Viisas     Lystikas    Joro        Vilkas      Unelias     Nuhanena    Ujo
# names fr
Prof       Joyeux      Grincheux   Simplet     Dormeur     Atchoum     Timide
# names hu
Tudor      Vidor       Morgo       Kuka        Szundi      Hapci       Szende
# names it
Dotto      Gongolo     Brontolo    Cucciolo    Pisolo      Eolo        Mammolo
# names no
Brille     Lystig      Sinnataggen Minsten     Sovnig      Prosit      Blygen
# names pt
Mestre     Feliz       Zangado     Dunga       Soneca      Atchim      Dengoso
# names sv
Kloker     Glader      Butter      Toker       Trotter     Prosit      Blyger\
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


