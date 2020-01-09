# -*- coding: utf-8 -*-
'''

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


- YAPC::America::North
 
 Pittsburgh (1999, 2000), Montreal (2001), Saint-Louis (2002),
 Boca Raton (2003), Buffalo (2004), Toronto (2005), Chicago (2006),
 Houston (2007), Chicago (2008), Pittsburgh (2009), Columbus (2010),
 Asheville (2011), Madison (2012), Austin (2013), Orlando (2014),
 Salt Lake City (2015).
 


- YAPC::Europe
 
 London (2000),  Amsterdam (2001), Munich (2002), Paris (2003),
 Belfast (2004), Braga (2005), Birmingham (2006), Vienna (2007),
 Copenhagen (2008), Lisbon (2009), Pisa (2010), Rīga (2011),
 Frankfurt (2012), Kyiv (2013), Sofia (2014), Granada (2015).
 


- YAPC::Israel
 
 Haifa (2003),  Herzliya (2004, 2005).
 
 In 2006, YAPC::Israel became OSDC::Israel.
 


- YAPC::Canada
 
 Ottawa (2003).
 


- YAPC::Australia
 
 Melbourne (2004).
 
 The first YAPC::Australia was held as part of OSDC (.au) 2004 in Melbourne,
 and has been held jointly thereafter.
 


- YAPC::Brazil
 
 Porto Alegre (2005-2006), São Paulo (2007, 2008), Rio de Janeiro (2009),
 Fortaleza (2010), Rio de Janeiro (2011), São Paulo (2012), Curitiba (2013).
 


- YAPC::Taipei
 
 Taipei (2004, 2005).
 
 YAPC Taipei became YAPC::Asia in 2006.
 


- YAPC::Asia
 
 Tokyo (2006-2014).
 


- YAPC::America::South
 
 São Paulo (2006), Porte Alegre (2007-2009).
 
 This conference was held in conjunction with CONISLI
 (Congresso Internacional de Software Livre).
 


- YAPC::Russia
 
 Moscow (2008-2009), Kiev (2010), Moscow (2011), Kiev (2012).
 




*****
NOTES
*****


Kiev and Kyiv are names for the same city. For YAPC::Russia, the name
Kiev is used, as this is the romanization of the Russian name for the
capital of Ukraine; however, for YAPC::Europe 2013, we opted for using
the romanization of name in modern Ukrainian.


************
CONTRIBUTORS
************


Mark Fowler, Philippe Bruhat (BooK), Abigail.


*******
CHANGES
*******



- \*
 
 2014-10-13 - v1.004
 
 Updated with various locations for 2014 and 2015
 in Acme-MetaSyntactic-Themes version 1.043.
 


- \*
 
 2013-07-29 - v1.003
 
 Updated by Abigail with the locations for YAPC::NA and YAPC::Brazil for 2013
 in Acme-MetaSyntactic-Themes version 1.035.
 


- \*
 
 2012-08-27 - v1.002
 
 Updated by Abigail with the locations for YAPC::Europe, YAPC::NA for 2013,
 as well as the locations of past YAPC::Russia,
 in Acme-MetaSyntactic-Themes version 1.016.
 


- \*
 
 2012-05-14 - v1.001
 
 Updated with an \ ``=encoding``\  pod command
 in Acme-MetaSyntactic-Themes version 1.001.
 


- \*
 
 2012-05-07 - v1.000
 
 Updated with all YAPC since 2007, and
 received its own version number in Acme-MetaSyntactic-Themes version 1.000.
 


- \*
 
 2006-09-11
 
 Updated with several other 2006 and 2007 YAPC, and turned into a
 MultiList by Abigail in Acme-MetaSyntactic version 0.91.
 


- \*
 
 2006-09-04
 
 Updated with the YAPC for 2007 in Acme-MetaSyntactic version 0.90.
 


- \*
 
 2006-01-30
 
 Updated in Acme-MetaSyntactic version 0.59.
 


- \*
 
 2005-11-21
 
 Updated in Acme-MetaSyntactic version 0.49.
 


- \*
 
 2005-11-07
 
 Updated by Abigail in Acme-MetaSyntactic version 0.47.
 


- \*
 
 2005-09-19
 
 Introduced in Acme-MetaSyntactic version 0.40.
 


- \*
 
 Mark Fowler asked me for this list during YAPC::Europe 2005 in Braga, Portugal.
 



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
Chicago Pittsburgh Columbus Asheville Madison Austin Orlando Salt_Lake_City
# names europe
London Amsterdam Munich Paris Belfast Braga Birmingham Vienna Copenhagen
Lisbon Pisa Riga Frankfurt Kiev Sofia Granada
# names israel
Haifa Herzliya
# names canada
Ottawa
# names australia
Melbourne
# names taipei
Taipei
# names brazil
Porto_Alegre Sao_Paulo Rio_de_Janeiro Fortaleza Rio_de_Janeiro Sao_Paulo
Curitiba
# names asia
Tokyo
# names america south
Sao_Paulo Porto_Alegre
# names russia
Moscow Kiev Moscow Kiev\
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


