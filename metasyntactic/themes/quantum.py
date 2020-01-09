# -*- coding: utf-8 -*-
'''

############################
Acme::MetaSyntactic::quantum
############################

****
NAME
****


Acme::MetaSyntactic::quantum - The Quantum Mechanics theme


***********
DESCRIPTION
***********


This theme provides the English names of the particles from 
the standard model of quantum mechanics, plus a few composite 
particles (hadrons and mesons).

Trivia: the tau lepton was discovered in 1975 by Martin \ *Perl*\  and a
team of 30 physicists at the Stanford Positron-Electron Asymmetric Ring.
(See `http://www.pbs.org/wgbh/nova/elegant/part-nf.html <http://www.pbs.org/wgbh/nova/elegant/part-nf.html>`_)


***********
CONTRIBUTOR
***********


Sbastien Aperghis-Tramoni.


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
 
 2005-05-16
 
 Introduced in Acme-MetaSyntactic version 0.22.
 


- \*
 
 2005-03-14
 
 List proposed by Sbastien Aperghis-Tramoni.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'quantum'
DATA = '''\
# names
proton neutron delta lambda sigma xi
b_meson d_meson eta eta_prime j_psi kaon omega phi pion rho upsilon
electron positron electron_neutrino up down
muon muon_neutrino strange charm
tau tau_neutrino bottom top
photon z_zero w_plus w_minus gluon graviton higgs
selectron electron_sneutrino up_squark down_squark
muon_slepton muon_sneutrino strange_squark charm_squark
tau_slepton tau_sneutrino bottom_squark top_squark
photino neutralino zino w_plus_wino w_minus_wino
gluino gravitino higgsino\
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


