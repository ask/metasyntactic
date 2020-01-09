# -*- coding: utf-8 -*-
'''

#################################
Acme::MetaSyntactic::thunderbirds
#################################

****
NAME
****


Acme::MetaSyntactic::thunderbirds - Thunderbirds are GO!


***********
DESCRIPTION
***********


Items related to the 1960s \ *Supermarionation*\  TV series \ *Thunderbirds*\ .

This list contains 5 categories: \ ``characters``\ , \ ``crafts``\ , \ ``episodes``\ ,
\ ``movies``\ , and \ ``novels``\ . The latter category has two subcategories,
\ ``novels/Thunderbirds``\  for novels about the Thunderbirds, and
\ ``novels/Lady_Penelope``\ , the novels starring Lady Penelope.

The default category is \ ``characters``\ .


*******
SOURCES
*******


`http://www.thunderbirds.com/ <http://www.thunderbirds.com/>`_,
`http://en.wikipedia.org/wiki/Thunderbirds_%28TV_series%29 <http://en.wikipedia.org/wiki/Thunderbirds_%28TV_series%29>`_.


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
 
 2006-10-16
 
 Introduced in Acme-MetaSyntactic version 0.96.
 


- \*
 
 2006-05-13
 
 Submitted by Abigail.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::MultiList <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aMultiList&mode=module>`_.
'''

name = 'thunderbirds'
DATA = '''\
# default 
characters
# names characters
Jeff_Tracey Scott_Tracy John_Tracy Virgil_Tracy Gordon_Tracy Alan_Tracy
Tin_Tin Brains Lady_Penelope Parker Grandma Kyrano The_Hood
# names crafts
Thunderbird_1 Thunderbird_2 Thunderbird_3 Thunderbird_4 Thunderbird_5
FAB1 FAB2 The_Mole The_Domo Firefly Thunderiser Booster_Mortar Excadigger
# names episodes
Trapped_in_the_Sky Pit_of_Peril City_of_Fire Sun_Probe The_Uninvited
The_Mighty_Atom Vault_of_Death Operation_Crash_Dive Move_and_Youre_Dead
Martian_Invasion Brink_of_Disaster The_Perils_of_Penelope
Terror_in_New_York_City End_of_the_Road Day_of_disaster Edge_of_Impact
Desperate_Intruder Thirty_Minutes_After_Noon The_Impostors The_Man_From_MI5
Cry_Wolf Danger_at_Ocean_Deep The_Duchess_Assignment Attack_of_the_Alligators
The_Cham_Cham Security_Hazard Atlantic_Inferno Path_of_Destruction
Alias_Mr_Hackenbacker Lord_Parkers_Oliday Ricochet Give_or_Take_a_Million
# names movies
Thunderbirds_Are_GO Thunderbird_6
# names novels Thunderbirds
Thunderbirds Calling_Thunderbirds Ring_of_Fire Thunderbirds_Are_Go
Operation_Asteroids Lost_World
# names novels Lady_Penelope
A_Gallery_of_Thieves Cool_for_Danger The_Albanian_Affair\
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


