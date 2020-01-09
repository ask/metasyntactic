# -*- coding: utf-8 -*-
'''

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


Antoine Hulin, Abigail, Xavier Caron.


*******
CHANGES
*******



- \*
 
 2013-12-09 - v1.002
 
 Updated to fix a misspelling in Bashful's name (English),
 in Acme-MetaSyntactic-Themes version 1.038.
 


- \*
 
 2012-05-14 - v1.001
 
 Updated by Abigail (added Irish Gaelic and Croatian)
 in Acme-MetaSyntactic-Themes version 1.001.
 


- \*
 
 2012-05-07 - v1.000
 
 Received its own version number in Acme-MetaSyntactic-Themes version 1.000.
 


- \*
 
 2006-05-15
 
 Updated by Abigail (added Danish, German, Spanish, Finnish, Hungarian,
 Italian, Norwegian, Portuguese and Swedish) in Acme-MetaSyntactic version 0.74.
 


- \*
 
 2005-11-14
 
 Introduced in Acme-MetaSyntactic version 0.48.
 


- \*
 
 2005-10-28
 
 English and French lists proposed by Xavier Caron.
 
 I definitely \ *had*\  to include this list! \ ``:-)``\ 
 


- \*
 
 2005-10-23
 
 Submitted as a simple list of English names by Abigail.
 


- \*
 
 2005-01-30
 
 Initial lists (French and English) proposed by Antoine Hulin.
 



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
Doc        Happy       Grumpy      Dopey       Sleepy      Sneezy      Bashful
# names es
Sabio      Feliz       Grunon      Tontin      Dormilon    Alergico    Romantico
# names fi
Viisas     Lystikas    Joro        Vilkas      Unelias     Nuhanena    Ujo
# names fr
Prof       Joyeux      Grincheux   Simplet     Dormeur     Atchoum     Timide
# names ga
Saoi       Sonai       Cancran     Simpleoir   Codlatan    Sraothachan Cuthalachan
# names hr
Uco        Srecko      Ljutko      Glupko      Pospanko    Kihavko     Stidljivko
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


