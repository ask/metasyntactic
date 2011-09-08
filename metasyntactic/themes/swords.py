# -*- coding: utf-8 -*-
'''
.. highlight:: perl


###########################
Acme::MetaSyntactic::swords
###########################

****
NAME
****


Acme::MetaSyntactic::swords - The swords theme


***********
DESCRIPTION
***********


This list gives the names of famous swords, 
historical as well as legendary and fictional.

Sources:


\*
 
 \ *Dictionary of Phrase and Fable*\ ,
 written by E. Cobham Brewer, 1898, on line at
 `http://www.bartleby.com/81/16143.html <http://www.bartleby.com/81/16143.html>`_.
 


\*
 
 `http://pages.infinit.net/celte/epees.html <http://pages.infinit.net/celte/epees.html>`_
 


\*
 
 \ *The Colour of Magic*\ , Terry Pratchett.
 



***********
CONTRIBUTOR
***********


Jean Forget.

Introduced in version 0.81, published on July 3, 2006.


********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'swords'
DATA = '''\
# names
Al_Battar
Almace
Anduril
Angurvadel
Answerrer
Aroundight
Ascalon
Balmung
Baptism
Begallta
Balisarda
Blutgang
Brinning
Caladbolg
Calad_colg
Caliburn
Cat_s_claws
Chastiefol
Chrysaor
Claidheamh_Solius
Colada
Corrougue
Courtain
Crocea_Mors
Curtana
Dainsleif
Dhu_l_Fakar
Durandal
Dyrnwyn
Ekkisax
Excalibur
Flamberge
Flamborge
Florence
Fragarach
Fusberta
Galatyn
Glamdring
Glorieuse
Graban
Gram
Greysteel
Greywand
Grimtooth
Gurthang
Hauteclaire
Haute_Claire
Halef
Hadhafang
Herrugrim
Hofud
Hrotti
Hrunting
Joyeuse
Kring
Lagulf
Leochain
Licorne
Marmadoise
Medham
Merveilleuse
Mimung
Morglay
Murgleis
Naegling
Naglhring
Nagelring
Narsil
Noralltach
Nothung
Orcrist
Philippan
Precieuse
Quern_biter
Refil
Ridill
Ringwraith
Sacho
Samsamha
Sanglamore
Sauvagine
Scalpel
Schrit
Sting
Stormbringer
Szczerbiec
Tyrfing
Tizona
Tranchera
Waske
Welsung
Zulgafar\
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


