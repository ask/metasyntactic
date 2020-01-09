# -*- coding: utf-8 -*-
'''

###################################
Acme::MetaSyntactic::fabeltjeskrant
###################################

****
NAME
****


Acme::MetaSyntactic::fabeltjeskrant - Characters from the 'Fabeltjeskrant'


***********
DESCRIPTION
***********


The \ *Fabeltjeskrant*\  was a Dutch puppet animation television series, 
which appeared on and off on Dutch television between 1968 and 1995, 
for a total of 1640 episodes.

Website: `http://www.fabeltjesweb.nl/ <http://www.fabeltjesweb.nl/>`_.


***********
CONTRIBUTOR
***********


Abigail


*******
CHANGES
*******



- \*
 
 2012-06-04 - v1.000
 
 Introduced in Acme-MetaSyntactic-Themes version 1.004.
 


- \*
 
 2005-10-26
 
 Submitted by Abigail.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'fabeltjeskrant'
DATA = '''\
# names
Meneer_de_Uil       Juffrouw_Ooievaar     Lowieke_de_Vos
Meneer_de_Raaf      Bor_de_Wolf           Ed_Bever
Willem_Bever        Zoef_de_Haas          Stoffel_de_Schildpad
Momfer_de_Mol       Truus_de_Mier         Gerrit_de_Postduif
Meindert_het_Paard  Myra_Hamster          Martha_Hamster
Woefdram            Isadora_Paradijsvogel Greta_Bontekoe
Piet_de_Pad
Chico_Lama          Zaza_Zebra            John_Maraboe

Droes_de_Beer       Jodocus_de_Marmot     Teun_Stier
Oleta_Vulpecula     Harry_Lepelaar        Tijl_Schavuit
Sjefke_Schelm       Rocus_de_Vrije_Vogel  Pepijn_de_Kater
Timme_de_Hond       Plons_de_Kikvors      Blinkert_de_Bliek
Arthur_de_Leeuw     Flora_Nachtegaal      George_de_Wezel
Stokebrand_de_Mug   Mia_de_Muilezel       Maup_de_Muis
Marius_de_Bok       Irma_de_Krekel        Orm_de_Aap
Toeter_de_Olifant   Kirreke_de_Tortelduif Koer_de_Tortelduif
Frija_Forel         Greta_2               Hondje_Woef
Wasa_de_Beer        Melis_Das             Lamaar_Snoespoes
Woef_Hektor         Wip_de_Eekhoorn       Gies_de_Vlieg
Arie_de_Rat         Borita                Cas_de_Kraai
Asa_de_Spin\
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


