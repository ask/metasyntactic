# -*- coding: utf-8 -*-
'''

################################
Acme::MetaSyntactic::wales_towns
################################

****
NAME
****


Acme::MetaSyntactic::wales_towns - Towns in Wales


***********
DESCRIPTION
***********


List of towns in Wales.

It would be nice to extend this to a list of all towns and villages
in Wales, if only to be able to include
Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch.

Source: `http://en.wikipedia.org/wiki/List_of_towns_in_Wales <http://en.wikipedia.org/wiki/List_of_towns_in_Wales>`_.


************
CONTRIBUTORS
************


Abigail, Philippe Bruhat (BooK).


*******
CHANGES
*******



- \*
 
 2019-10-28 - v1.013
 
 Updated from the source web site in Acme-MetaSyntactic-Themes version 1.054.
 


- \*
 
 2019-07-29 - v1.012
 
 Updated from the source web site in Acme-MetaSyntactic-Themes version 1.053.
 


- \*
 
 2017-11-13 - v1.011
 
 Updated from the source web site in Acme-MetaSyntactic-Themes version 1.051.
 


- \*
 
 2017-06-12 - v1.010
 
 Updated from the source web site in Acme-MetaSyntactic-Themes version 1.050.
 


- \*
 
 2016-03-21 - v1.009
 
 Updated from the source web site in Acme-MetaSyntactic-Themes version 1.049.
 


- \*
 
 2015-10-19 - v1.008
 
 Updated from the source web site in Acme-MetaSyntactic-Themes version 1.048.
 


- \*
 
 2015-02-02 - v1.007
 
 Updated from the source web site in Acme-MetaSyntactic-Themes version 1.045.
 


- \*
 
 2015-01-05 - v1.006
 
 Updated from the source web site in Acme-MetaSyntactic-Themes version 1.044.
 


- \*
 
 2014-04-07 - v1.005
 
 Updated from the source web site in Acme-MetaSyntactic-Themes version 1.039.
 


- \*
 
 2013-12-09 - v1.004
 
 Updated from the source web site in Acme-MetaSyntactic-Themes version 1.038.
 


- \*
 
 2013-10-14 - v1.003
 
 Updated from the source web site in Acme-MetaSyntactic-Themes version 1.037.
 


- \*
 
 2013-07-22 - v1.002
 
 Updated from the source web site in Acme-MetaSyntactic-Themes version 1.034.
 


- \*
 
 2013-06-17 - v1.001
 
 Updated from the source web site in Acme-MetaSyntactic-Themes version 1.033.
 


- \*
 
 2012-08-27 - v1.000
 
 Added a remote source for the list and updated the list
 in Acme-MetaSyntactic-Themes v1.016.
 


- \*
 
 2005-10-25
 
 Submitted by Abigail.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'wales_towns'
DATA = '''\
# names
Aberaeron
Aberavon
Aberbargoed
Abercarn
Aberdare
Abergavenny
Abergele
Abertillery
Aberystwyth
Amlwch
Ammanford
Bagillt
Bala
Bangor
Bargoed
Barmouth
Barry
Beaumaris
Bethesda
Blackwood
Blaenau_Ffestiniog
Blaenavon
Blaina
Brecon
Bridgend
Briton_Ferry
Brynmawr
Buckley
Builth_Wells
Burry_Port
Caerleon
Caernarfon
Caerphilly
Caerwys
Caldicot
Cardiff
Cardigan
Carmarthen
Chepstow
Chirk
Cilgerran
Colwyn_Bay
Connah_s_Quay
Conwy
Corwen
Cowbridge
Criccieth
Crickhowell
Crumlin
Crymych
Cwmamman
Cwmbran
Denbigh
Dolgellau
Ebbw_Vale
Ewloe
Fishguard
Flint
Gelligaer
Glynneath
Goodwick
Gorseinon
Gowerton
Gresford
Harlech
Haverfordwest
Hay_on_Wye
Holyhead
Holywell
Kidwelly
Knighton
Lampeter
Laugharne
Llanberis
Llandeilo
Llandovery
Llandrindod_Wells
Llandudno
Llandudno_Junction
Llandysul
Llanelli
Llanfair_Caereinion
Llanfairfechan
Llanfyllin
Llangefni
Llangollen
Llanidloes
Llanrwst
Llantrisant
Llantwit_Major
Llanwrtyd_Wells
Llanybydder
Loughor
Machynlleth
Maesteg
Menai_Bridge
Merthyr_Tydfil
Milford_Haven
Mold
Monmouth
Montgomery
Narberth
Neath
Nefyn
Newbridge
Newcastle_Emlyn
Newport
Newport_Pembrokeshire
New_Quay
Newtown
Neyland
Old_Colwyn
Overton_on_Dee
Pembroke
Pembroke_Dock
Penarth
Pencoed
Penmaenmawr
Penrhyn_Bay
Pontardawe
Pontarddulais
Pontyclun
Pontypool
Pontypridd
Porth
Porthcawl
Porthmadog
Port_Talbot
Prestatyn
Presteigne
Pwllheli
Queensferry
Rhayader
Rhuddlan
Rhyl
Rhymney
Risca
Ruthin
Saltney
Senghenydd
Shotton
St_Asaph
St_Clears
Swansea
Talgarth
Tenby
Tonypandy
Tredegar
Tregaron
Treharris
Tywyn
Usk
Welshpool
Whitland
Wrexham
Ystradgynlais
Ystrad_Mynach\
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


