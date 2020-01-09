# -*- coding: utf-8 -*-
'''

##########################
Acme::MetaSyntactic::stars
##########################

****
NAME
****


Acme::MetaSyntactic::stars - The stars theme


***********
DESCRIPTION
***********


A list of traditional star names, as listed on
`http://en.wikipedia.org/wiki/List_of_traditional_star_names <http://en.wikipedia.org/wiki/List_of_traditional_star_names>`_.


***********
CONTRIBUTOR
***********


Rafal Garcia-Suarez.


*******
CHANGES
*******



- \*
 
 2012-05-07 - v1.000
 
 Received its own version number in Acme-MetaSyntactic-Themes version 1.000.
 


- \*
 
 2005-09-12
 
 Introduced in Acme-MetaSyntactic version 0.39.
 


- \*
 
 2005-08-24
 
 Wikipedia link provided by Rafal Garcia-Suarez, helpfully providing ideas.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'stars'
DATA = '''\
# names
Acamar Achernar Acrux Acubens Adhafera Adhara Agena Albali Albireo Alcor
Alcyone Aldebaran Alderamin Alfirk Algedi Algenib Algieba Algol Algorab
Alhena Alioth Alkaid Alkalurops Alkes Almach Alnilam Alnitak Alphard
Alphecca Alpheratz Alshain Altair Altais Alterf Aludra Alula_Australis
Alula_Borealis Alya Ancha Ankaa Antares Arcturus Arkab Arneb Ascella
Aspidiske Asterope Atik Atlas Atria Avior Azha Baten_Kaitos Becrux Beid
Bellatrix Benetnasch Betelgeuse Canopus Capella Caph Castor Celaeno Chara
Cheleb Chertan Chort Cursa Dabih Deneb Deneb_Algedi Deneb_Kaitos Denebola
Diphda Dnoces Dschubba Dubhe Edasich Electra Elnath Eltanin Enif Errai
Fomalhaut Furud Gacrux Gomeisa Graffias Grumium Hadar Hamal Homam Izar
Kaus_Australis Kaus_Borealis Kaus_Media Keid Kitalpha Kochab Kornephoros
Lesath Maia Marfik Markab Matar Mebsuta Media Megrez Meissa Mekbuda
Menkab Menkalinan Menkar Menkent Merak Merope Mesarthim Miaplacidus Mimosa
Mintaka Mira Mirach Mirfak Mirzam Mizar Mothallah Muhlifain Muscida Naos
Nashira Navi Nekkar Nihal Nunki Nusakan Peacock Phact Phad Phecda Pherkad
Pleione Polaris Pollux Porrima Procyon Propus Pulcherrima Rasalgethi
Rasalhague Rastaban Regor Rigel Rigil_Kentaurus Rotanev Ruchba Ruchbah
Rukbat Sabik Sadalbari Sadalmelik Sadalsuud Sadatoni Sadr Saiph Sargas
Scheat Schedar Seginus Shaula Sheliak Sheratan Sirius Situla Skat Spica
Sualocin Suhail Sulafat Syrma Talitha Tania_Australis Tania_Borealis
Tarazed Taygeta Tegmine Thuban Unukalhai Vega Vindemiatrix Wasat Wezen
Yed_Posterior Yed_Prior Yildun Zaniah Zaurak Zavijava Zubenelakrab
Zubenelgenubi Zubeneschamali\
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


