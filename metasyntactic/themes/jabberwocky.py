# -*- coding: utf-8 -*-
'''

################################
Acme::MetaSyntactic::jabberwocky
################################

****
NAME
****


Acme::MetaSyntactic::jabberwocky - Jabberwocky


***********
DESCRIPTION
***********


Words from the famous poem by Lewis Carroll.


****
POEM
****


Source: `http://en.wikisource.org/wiki/Jabberwocky <http://en.wikisource.org/wiki/Jabberwocky>`_.


.. code-block:: perl

     'Twas brillig, and the slithy toves
     Did gyre and gimble in the wabe;
     All mimsy were the borogoves,
     And the mome raths outgrabe.
 
     'Beware the Jabberwock, my son!
     The jaws that bite, the claws that catch!
     Beware the Jubjub bird, and shun
     The frumious Bandersnatch!'
 
     He took his vorpal sword in hand:
     Long time the manxome foe he sought--
     So rested he by the Tumtum tree,
     And stood awhile in thought.
 
     And as in uffish thought he stood,
     The Jabberwock, with eyes of flame,
     Came whiffling through the tulgey wood,
     And burbled as it came!
 
     One, two! One, two! And through and through
     The vorpal blade went snicker-snack!
     He left it dead, and with its head
     He went galumphing back.
 
     'And has thou slain the Jabberwock?
     Come to my arms, my beamish boy!
     O frabjous day! Callooh! Callay!'
     He chortled in his joy.
 
     'Twas brillig, and the slithy toves
     Did gyre and gimble in the wabe;
     All mimsy were the borogoves,
     And the mome raths outgrabe.



**********************
OTHER PERLISH VERSIONS
**********************


Some perlmonks have tried their hand on this classic too:


- \*
 
 `http://perlmonks.org/?node_id=29907 <http://perlmonks.org/?node_id=29907>`_ by wombat,
 


- \*
 
 `http://perlmonks.org/?node_id=111157 <http://perlmonks.org/?node_id=111157>`_ by andreychek,
 


- \*
 
 `http://perlmonks.org/?node_id=195873 <http://perlmonks.org/?node_id=195873>`_ by RMGir.
 



***********
CONTRIBUTOR
***********


Abigail


*******
CHANGES
*******



- \*
 
 2012-05-07 - v1.000
 
 Received its own version number in Acme-MetaSyntactic-Themes version 1.000.
 


- \*
 
 2006-09-25
 
 Introduced in Acme-MetaSyntactic version 0.93.
 


- \*
 
 2005-10-24
 
 Submitted by Abigail.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_,
'''

name = 'jabberwocky'
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


