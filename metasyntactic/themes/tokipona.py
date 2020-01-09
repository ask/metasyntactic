# -*- coding: utf-8 -*-
'''

#############################
Acme::MetaSyntactic::tokipona
#############################

****
NAME
****


Acme::MetaSyntactic::tokipona - Words from the Toki Pona language


***********
DESCRIPTION
***********


Toki Pona is a constructed language, with little more than a hundred words.
This theme has them all.

See `http://www.tokipona.org/ <http://www.tokipona.org/>`_.


************
CONTRIBUTORS
************


Abigail, Philippe Bruhat (BooK)


*******
CHANGES
*******



- \*
 
 2014-08-18 - v1.001
 
 Picked a new link (still from the official web site) from which to
 get the official word list, and updated from the source web site
 in Acme-MetaSyntactic-Themes version 1.041.
 


- \*
 
 2012-08-20 - v1.000
 
 Updated from remote site, and
 published in Acme-MetaSyntactic-Themes 1.015.
 


- \*
 
 2012-06-26
 
 Added a remote list (from the official web site).
 


- \*
 
 2005-11-19
 
 Submitted by Abigail.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'tokipona'
DATA = '''\
# names
a akesi ala alasa ale ali anpa ante anu awen
e en esun
ijo ike ilo insa
jaki jan jelo jo
kala kalama kama kasi ken kepeken kili kin kipisi kiwen ko kon kule kulupu kute
la lape laso lawa len lete li lili linja lipu loje lon luka lukin lupa
ma mama mani meli mi mije moku moli monsi mu mun musi mute
namako nanpa nasa nasin nena ni nimi noka
o oko olin ona open
pakala pali palisa pan pana pata pi pilin pimeja pini pipi poka poki pona
sama seli selo seme sewi sijelo sike sin sina sinpin sitelen sona soweli suli suno supa suwi
tan taso tawa telo tenpo toki tomo tu
unpa uta utala
walo wan waso wawa weka wile\
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


