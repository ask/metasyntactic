# -*- coding: utf-8 -*-
'''

#########################
Acme::MetaSyntactic::smtp
#########################

****
NAME
****


Acme::MetaSyntactic::smtp - The (E)SMTP commands theme


***********
DESCRIPTION
***********


Commands of the SMTP and ESMTP protocols, as described in
RFC 821 (`http://www.ietf.org/rfc/rfc821.txt <http://www.ietf.org/rfc/rfc821.txt>`_) and
RFC 2821 (`http://www.ietf.org/rfc/rfc2821.txt <http://www.ietf.org/rfc/rfc2821.txt>`_).


***********
CONTRIBUTOR
***********


Abigail


*******
CHANGES
*******



- \*
 
 2012-05-07
 
 Received its own version number in Acme-MetaSyntactic-Themes version 1.000.
 


- \*
 
 2006-03-20
 
 Introduced in Acme-MetaSyntactic version 0.66.
 


- \*
 
 2005-10-27
 
 Submitted by Abigail.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'smtp'
DATA = '''\
# names
HELO EHELO MAIL RCPT DATA SEND SOML SAML RSET VRFY EXPN HELP NOOP QUIT TURN\
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


