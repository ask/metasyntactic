# -*- coding: utf-8 -*-
'''
.. highlight:: perl


###################################
Acme::MetaSyntactic::space_missions
###################################

****
NAME
****


Acme::MetaSyntactic::space_missions - The space missions theme


***********
DESCRIPTION
***********


This theme lists the names of various space missions flights.


Apollo
 
 As from Apollo 9, the command and lunar modules of Project Apollo were
 given radio call signs. This list document them.
 
 Source: \ *A Man on the Moon*\ , by Andrew Chaikin.
 


Mercury
 
 This list gives the names of the six Mercury spacecraft,
 plus the name of the flight cancelled when Deke Slayton
 was grounded for health reasons.
 
 Source: \ *The Right Stuff*\ , by Tom Wolfe.
 


Manned Spacecraft
 
 This list gives the names of the manned spacecraft,
 all nations and all agencies or firms combined.
 


Launch Vehicles
 
 This list gives the names of launch vehicles type. For vehicles with
 several numbered subtypes, only the main type has been given, without
 the subtype number (which gives one-letter names for Japanese launch
 vehicles).
 
 Source: The list of launch vehicles is taken from the colour
 photos from \ *Rocket Science*\ , Alfred J. Zaehringer, Apogee
 (ISBN 1-894959-09-4).
 To this book, I have added
 `http://en.wikipedia.org/wiki/List_of_launch_vehicles <http://en.wikipedia.org/wiki/List_of_launch_vehicles>`_ and
 `http://en.wikipedia.org/wiki/Scaled_Composites_White_Knight <http://en.wikipedia.org/wiki/Scaled_Composites_White_Knight>`_.
 


Victims
 
 This list gives the names of the humans who were killed in a
 spacecraft accident.
 
 Source: `http://en.wikipedia.org/wiki/Category:Space_program_fatalities <http://en.wikipedia.org/wiki/Category:Space_program_fatalities>`_
 `http://en.wikipedia.org/wiki/Space_disaster <http://en.wikipedia.org/wiki/Space_disaster>`_.
 



***********
CONTRIBUTOR
***********


Jean Forget

Introduced in version 0.41 as \ ``apollo``\ , published on September 26, 2005.

Augmented with other space missions and renamed \ ``space_missions``\  in
version 0.86, published on August 7, 2006.

Updated with themes \ ``manned_spacecraft``\ , \ ``launch_vehicles``\  and \ ``victims``\ 
in version 0.88, published on August 21, 2006.


********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::MultiList <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aMultiList&mode=module>`_.
'''

name = 'space_missions'
DATA = '''\
# default
:all
# names apollo
Gumdrop Spider
Charlie_Brown Snoopy
Columbia Eagle
Yankee_Clipper Intrepid
Odyssey Aquarius
Kitty_Hawk Antares
Endeavour Falcon
Casper Orion
America Challenger
# names mercury
Freedom7
Liberty_Bell7
Friendship7
Delta7
Aurora7
Sigma7
Faith7
# names manned_spacecraft
Vostok Mercury X_15 Voskhod Gemini Soyuz
Apollo Salyut Skylab Space_Shuttle
Mir ISS Shenzhou SpaceShipOne
# names launch_vehicles
Vanguard Jupiter Thor Juno Redstone Atlas Centaur Agena Titan Delta Saturn Scout Pegasus Minotaur
R_7 Cosmos N_1 Semyorka Proton Dnepr Energia Start
Diamant Veronique
Ariane
Long_March
Shavit
N H J
White_Knight
# names victims
Gus_Grissom Ed_White Roger_Chaffee
Vladimir_Komarov
Mike_Adams
Georgi_Dobrovolski Viktor_Patsayev Vladislav_Volkov
Greg_Jarvis Christa_McAuliffe Ronald_McNair Ellison_Onizuka Judith_Resnik Michael_J_Smith Dick_Scobee
Rick_D_Husband William_McCool Michael_P_Anderson David_M_Brown
Kalpana_Chawla Laurel_B_Clark Ilan_Ramon\
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


