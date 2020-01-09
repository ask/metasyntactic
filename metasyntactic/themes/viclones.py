# -*- coding: utf-8 -*-
'''

#############################
Acme::MetaSyntactic::viclones
#############################

****
NAME
****


Acme::MetaSyntactic::viclones - The \ ``vi``\  clones theme


***********
DESCRIPTION
***********


A list of vi clones, as maintained by Sven Guckes on
`http://www.guckes.net/vi/clones.php3 <http://www.guckes.net/vi/clones.php3>`_.


***********
CONTRIBUTOR
***********


Philippe "BooK" Bruhat.


*******
CHANGES
*******



- \*
 
 2012-05-07 - v1.000
 
 Received its own version number in Acme-MetaSyntactic-Themes version 1.000.
 


- \*
 
 2005-11-21
 
 Added a remote list in Acme-MetaSyntactic version 0.49.
 


- \*
 
 2005-02-21
 
 Introduced in Acme-MetaSyntactic version 0.10.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'viclones'
DATA = '''\
# names
BBStevie bedit Bvi calvin e3 Elvis exvi elwin javi jVi Lemmy levee nvi
Oak_Hill_vi PVIC trived tvi vigor vile vim Watcom_VI WinVi viper virus
xvi\
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


