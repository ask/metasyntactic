# -*- coding: utf-8 -*-
'''
.. highlight:: perl


#########################
Acme::MetaSyntactic::yapc
#########################

****
NAME
****


Acme::MetaSyntactic::yapc - The YAPC theme


***********
DESCRIPTION
***********


This theme lists all the places that have held YAPC (Yet Another Perl
Conference).

Details
=======


The various YAPC are:


YAPC::America::North
 
 Pittsburgh (1999, 2000), Montreal (2001), Saint-Louis (2002),
 Boca Raton (2003), Buffalo (2004), Toronto (2005), Chicago (2006),
 Houston (2007).
 


YAPC::Europe
 
 London (2000),  Amsterdam (2001), Munich (2002), Paris (2003),
 Belfast (2004), Braga (2005), Birmingham (2006), Vienna (2007).
 


YAPC::Israel
 
 Haifa (2003),  Herzliya (2004, 2005), Netanya (2006).
 


YAPC::Canada
 
 Ottawa (2003).
 


YAPC::Australia
 
 Melbourne (2004, 2005, 2006).
 


YAPC::Taipei
 
 Taipei (2004, 2005).
 


YAPC::Brazil
 
 Porto Alegre (2005).
 


YAPC::Asia
 
 Tokyo (2006, 2007).
 


YAPC::America::South
 
 São Paulo (2006).
 




***********
CONTRIBUTOR
***********


Mark Fowler asked me for this list during YAPC::Europe 2005.

Introduced in version 0.40, published on September 19, 2005.

Updated by Abigail in version 0.47, published on November 7, 2005.

Updated in version 0.49, published on November 21, 2005.

Updated in version 0.59, published on January 30, 2006.

Updated with the YAPC for 2007 in version 0.90, published on September 4, 2006.

Updated with several other 2006 and 2007 YAPC, and turned into a
MultiList by Abigail in version 0.91, published on September 11, 2006.


********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::MultiList <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aMultiList&mode=module>`_.
'''

name = 'yapc'
DATA = '''\
# default
:all
# names america north
Pittsburgh Montreal Saint_Louis Boca_Raton Buffalo Toronto Chicago Houston
# names europe
London Amsterdam Munich Paris Belfast Braga Birmingham Vienna
# names israel
Haifa Herzliya Netanya
# names canada
Ottawa
# names australia
Melbourne
# names taipei
Tai_Pei
# names brazil
Porto_Alegre
# names asia
Tokyo
# names america south
Sao_Paulo\
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


