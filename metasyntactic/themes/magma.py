# -*- coding: utf-8 -*-
'''

##########################
Acme::MetaSyntactic::magma
##########################

****
NAME
****


Acme::MetaSyntactic::magma - The Magma theme


***********
DESCRIPTION
***********


This theme list the song titles of the Magma band.

The band was created in 1969 by Christian Vander and is still
touring in 2012.

Some links:


- \*
 
 `http://members.aol.com/sleeplessz/ <http://members.aol.com/sleeplessz/>`_
 


- \*
 
 `http://www.seventhrecords.com/ <http://www.seventhrecords.com/>`_
 


- \*
 
 `http://en.wikipedia.org/wiki/Magma_(band) <http://en.wikipedia.org/wiki/Magma_(band)>`_
 



***********
CONTRIBUTOR
***********


Philippe "BooK" Bruhat.


*******
CHANGES
*******



- \*
 
 2012-10-15 - v1.001
 
 Updated with the songs from the album Flicit Thsz, and
 published in Acme-MetaSyntactic-Themes version 1.023.
 


- \*
 
 2012-05-07 - v1.000
 
 Updated with the songs from the album mhnthtt-R, and
 received its own version number in Acme-MetaSyntactic-Themes version 1.000.
 


- \*
 
 2006-10-30
 
 Introduced in Acme-MetaSyntactic version 0.98.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'magma'
DATA = '''\
# default
:all
# names magma
Kobaia
Aina
Malaria
Sohia
Sckxyss
Aurae
Thaud Zaia
Nau Ektila
Stoah
Muh
# names 1001_degres_centigrade
Riah_Sahiltaahk
Iss_Lansei_Doia
Ki_Iahl_O_Liahk
# names mekanik_destruktiw_kommandoh
Hortz_Fur_Dehn_Stekehn_West
Ima_suri_Dondai
Kobaia_is_de_Hundin
Da_Zeuhl_wortz_Mekanik
Nebehr_Gudahtt
Mekanik_Kommandoh
Kreuhn_Kohrmahn_Iss_de_Hundin
# names kohntarkosz
Kohntarkosz
Ork_Alarm
Coltrane_Sundia
# names wurdah_itah
Malawelekaahm
Bradia_da_Zimehn_Iegah
Maneh_Fur_Da_Zess
Fur_Dihhel_Kobaia
Blum_Tendiwa
Wohldunt_Mem_Deweless
Wainsaht
Wlasik_Steuhn_Kobaia
Sehnnteht_Dros_Wurdah_Sums
C_est_la_Vie_Qui_les_A_Menes_La
Ek_Sun_Da_Zess
De_Zeuhl_Undazir
# names hhai
Kohntark
Emehnteht_Re
Hhai
Kobah
Lihns
Da_Zeuhl_Worts_Mekanik
Mekanik_Zain
# names attahk
The_Last_Seven_Minutes
Spiritual
Rinde
Liriik_Necronomicus_Kanth
Maahnt
Dondai
Nono
# names udu_wudu
Udu_Wudu
Weidorje
Troller_Tanz
Soleil_d_Ork
Zombies
De_Futura
Emehnteht_Re
# names merci
Call_From_The_Dark
Otis
Do_The_Music
I_Must_Return
Eliphas_Levi
The_Night_We_Died
# names floe_essi
Floe_Essi
Ektah
# names ka
Ka_I
Ka_II
Ka_III
# names emehntehtt_re
Emehntehtt_Re_I
Emehntehtt_Re_II
Emehntehtt_Re_III
Emehntehtt_Re_IV
Funehrarium_Kanht
Sehe
# names felicite_thosz
Ekmah
Elss
Dzoi
Nums
Teha
Waahrz
Duhl
Tsai
Ohst
Zahrr
Les_Hommes_Sont_Venus\
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


