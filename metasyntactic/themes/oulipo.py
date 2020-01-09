# -*- coding: utf-8 -*-
'''

###########################
Acme::MetaSyntactic::oulipo
###########################

****
NAME
****


Acme::MetaSyntactic::oulipo - The Oulipo theme


***********
DESCRIPTION
***********


This theme contains the initials of the members of the French literary
group Oulipo, created by Raymond Queneau (RQ) and Franois Le Lionnais
(FLL) in 1960. These initials are commonly used in place of a member's
full name.

See the official Oulipo web site at `http://www.oulipo.net/ <http://www.oulipo.net/>`_.

Members
=======



- \*
 
 Nol ARNAUD (1919-2003), founding member.
 


- \*
 
 Michle AUDIN (1954-), joined in 2009.
 


- \*
 
 Valrie BEAUDOUIN (1968-), joined in 2003.
 


- \*
 
 Marcel BNABOU (1939-), joined in 1970.
 


- \*
 
 Jacques BENS (1931-2001), founding member.
 


- \*
 
 Claude BERGE (1926-2002), founding member.
 


- \*
 
 Eduardo BERTI (1964-), joined in 2014.
 


- \*
 
 Andr BLAVIER (1922-2001), foreign correspondent.
 


- \*
 
 Paul BRAFFORT (1923-), joined in 1961.
 


- \*
 
 Italo CALVINO (1923-1985), joined in 1974.
 


- \*
 
 Franois CARADEC (1924-2008), joined in 1983.
 


- \*
 
 Bernard CERQUIGLINI (1947-), joined in 1995.
 


- \*
 
 Ross CHAMBERS (1932-), joined in 1961.
 


- \*
 
 Stanley CHAPMAN (1925-2009), joined in 1961.
 


- \*
 
 Marcel DUCHAMP (1887-1968), joined in 1962.
 


- \*
 
 Jacques DUCHATEAU (1929-), founding member.
 


- \*
 
 Luc ETIENNE (1908-1984), joined in 1970.
 


- \*
 
 Frdric FORTE (1973-), joined in 2005.
 


- \*
 
 Paul FOURNEL (1947-), joined in 1972.
 


- \*
 
 Anne F. GARRTA (1962-), joined in 2000.
 


- \*
 
 Michelle GRANGAUD (1941-), joined in 1995.
 


- \*
 
 Jacques JOUET (1947-), joined in 1983.
 


- \*
 
 LATIS (1913-1973), founding member.
 


- \*
 
 Franois LE LIONNAIS (1901-1984), founder.
 


- \*
 
 Herv LE TELLIER (1957-), joined in 1992.
 


- \*
 
 tienne LCROART (1960-), joined in 2012.
 


- \*
 
 Jean LESCURE (1912-2005), founding member.
 


- \*
 
 Daniel LEVIN BECKER (1984-), joined in 2009.
 


- \*
 
 Pablo MARTN SNCHEZ (1977-), joined in 2014.
 


- \*
 
 Harry MATHEWS (1930-), joined in 1973.
 


- \*
 
 Michle MTAIL (1950-), joined in 1975.
 


- \*
 
 Ian MONK (1960-), joined in 1998.
 


- \*
 
 Oskar PASTIOR (1927-2006), joined in 1992.
 


- \*
 
 Georges PEREC (1936-1982), joined in 1967.
 


- \*
 
 Raymond QUENEAU (1903-1976), founder.
 


- \*
 
 Jean QUEVAL (1913-1990), founding member.
 


- \*
 
 Pierre ROSENSTIEHL (1933-), joined in 1992.
 


- \*
 
 Jacques ROUBAUD (1932-), joined in 1966.
 


- \*
 
 Olivier SALON (1955-), joined in 2000.
 


- \*
 
 Albert-Marie SCHMIDT (1901-1966), founding member.
 




***********
CONTRIBUTOR
***********


Philippe "BooK" Bruhat, co-creator (with Estelle Souche) of
the first Oulipo web site, back in 1995.


*******
CHANGES
*******



- \*
 
 2014-09-15 - v1.003
 
 Updated with two new members,
 added the date each member joined the group,
 in Acme-MetaSyntactic-Themes version 1.042.
 


- \*
 
 2012-10-08 - v1.002
 
 Updated with a new member,
 added the list of Oulipo member names (with activity dates),
 in Acme-MetaSyntactic-Themes version 1.022.
 


- \*
 
 2012-05-14 - v1.001
 
 Updated with an \ ``=encoding``\  pod command
 in Acme-MetaSyntactic-Themes version 1.001.
 


- \*
 
 2012-05-07 - v1.000
 
 Updated with the new Oulipo members since 2007, and
 received its own version number in Acme-MetaSyntactic-Themes version 1.000.
 


- \*
 
 2005-06-27
 
 Introduced in Acme-MetaSyntactic version 0.28.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'oulipo'
DATA = '''\
\
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


