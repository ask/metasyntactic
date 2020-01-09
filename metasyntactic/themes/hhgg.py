# -*- coding: utf-8 -*-
'''

#########################
Acme::MetaSyntactic::hhgg
#########################

****
NAME
****


Acme::MetaSyntactic::hhgg - The Hitch Hiker's Guide to the Galaxy theme


***********
DESCRIPTION
***********


Characters and other names from Douglas Adams's "Hitch Hiker's Guide to
the Galaxy" book series.

The list is very incomplete (it should contain at least 42 items).

After glancing at
`http://en.wikisource.org/wiki/The_Ultra-Complete_Index_to_the_Hitch_Hiker%27s_Guide_to_the_Galaxy <http://en.wikisource.org/wiki/The_Ultra-Complete_Index_to_the_Hitch_Hiker%27s_Guide_to_the_Galaxy>`_,
I wonder if I should include all the entries...


************
CONTRIBUTORS
************


Aldo Calpini, Philippe Bruhat, Jean Forget.


*******
CHANGES
*******



- \*
 
 2012-05-07 - v1.000
 
 Received its own version number in Acme-MetaSyntactic-Themes version 1.000.
 


- \*
 
 2006-04-10
 
 Link updated in Acme-MetaSyntactic version 0.69.
 


- \*
 
 2005-06-27
 
 Link to \ *The Ultra-Complete Index to the Hitch Hiker's Guide to the Galaxy*\ 
 (written and entirely copyrighted 1992-94 by Mathias Maul)
 entry on Wikipedia provided by Jean Forget in time for
 Acme-MetaSyntactic version 0.28.
 


- \*
 
 2005-03-21
 
 Updated by Philippe "BooK" Bruhat (item \ ``fortytwo``\ )
 in Acme-MetaSyntactic version 0.14.
 


- \*
 
 2005-02-28
 
 Introduced in Acme-MetaSyntactic version 0.11.
 


- \*
 
 2005-02-22
 
 Submitted by Aldo Calpini.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'hhgg'
DATA = '''\
# names
answer arthur babelfish beeblebrox bugblatter_beast eccentrica_gallumbits 
fenchurch ford heartofgold jeltz kwaltz magrathea marvin milliways 
pan_galactic_gargle_blaster slartibartfast trillian vogon wonko zaphod
fortytwo\
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


