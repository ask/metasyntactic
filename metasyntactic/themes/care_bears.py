# -*- coding: utf-8 -*-
'''

###############################
Acme::MetaSyntactic::care_bears
###############################

****
NAME
****


Acme::MetaSyntactic::care_bears - The Care Bears theme


***********
DESCRIPTION
***********


The Care Bears are characters created by American Greetings in the 1980s
for use on greeting cards. Later on, they got turned into plush teddy
bears, and got their own television series.

Official website: `http://www.care-bears.com/ <http://www.care-bears.com/>`_.


************
CONTRIBUTORS
************


ric Cassagnard, Philippe Bruhat.


*******
CHANGES
*******



- \*
 
 2012-11-12 - v1.000
 
 Published in Acme-MetaSyntactic-Themes version 1.027.
 


- \*
 
 2012-10-23
 
 Collected the list from
 `http://en.wikipedia.org/wiki/List_of_Care_Bear_characters <http://en.wikipedia.org/wiki/List_of_Care_Bear_characters>`_.
 Another possible source would be
 `http://carebears.wikia.com/wiki/List_Of_Care_Bear_Characters <http://carebears.wikia.com/wiki/List_Of_Care_Bear_Characters>`_.
 


- \*
 
 2006-07-13
 
 Idea submitted by ric Cassagnard.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::MultiList <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aMultiList&mode=module>`_.
'''

name = 'care_bears'
DATA = '''\
# names original
Bedtime_Bear
Birthday_Bear
Cheer_Bear
Friend_Bear
Funshine_Bear
Good_Luck_Bear
Grumpy_Bear
Love_a_Lot_Bear
Tenderheart_Bear
Wish_Bear
# names 1980s_1990s
Baby_Hugs_Bear
Baby_Tugs_Bear
Champ_Bear
Daydream_Bear
Forest_Friend_Bear
Grams_Bear
Harmony_Bear
I_Love_You_Bear
Perfect_and_Polite_Panda
Sea_Friend_Bear
Secret_Bear
Share_Bear
Surprise_Bear
Take_Care_Bear
True_Heart_Bear
# names 2000s
America_Cares_Bear
Bashful_Heart_Bear
Best_Friend_Bear
Do_Your_Best_Bear
Laugh_a_Lot_Bear
Smart_Heart_Bear
Thanks_a_Lot_Bear
Hopeful_Heart_Bear
All_My_Heart_Bear
Amigo_Bear
Heartsong_Bear
Play_a_Lot_Bear
Shine_Bright_Bear
Superstar_Bear
Work_of_Heart_Bear
Sweet_Dreams_Bear
Always_There_Bear
Oopsy_Bear
Pink_Power_Bear
Sweet_Sakura_Bear
# names 2010s
Wonderheart_Bear
Great_Giving_Bear
# names movie
Me_Bear
Messy_Bear
Too_Loud_Bear
# names cousins
Brave_Heart_Lion
Bright_Heart_Raccoon
Cozy_Heart_Penguin
Gentle_Heart_Lamb
Lotsa_Heart_Elephant
Loyal_Heart_Dog
Noble_Heart_Horse
Playful_Heart_Monkey
Proud_Heart_Cat
Swift_Heart_Rabbit
Treat_Heart_Pig\
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


