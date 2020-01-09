# -*- coding: utf-8 -*-
'''

#############################
Acme::MetaSyntactic::weekdays
#############################

****
NAME
****


Acme::MetaSyntactic::weekdays - The days of the week theme


***********
DESCRIPTION
***********


Days of the week, in various languages.
(Some letters have been brutally transliterated to us-ascii.)

See `http://www.lexilogos.com/calendrier_jours.htm <http://www.lexilogos.com/calendrier_jours.htm>`_, for
many other languages.


************
CONTRIBUTORS
************


Abigail (English).

Gisbert W. Selke (Egyptian Arabic, Bulgarian, Czech, Modern Greek,
Esperanto, Gaelic, Japanese, Norwegian, Russian and Tagalog).

Philippe "BooK" Bruhat (all the others languages, many thanks to Estelle
Souche for her help with the Yiddish names).


*******
CHANGES
*******



- \*
 
 2012-05-07 - v1.000
 
 Received its own version number in Acme-MetaSyntactic-Themes version 1.000.
 


- \*
 
 2006-05-15
 
 Ten new languages added by Gisbert W. Selke
 in Acme-MetaSyntactiuc version 0.74.
 


- \*
 
 2006-01-02
 
 Made multilingual in Acme-MetaSyntactic version 0.55.
 


- \*
 
 2005-12-05
 
 Introduced in Acme-MetaSyntactic version 0.51.
 


- \*
 
 2005-10-20
 
 Submitted by Abigail (English names).
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::Locale <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aLocale&mode=module>`_.
'''

name = 'weekdays'
DATA = '''\
# default
en
# names ar_eg
yom_litnen yom_it_talat yom_il_arba yom_il_chamis yom_il_guma yom_al_sabt yom_al_hadd
# names bg
ponedelnik vtornik sryada chetvyrtyk petyk sybota nedelya
# names ca
dilluns dimarts dimecres dijous divendres dissabte diumenge
# names co
luni marti marcuri ghjovi venneri sabbatu dumenica
# names cy
llun mawrth mercher iau gwener sadwrn sul
# names cs
pondeli utery streda ctvrtek patek sobota nedele
# names de
montag dienstag mittwoch donnerstag freitag samstag sonntag
# names dk
mandag tirsdag onsdag torsdag fredag lordag sondag
# names el
devtera triti tetarti pempti paraskevi sabbato kyriaki
# names en
monday tuesday wednesday thursday friday saturday sunday
# names eo
lundo mardo merkredo jaudo vendredo sabato dimanco
# names es
lunes martes miercoles jueves viernes sabado domingo
# names et
esmapaev teisipaev kolmapaev neljapaev reede laupaev puhapaev
# names eu
astelehena asteartea asteazkena osteguna ostirala larunbata igandea
# names fi
maanantai tiistai keskiviikko torstai perjantai lauantai sunnuntai
# names fr
lundi mardi mercredi jeudi vendredi samedi dimanche
# names gd
di_luain di_mairt di_ciadain di_ardaoin di_haoine di_sathurna di_domhnaich
# names it
lunedi martedi mercoledi giovedi venerdi sabato domenica
# names ja
getsuyo kayo suiyo mokuyo kinyo doyo nichiyo
# names la
lunae martis mercurii jovis veneris saturni solis
# names lv
svetdiena pirmdiena otrdiena tresdiena ceturtdiena piektdiena sestdiena
# names nl
maandag dinsdag woensdag donderdag vrijdag zaterdag zondag
# names no
mandag tirsdag onsdag torsdag fredag lordag sondag
# names pl
poniedzialek wtorek sroda czwartek piatek sobota niedziela
# names pt
segunda_feira terca_feira quarta_feira quinta_feira sexta_feira sabado domingo
# names ru
ponedelnik vtornik sreda chetverg pyatnitsa subbota voskresene
# names se
mandag tisdag onsdag torsdag fredag lordag sondag
# names sw
jumatatu jumanne jumatano alhamisi ijumaa jumamosi jumapili
# names tl
lunes martes miyerkoles huwebes biyernes sabado linggo
# names x-pataphysical
lundi mardi mercredi jeudi vendredi samedi hunyadi dimanche
# names yi
montik dinstik mitvokh donershtik fraytik shabes zuntik\
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


