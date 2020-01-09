# -*- coding: utf-8 -*-
'''

##########################
Acme::MetaSyntactic::amber
##########################

****
NAME
****


Acme::MetaSyntactic::amber - The Amber theme


***********
DESCRIPTION
***********


This theme pays homage to the 10-book Amber fantasy series,
written by Roger Zelazny. The list contains names of
characters, things and places from the series, as well as the name
of the author.


***********
CONTRIBUTOR
***********


Offer Kaye


*******
CHANGES
*******



- \*
 
 2012-05-07 - v1.000
 
 Received its own version number in Acme-MetaSyntactic-Themes version 1.000.
 


- \*
 
 2005-04-18
 
 Introduced in Acme-MetaSyntactic version 0.18.
 


- \*
 
 2005-03-23
 
 Submitted by Offer Kaye.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'amber'
DATA = '''\
# names
Amber Arbor_House Arden Arkans Arthur Avalon Avernus Bances Bayle
Baylesport Begma Belissa_Minobee Benedict Bill_Roth Bleys Borel Borquist
Brand Cabra Cade Caine Chinaway Clarissa Coral Corwin Courts_of_Chaos
Cymnea Dalt Dan_Martinez Dara Dave Deela Deiga Delwin Dertha_Gannel
Despil Dierdre Dik Doyle Dretha_Gannel Droppa_Ma_Pantz Dworkin Dybele
Ed_Wellen Eregnor Eric Faiella_Bionin Ferla_Quist Finndo Fiona Flora
Frakir Gail_Lampron Ganelon Garnath_Valley George_Hansen Gerard Ghostweel
Gilva Glait Glemdenning Gramble Grayswandir Gride Grove_Of_The_Unicorn
Gryll Harla Heerat Hendon Hugi Isles_Of_The_Sun Jamie Jasra Jasrick
Jaston Jidrash John Jopin Julia Julian Jurt Kasman Kergma Kinta Kolvir
Lancelot Larsus_Minobee Lintra Llewella Logrus Lorraine Luke Mandor Martin
Meg_Delvin Melkin Menillan Merlin Michel_Focault Mirelle Moins Moire
Morganthe Morgenstern Moris_Bailey Nayda Oberon Oisen Orguz Osric Pattern
Paulette Random Rebma Rein Rhanda Rick_Kinsky Rilga Rinaldo Roderick
Roger Roger_Zelazny Rolovians Sand Sawall Scrof Sharu_Garul Snake Star
Strygalldwir Suhuy Swayvill Tecys Texorami Thoben Tir_na_Nogth Tmer Tubble
Unicorne Uther Vialle Victor_Melman Vinta_Bayle Werewindle Wixer Ygg\
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


