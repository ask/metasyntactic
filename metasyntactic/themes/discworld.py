# -*- coding: utf-8 -*-
'''

##############################
Acme::MetaSyntactic::discworld
##############################

****
NAME
****


Acme::MetaSyntactic::discworld - The Discworld theme


***********
DESCRIPTION
***********


This theme contains items from Terry Pratchett's Discworld series.


************
CONTRIBUTORS
************


Martin Vorländer, Jean Forget.


***********
IN MEMORIAM
***********


This theme is dedicated to


- Josh Kirby (1928-2001)
 
 "I only invented the Discworld. Josh created it."
 
 -- Terry Pratchett
 


- Terry Pratchett (1948-2015)
 
 
 .. code-block:: perl
 
    AT LAST, SIR TERRY, WE MUST WALK TOGETHER.
  
    Terry took Death’s arm and followed him through the doors and on to the black desert under the endless night.
  
    The End
  
    @terryandrob on Twitter, 12 March 2015
 
 



*******
CHANGES
*******



- \*
 
 2015-06-08 - v1.002
 
 Updated with IN MEMORIAM after the passing of Sir Terry Pratchett
 on March 12, 2015. Published in Acme-MetaSyntactic-Themes version 1.046.
 


- \*
 
 2012-05-14 - v1.001
 
 Updated with an \ ``=encoding``\  pod command.
 
 Published in Acme-MetaSyntactic-Themes version 1.001.
 


- \*
 
 2012-05-07
 
 Received its own version number in Acme-MetaSyntactic-Themes version 1.000.
 


- \*
 
 2005-11-07
 
 Updated by Jean Forget in Acme-MetaSyntactic version 0.47.
 


- \*
 
 2005-10-03
 
 Introduced in Acme-MetaSyntactic version 0.42.
 


- \*
 
 2005-09-02
 
 Initial list proposed by Martin Vorländer.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'discworld'
DATA = '''\
# names
great_a_tuin berilia jerakeen tubul great_t_phon
rincewind twoflower death nanny_ogg granny_weatherwax magrat_garlick
agnes_nitt king_verence jason_ogg shawn_ogg
mustrum_ridcully ponder_stibbons windle_poons ipslore igneous_cutwell
eric mort ysabell susan binky
alberto_malich lord_vetinari leonardo_da_quirm lady_sybil_ramkin
greebo pteppic ptraci 
captain_vimes carrot angua littlebottom
detritus sergeant_colon nobby reg_shoe errol gaspode bel_shamharoth
offler blind_io creosote conina nijel koomi ksandra granpone bravd weasel tethis
bathys garhartra dibbler gaffer silverfish
brutha vorbis casanunda william_de_worde
cohen caleb_the_ripper old_vincent mad_hamish boy_willy

ankh_morpork the_broken_drum dunmanifestin wyrmberg nef sto_lat lancre
cori_celesti tsort pseudopolis sto_helit klatch quirm
ramtops uberwald djelibeybi ephebe genua llamedos agatean_empire xxxx\
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


