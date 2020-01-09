# -*- coding: utf-8 -*-
'''

#############################
Acme::MetaSyntactic::alphabet
#############################

****
NAME
****


Acme::MetaSyntactic::alphabet - Learn your ABC in various languages


***********
DESCRIPTION
***********


Various alphabets, transliterated if the latin alphabet doesn't fit.

I've found most of the transliterations on the Internet, which may
be wrong. Please correct me.


***********
CONTRIBUTOR
***********


Philippe "BooK" Bruhat.


***************
ACKNOWLEDGMENTS
***************


Thanks to Estelle Souche for help with the Yiddish Alef-Beys.


*******
CHANGES
*******



- \*
 
 2012-05-07 - v1.000
 
 Updated with small fixes for category \ ``nato``\  (see RT #50160), and
 received its own version number in Acme-MetaSyntactic-Themes version 1.000.
 


- \*
 
 2005-05-09
 
 Introduced in Acme-MetaSyntactic version 0.21.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::Locale <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aLocale&mode=module>`_.
'''

name = 'alphabet'
DATA = '''\
# default
en
# names en
a b c d e f g h i j k l m n o p q r s t u v w x y z
# names it
a b c d e f g h i     l m n o p q r s t u v       z
# names la
a b c d e f   h i   k l m n o p q r s t   v   x
# names he
aleph bet gimmel dalet  hey vav    zayin chet tet  yod kaf
lamed mem nun    samech pay tsadie qof   resh shin tav
# names yi
alef  beys giml daled  hey  vov zayen  khes tes   yud  kof
lamed mem  nun  samekh ayen pey tsadik kuf  reysh shin tov
# names gr
alpha beta gamma   delta epsilon zeta  eta theta   iota kappa lambda mu
nu    xi   omicron pi    rho     sigma tau upsilon phi  chi   psi    omega
# names nato
alfa    bravo charlie  delta echo foxtrot golf  hotel  india juliett kilo
lima    mike  november oscar papa quebec  romeo sierra tango uniform victor
whiskey xray  yankee   zulu
# names ja
a  i   u   e  o
ka ki  ku  ke ko
sa shi su  se so
ta chi tsu te to
na ni  nu  ne no
ha hi  fu  he ho
ma mi  mu  me mo
ya     yu     yo    
ra ri  ru  re ro
wa wi      we wo  
              n\
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


