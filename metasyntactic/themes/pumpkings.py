# -*- coding: utf-8 -*-
'''

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


*******
CHANGES
*******



- \*
 
 2012-05-07 - v1.000
 
 Updated with new pumpkings since 2006, and
 received its own version number in Acme-MetaSyntactic-Themes version 1.000.
 


- \*
 
 2006-05-15
 
 Turned into a multilist (separate lists for different versions of Perl)
 by Abigail in Acme-MetaSyntactic version 0.74.
 


- \*
 
 2005-03-21
 
 Introduced in Acme-MetaSyntactic version 0.14.
 



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
lwall andyd
# names perl5
lwall andyd tomc cbail ni_s chips timb micb gsar gbarr
jhi hvds rgarcia nwclark lbrocard jesse rjbs
dapm mstrout shay miyagawa bingos dagolden flora zefram
avar stevan drolsky corion abigail\
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


