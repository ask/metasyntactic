# -*- coding: utf-8 -*-
'''
.. highlight:: perl


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


***********
CONTRIBUTOR
***********


Martin Vorländer.

Introduced in version 0.42, published on October 3, 2005.

Updated by Jean Forget in version 0.47, published on November 7, 2005.


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
data = parse_data(DATA)


def default():
    try:
        if 'default' in data:
            return data['default'][0]
    except KeyError, IndexError:
        pass
    return 'en'


def all():
    acc = set()
    for category, names in data['names'].iteritems():
        if names:
            acc |= names
    return acc


def names(category=None):
    if not category:
        category = default()
    if category == ':all':
        return list(all())
    return list(data['names'][category])


def random(n=1, category=None):
    got = names(category)
    if got:
        shuffle(got)
        if n == 1:
            return choice(got)
        return got[:n]

def sections():
    return set(data['names'].keys())


