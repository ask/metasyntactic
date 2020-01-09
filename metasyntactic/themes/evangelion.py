# -*- coding: utf-8 -*-
'''

###############################
Acme::MetaSyntactic::evangelion
###############################

****
NAME
****


Acme::MetaSyntactic::evangelion - The Neon Genesis Evangelion theme


***********
DESCRIPTION
***********


This theme provides the English names of the characters from the
Japanese animated series \ *Neon Genesis Evangelion*\ , and also other
terms used in the series. It also contains names from the \ *Rebuild
of Evangelion*\  tetralogy and from 新世紀エヴァンゲリオン 碇シンジ育成計画
(\ *Shin Seiki Evangelion: Ikari Shinji Ikusei Keikaku*\ ).

`http://en.wikipedia.org/wiki/Neon_Genesis_Evangelion <http://en.wikipedia.org/wiki/Neon_Genesis_Evangelion>`_ is a good
start to read about about \ *Evangelion*\ .

Categories
==========


This theme contains the following categories:


* pilots/original
 
 names of the Evangelion pilots
 


* pilots/Rebuild
 
 names of the additional pilots in \ *Rebuild of Evangelion*\ 
 


* staff/nerv/original
 
 names of the people working for the Nerv organisation
 


* staff/nerv/dead
 
 names of the people who worked for the Nerv organisation,
 but are dead before the beginning of the show
 


* staff/nerv/IkuseiKeikaku
 
 names of the additional people working for the Nerv organisation
 in \ *Shin Seiki Evangelion: Ikari Shinji Ikusei Keikaku*\ 
 


* staff/seele
 
 names of the people working for the Seele organisation
 


* magi
 
 names of the MAGI super-computer
 


* evas
 
 Japanese names of the Evangelions
 


* angels
 
 names of the Angels (Shito)
 


* students/original
 
 names of other students
 


* students/IkuseiKeikaku
 
 names of other students
 in \ *Shin Seiki Evangelion: Ikari Shinji Ikusei Keikaku*\ 
 


* animals
 
 names of the animals
 


* glossary/common
 
 miscellaneous names
 


* glossary/Rebuild
 
 additionnal names from \ *Rebuild of Evangelion*\ 
 




***********
CONTRIBUTOR
***********


Sébastien Aperghis-Tramoni.


*******
CHANGES
*******



- \*
 
 2013-10-14 - v1.001
 
 Fixed a typo in Sébastien's last name and now load the proper parent module,
 in Acme-MetaSyntactic-Themes version 1.037.
 


- \*
 
 2012-09-03 - v1.000
 
 Published in Acme-MetaSyntactic-Themes version 1.017.
 
 Reviewed to fix a few mistakes, and improve the tags.
 Added names from the \ *Rebuild of Evangelion*\  tetralogy and from
 新世紀エヴァンゲリオン 碇シンジ育成計画 (\ *Shin Seiki Evangelion:
 Ikari Shinji Ikusei Keikaku*\ ).
 Documented the categories.
 


- \*
 
 2006-01-05
 
 Submitted by Sébastien Aperghis-Tramoni (Maddingue).
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'evangelion'
DATA = '''\
# names pilots original
First_Children Ayanami_Rei
Second_Children Soryu_Asuka_Langley
Third_Children Ikari_Shinji
Fourth_Children Suzuhara_Toji
Fifth_Children Nagisa_Kaworu
# names pilots Rebuild
Shikinami_Asuka_Langley
Makinami_Illustrious_Mari

# names staff nerv original
Ikari_Gendoo
Fuyutsuki_Kozo
Akagi_Ritsuko
Katsuragi_Misato
Ryouji_Kaji
Ibuki_Maya
Hyuga_Makoto
Shigeru_Aoba
# names staff nerv dead
Ikari_Yui
Soryu_Zeppelin_Kyoko
Akagi_Naoko
# names staff nerv IkuseiKeikaku
Agano_Kaede
Ooi_Satsuki
Mogami_Aoi

# names staff seele
Keel_Lorenz

# names magi
MAGI Melchior Balthasar Casper

# names evas
Zerogoki Shogoki Nigoki Sangoki Yongoki Ryousanki

# names angels
Adam Lilith Sachiel Shamshel Ramiel Gaghiel Israfel Sandalphon Matarael
Sahaqiel Ireul Leliel Bardiel Zeruel Arael Armisael Tabris Lilin

# names students original
Aida_Kensuke
Horaki_Hikari
# names students IkuseiKeikaku
Kirishima_Mana

# names animals
Pen_Pen

# names glossary common
Seele Gehirn Nerv Marduk_Institute
Sephiroth Dead_Sea_Scrolls Human_Instrumentality_Project
Henflick_limit
Eva Evangelion Shito Angel
B_type D_Type F_type
entry_plug dummy_system dummy_plug LCL
progressive_knife lance_of_Longinus 
AT_Field S2_Engine beast_mode berserk_mode
N2_bomb Jet_Alone
Tokyo_3 GeoFront Central_Dogma Terminal_Dogma
First_Impact Second_Impact Third_Impact
# names glossary Rebuild
Bethany_Base Limbo_area Cocytus Malebolge_system Styx_shaft Acheron
Tabgha_Base\
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


