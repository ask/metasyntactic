# -*- coding: utf-8 -*-
'''

############################
Acme::MetaSyntactic::browser
############################

****
NAME
****


Acme::MetaSyntactic::browser - The "browser" theme


***********
DESCRIPTION
***********


Some famous web browsers.

Evolt.org maintains a browser archive at `http://browsers.evolt.org/ <http://browsers.evolt.org/>`_.
The information in the archive was not used to create this list.

Wikipedia maintains a large list of web browsers at
`https://en.wikipedia.org/wiki/List_of_web_browsers <https://en.wikipedia.org/wiki/List_of_web_browsers>`_.


************
CONTRIBUTORS
************


Philippe "BooK" Bruhat, Sbastien Aperghis-Tramoni, Rafal Garcia-Suarez.


*******
CHANGES
*******



- \*
 
 2012-05-14 - v1.001
 
 Updated with an \ ``=encoding``\  pod command
 in Acme-MetaSyntactic-Themes version 1.001.
 


- \*
 
 2012-05-07 - v1.000
 
 Updated with Google Chrome, and
 received its own version number in Acme-MetaSyntactic-Themes version 1.000.
 


- \*
 
 2006-10-16
 
 Updated in Acme-MetaSyntactic version 0.96.
 


- \*
 
 2006-04-17
 
 Updated in Acme-MetaSyntactic version 0.70.
 


- \*
 
 2005-01-16
 
 Introduced in Acme-MetaSyntactic version 0.05.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'browser'
DATA = '''\
# names
mozilla netscape msie mosaic links lynx w3m opera galeon konqueror safari
camino dillo amaya arachne omniweb planetweb voyager seamonkey iceweasel
chrome\
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


