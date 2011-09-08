# -*- coding: utf-8 -*-
'''
.. highlight:: perl


########################
Acme::MetaSyntactic::vcs
########################

****
NAME
****


Acme::MetaSyntactic::vcs - The vcs theme


***********
DESCRIPTION
***********


This theme lists popular (and not so popular) Version Control systems.


***********
CONTRIBUTOR
***********


Éric Cholet

Introduced in version 0.91, published on September 11, 2006.

Updated by Abigail in version 0.92, published on September 18, 2006.


********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'vcs'
DATA = '''\
# names
accurev
aegis
aldon_lifecycle_manager
alienbrain
allchange
allfusion_harvest_change_manager
arch
archipel
arx
asvcs
bazaar
bazaar_ng
bitkeeper
bky
changelogic
clearcase
code_co_op
codeville
cogito
controltier
CS_RCS
CSSC
cvs
cvsnt
cvs_suite
darcs
dcvs
dvs
evolution
fastcst
gat
git
ic_manage
jedi_vcs
katie
m_files
matrixone
mecasp
mercurial
meta_cvs
MKS
monotone
opencm
opencvs
Perforce
prcs
projector
QVCS
quilt
razor
RCS
rmtrcs
sccs
sdf
serena_changeman
serena_version_manager
siveco
slash_briefcase
snapshotcm
so6
sourceanywhere
sourcehaven
sourcejammer
starteam
stellation
surround_SCM
svk
Subversion
superversion
team_foundation_server
teamware
telelogic_synergy
TLIB
truechange
vault
vesta
Visual_SourceSafe
workshare_professional\
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


