# -*- coding: utf-8 -*-
'''

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


************
CONTRIBUTORS
************


ric Cholet, Abigail.


*******
CHANGES
*******



- \*
 
 2012-05-14 - v1.001
 
 Updated with an \ ``=encoding``\  pod command in version 1.001,
 published on May 14,2012
 


- \*
 
 2012-05-07 - v1.000
 
 Received its own version number in Acme-MetaSyntactic-Themes version 1.000,
 published on May 7, 2012.
 


- \*
 
 2006-09-18
 
 Updated by Abigail in Acme-MetaSyntactic version 0.92.
 


- \*
 
 2006-09-11
 
 Introduced in Acme-MetaSyntactic version 0.91.
 


- \*
 
 2006-06-29
 
 Initial list proposed by ric Cholet.
 



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


