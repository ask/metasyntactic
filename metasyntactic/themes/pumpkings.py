# -*- coding: utf-8 -*-
'''
.. highlight:: perl


##############################
Acme::MetaSyntactic::pumpkings
##############################

****
NAME
****


Acme::MetaSyntactic::pumpkings - The pumpkings theme


***********
DESCRIPTION
***********


This is the list of the Perl Pumpkings, as listed in perlhist(1).

The names are the pumpkings PAUSE id (except for \ ``NI-S``\ , which was
changed to \ ``NI_S``\ ).


***********
CONTRIBUTOR
***********


Rafael Garcia-Suarez.

Introduced in version 0.14, published on March 21, 2005.

Turned into a multilist (separate lists for different versions of Perl)
by Abigail in version 0.74, published on May 15, 2006.


********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::MultiList <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aMultiList&mode=module>`_.
'''

name = 'pumpkings'
DATA = '''\
# default
perl5
# names perl0
lwall
# names perl1
lwall mschwern rclamp
# names perl2
lwall
# names perl3
lwall
# names perl4
lwall
# names perl5
lwall andyd tomc cbail ni_s chips timb micb gsar gbarr
jhi hvds rgarcia nwclark lbrocard\
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


