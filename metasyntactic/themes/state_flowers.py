# -*- coding: utf-8 -*-
'''

##################################
Acme::MetaSyntactic::state_flowers
##################################

****
NAME
****


Acme::MetaSyntactic::state_flowers - The US State Flowers theme


***********
DESCRIPTION
***********


Each US state has a state flower. This theme uses all of them. Note however
that while there are 50 US states, there are only 43 entries in this theme.
This is not a bug - there are 7 pairs of states that have a common state
flower. Which leaves 43 different flowers.


***********
CONTRIBUTOR
***********


Abigail


*******
CHANGES
*******



- \*
 
 2012-05-07
 
 Received its own version number in Acme-MetaSyntactic-Themes version 1.000.
 


- \*
 
 2006-09-04
 
 Introduced in Acme-MetaSyntactic version 0.90.
 


- \*
 
 2005-11-01
 
 Submitted by Abigail.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'state_flowers'
DATA = '''\
# names
American_Dogwood Apple_Blossom Bitterroot Black_Eyed_Susan
Bluebonnet California_Poppy Camellia Cherokee_Rose Coast_Rhododendron
Forget_Me_Not Goldenrod Hawaiian_Hibiscus Hawthorn Indian_Paintbrush
Iris Magnolia Mayflower Mock_Orange Mountain_Laurel Oklahoma_Rose
Orange_Blossom Oregon_Grape Pasque_Flower Peach_Blossom
Peony Pink_and_White_Lady_s_Slipper Purple_Lilac Purple_Violet
Red_Clover Rhododendron Rocky_Mountain_Columbine Rose Sagebrush
Saguaro_Cactus_blossom Scarlet_Carnation Sego_Lily Sunflower Violet
White_Pine_Cone_and_Tassel Wild_Prairie_Rose Wood_Violet Yellow_Jessamine
Yucca_Flower\
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


