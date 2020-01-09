# -*- coding: utf-8 -*-
'''

#############################
Acme::MetaSyntactic::jerkcity
#############################

****
NAME
****


Acme::MetaSyntactic::jerkcity - The Jerkcity theme


***********
DESCRIPTION
***********


Character names and other keywords from the popular (at least
on #perl) webcomic \ *jerkcity*\ .

See `http://www.jerkcity.com/ <http://www.jerkcity.com/>`_ for details.


***********
CONTRIBUTOR
***********


Rafal Garcia-Suarez.


*******
CHANGES
*******



- \*
 
 2012-05-07 - v1.000
 
 Received its own version number in Acme-MetaSyntactic-Themes version 1.000.
 


- \*
 
 2005-08-29
 
 Introduced in Acme-MetaSyntactic version 0.37.
 


- \*
 
 2005-08-23
 
 After some discussion on IRC, \ ``rgs``\  provided the initial list:
 
 
 .. code-block:: perl
 
      14:10 <@rgs> il faut en faire un jerkcity
      14:10 <@rgs> DONGS
      14:10 <@rgs> spigot deuce rands
      14:10 <@rgs> et pants
      14:11 <@rgs> HUGLAGHALGHALGHAL
      14:11 <@rgs> T
      14:12 <@rgs> il doit tre possible d'extraire la liste des personnages automatiquement
      14:12 <@rgs> avec un script perl, par exemple
      14:17 <@rgs> http://en.wikipedia.org/wiki/Jerkcity
      14:18 <@BooK> rgs: patches welcome
      14:18 <+purl> Of course, you really mean FOAD, HAND, HTH
      14:19 <@rgs> BooK: forthcoming
      14:21 <@rgs> BooK: Atandt Bung Deuce Dick Effigy Hanford Harriet Jean_Charles Net Ozone Pants Rands Spigot T HUGLAGHALGHALGHAL gay dicks dongs rape piss
      14:23 <@rgs> d'autres mots-cls du plot ?
      14:24 <@rgs> hmm, peut tre faut ajouter une option --over-18  meta(1)
 
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'jerkcity'
DATA = '''\
# names
Atandt Bung Deuce Dick Effigy Hanford Harriet Jean_Charles Net Ozone
Pants Rands Spigot T HUGLAGHALGHALGHAL gay dicks dongs rape piss\
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


