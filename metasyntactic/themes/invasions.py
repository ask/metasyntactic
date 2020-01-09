# -*- coding: utf-8 -*-
'''

##############################
Acme::MetaSyntactic::invasions
##############################

****
NAME
****


Acme::MetaSyntactic::invasions - The naval and airborne invasions theme


***********
DESCRIPTION
***********


This list gives some codenames for naval invasions, paradrops and
operations with both a naval invasion component and an airborne
component during World War II. The list includes some operations which
were planned but not executed.

Sources, among others:


- \*
 
 the \ *Codeword Dictionnary*\ ,
 Paul Adkins, Motorbooks International
 (ISBN 0-7603-00368-1)
 


- \*
 
 \ *Strategy & Tactics*\  #160, May 1993
 



- Al
 
 Diversionary invasion of the Aleutians, in support of the invasion of Midway. Executed on 7th June 1942.
 


- Anvil
 
 Invasion of the South of France, near Toulon and Marseille. Executed as "Dragoon" on 15th August 1944.
 


- Avalanche
 
 Invasion on Salerno, executed on 9 September 1943.
 


- Barracuda
 
 Invasion of the Naples region, also known as Gangway or Mustang. Planned but never executed.
 


- Baytown
 
 Diversionary invasion of Calabria near Reggio Calabria, executed on 3rd September 1943,
 in support of Avalanche and Slapstick.
 


- Brimstone
 
 Invasion of Sardinia. Planned but never executed.
 


- Buttress
 
 Invasion of Calabria near Cetrano, Almantea and Pizzo. Planned but never executed.
 


- Coronet
 
 Invasion of Honshu, in the Tokyo Plain. Planned for December 1945 or March 1946, but
 the war ended before.
 


- Detachment
 
 Invasion of Iwo Jima. Executed on 19th February 1945.
 


- Dragoon
 
 Invasion of the South of France, near Toulon. Executed on 15th August 1944. Also known
 as "Anvil".
 


- Eclipse
 
 Paradrop on Berlin. Planned but never executed.
 


- Firebrand
 
 Invasion of Corsica. Planned but never executed.
 


- Flintlock
 
 Invasion of Kwajalein. Executed on 31st January 1944.
 


- Gangway
 
 Invasion of the Naples region, also known as Barracuda or Mustang. Planned but never executed.
 


- Giant_I
 
 Paradrop on Caserta, Capua and the Volturno river, in support of Avalanche. Planned but
 never executed.
 


- Giant_II
 
 Paradrop on Rome. Planned but never executed.
 


- Goblet
 
 Invasion of Calabria near Crotone. Planned but never executed.
 


- Gruener_Pfeil
 
 German invasion of Jersey and Guernsey. Executed on 1st July 1940. The islands were
 occupied until 8th May 1945.
 


- Herkules
 
 German airborne invasion of Malta. Planned but never executed.
 


- Husky
 
 Invasion of Sicily, executed on 10th July 1943.
 


- Iceberg
 
 Invasion of Okinawa. Executed on 1st April 1945.
 


- Ikarus
 
 German invasion of Iceland. Planned but never executed.
 


- Jubilee
 
 Probing invasion of Dieppe. Executed on 19th August 1942.
 


- Leopard
 
 German invasion of the Greek island Leros. Executed on 12th November 1943.
 


- Market_Garden
 
 Joint airborne + armored invasion of the Netherlands. Executed on 7th September 1944.
 


- Menace
 
 Invasion of Dakar by British and Free French troops. Attempted on 23rd September 1940.
 


- Merkur
 
 German paradrop on Crete. Executed on 20th May 1941.
 


- Mi
 
 Japanese invasion of Midway. Attempted on 3rd June 1942.
 


- Mo
 
 Japanese plan including operation Al and operation Mi.
 


- Musket
 
 Invasion of Southern Italy. Planned but never executed.
 


- Mustang
 
 Invasion of the Naples region, also known as Barracuda or Gangway. Planned but never executed.
 


- Oboe
 
 A series of landings by American and Australian troops on Borneo and neighbour
 islands. Executed between May 1945 and July 1945.
 


- Olympic
 
 Invasion of Kyushu. Planned for 1st November 1945, but the war ended before this date.
 


- Overlord
 
 Invasion of Normandy. Executed on 6th June 1944.
 


- Roundhammer
 
 Invasion of Northern France. The plan was proposed but never adopted.
 


- Roundup
 
 Invasion of Northern France in 1943. Planned but never executed.
 


- Seeloewe
 
 German invasion of Great Britain. Planned for September 1940, but never executed.
 


- Shingle
 
 Invasion on Anzio, executed on 22nd January 1944.
 


- Shoestring
 
 Invasion of Guadalcanal. Executed on 7th August 1942. Its official name is "Watchtower".
 


- Slapstick
 
 Invasion on the Gulf of Taranto, executed on 9th September 1943.
 


- Sledgehammer
 
 Invasion of Western Europe. Considered in 1942 but never planned.
 


- Torch
 
 Invasion of North Africa. Executed on 8th November 1942.
 


- Varsity
 
 Paradrop across the Rhine. Executed on 23rd March 1945.
 


- Victor
 
 Series of amphibious landings on the Philippine Islands. Executed in 1945.
 


- Watchtower
 
 Invasion of Guadalcanal. Executed on 7th August 1942. Nicknamed as "Shoestring".
 



***********
CONTRIBUTOR
***********


Jean Forget


*******
CHANGES
*******



- \*
 
 2015-02-02 - v1.001
 
 Include names from \ *Strategy & Tactics*\  #160.
 
 Use the "POD inside here-doc" trick to give some historical tidbits about the various names.
 
 Published in Acme-MetaSyntactic-Themes v1.045.
 


- \*
 
 2012-05-07 - v1.000
 
 Received its own version number in Acme-MetaSyntactic-Themes version 1.000.
 


- \*
 
 2006-09-18
 
 Introduced in Acme-MetaSyntactic version 0.92,
 on the 62nd anniversary of Market-Garden.
 


- \*
 
 2006-06-14
 
 Submitted by Jean Forget.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'invasions'
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


