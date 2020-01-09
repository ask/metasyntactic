# -*- coding: utf-8 -*-
'''

########################
Acme::MetaSyntactic::nis
########################

****
NAME
****


Acme::MetaSyntactic::nis - Nick Ing-Simmons


***********
DESCRIPTION
***********


Nick Ing-Simmons passed away on 25 September 2006. This is his theme.

The sad annoucement:
`http://www.nntp.perl.org/group/perl.perl5.porters/116654 <http://www.nntp.perl.org/group/perl.perl5.porters/116654>`_.


***********
CONTRIBUTOR
***********


Abigail


*******
CHANGES
*******



- \*
 
 2012-05-07 - v1.000
 
 Received its own version number in Acme-MetaSyntactic-Themes version 1.000.
 


- \*
 
 2006-10-02
 
 Introduced in Acme-MetaSyntactic version 0.94.
 


- \*
 
 2006-09-27
 
 Submitted by Abigail.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::MultiList <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aMultiList&mode=module>`_.
'''

name = 'nis'
DATA = '''\
# default
nick
# names nick
Nick Ing_Simmons NI_S pumpking perl5003_02 Tk PerlTk
# names modules
Audio Bundle_Tk Devel_Leak File_Compare Make Math_GSL Math_Rand48
PodToHTML Ptty Regexp Sys_Sysconf Tk Tk_HTML Tk_JPEG Tk_PNG\
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


