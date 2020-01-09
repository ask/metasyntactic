# -*- coding: utf-8 -*-
'''

##########################
Acme::MetaSyntactic::buffy
##########################

****
NAME
****


Acme::MetaSyntactic::buffy - The Buffy theme


***********
DESCRIPTION
***********


The characters from London.pm's favorite serial.
Courtesy of `http://buffyology.johnhorner.nu/ <http://buffyology.johnhorner.nu/>`_.


***********
CONTRIBUTOR
***********


Rafael Garcia-Suarez.


*******
CHANGES
*******



- \*
 
 2012-05-07 - v1.000
 
 Received its own version number in Acme-MetaSyntactic-Themes version 1.000.
 


- \*
 
 2006-05-31
 
 Mail from John Horner informing of the new address of the buffyology web site.
 


- \*
 
 2005-02-07
 
 Introduced in Acme-MetaSyntactic version 0.09.
 


- \*
 
 2005-02-04
 
 List proposed by Rafal Garcia-Suarez.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'buffy'
DATA = '''\
# names
Adam Angel Anya Buffy Cordelia Darla Dawn Drusilla Faith Giles Glory
Jenny Jonathan Joyce Kendra Oz Snyder Prof_Walsh Riley Spike Tara
The_Master The_Mayor Warren Wesley Willow Xander\
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


