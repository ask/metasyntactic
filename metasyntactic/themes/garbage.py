# -*- coding: utf-8 -*-
'''

############################
Acme::MetaSyntactic::garbage
############################

****
NAME
****


Acme::MetaSyntactic::garbage - The garbage theme


***********
DESCRIPTION
***********


Rubbish synonyms to use when testing your smelly modules.

English list taken from `http://dico.isc.cnrs.fr/dico/en/search <http://dico.isc.cnrs.fr/dico/en/search>`_.
French list taken from `http://dico.isc.cnrs.fr/dico/fr/search <http://dico.isc.cnrs.fr/dico/fr/search>`_.


***********
CONTRIBUTOR
***********


Jrme Fenal.


*******
CHANGES
*******



- \*
 
 2012-05-14 - v1.001
 
 Updated with an \ ``=encoding``\  pod command
 in Acme-MetaSyntactic-Themes version 1.001.
 


- \*
 
 2012-05-07 - v1.000
 
 Received its own version number in Acme-MetaSyntactic-Themes version 1.000.
 


- \*
 
 2005-08-15
 
 Introduced in Acme-MetaSyntactic version 0.35.
 


- \*
 
 2005-03-21
 
 Submitted by Jrme Fenal.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::Locale <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aLocale&mode=module>`_.
'''

name = 'garbage'
DATA = '''\
# default
en
# names en
absurdity applesauce balderdash baloney bilge blether boloney bosh bull bullshit
claptrap cobblers debris detritus drivel dross eyewash fake folderol folly food
gadolinium gaff garbage gibber havoc hogwash humbug incongruity junk litter
maiming mess nonsense offal pandemonium refuse rigmarole rubbish rubble scoria
scraps shamble shambles slag slops swill trash tripe trumpery twaddle waffle
wander waste wish_wash wreckage
# names fr
abjection abomination alluvion avarice balayure bas_fond bassesse battitures
bauge bois boue boueux bouillasse bourbe bourbier bourre bourrier braye bris
brouillasse bruine caca camelote canaillerie charnier charogne chiure chute
cloaque cochon cochonnerie compost corruption crasse crevure crotte curure
debauche debris decharge dechet deperdition depot detritus eclaboussure eclat
ecume egout engrais entourloupette epais epave epluchure excrement fagne fange
ferraille fiente freinte fumier gabegie gachis gadoue gadouille gravelure
gringuenaude grivoiserie grossier grossierete gueuserie ignorance immondice
impurete incongruite indelicatesse inexcusable infamie injure laideur lavure lie
limon lourd macule malproprete marais marecage margouillis mechancete merde
merdier misere mortier mouise mouton nettoyure noirceur nul obscenite ordure
pacotille parcelle patine patraque perfidie perte petitesse pise poison
poudrette pouillerie pourriture poussiere propos pus raclure ramas rebut
recrement relief reliquat residu rincure rogaton rognure rosserie rossignol
ruine ruisseau sabot salaud salete salissure salope saloperie sanie scorie
sediment sentine sordidite souillure stupre tache tare terreau toc tour tourbe
trivialite truand turpitude vacherie vase vaurien vermine vice vidange
vidure vilenie voirie vouerie water_closets \
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


