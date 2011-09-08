# -*- coding: utf-8 -*-
'''
.. highlight:: perl


#########################
Acme::MetaSyntactic::pop3
#########################

****
NAME
****


Acme::MetaSyntactic::pop3 - The pop3 theme


***********
DESCRIPTION
***********


This theme list all the POP3 commands, responses and states,
as listed in RFC 1939.

See `http://www.ietf.org/rfc/rfc1939.txt <http://www.ietf.org/rfc/rfc1939.txt>`_ for details regarding
the POP3 protocol.

The history of the POP3 RFC is as follows:
RFC 1939 obsoletes
RFC 1725, which obsoletes
RFC 1460, which obsoletes
RFC 1225, which obsoletes
RFC 1081.


***********
CONTRIBUTOR
***********


Philippe "BooK" Bruhat

Introduced in version 0.67, published on March 27, 2006.


********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'pop3'
DATA = '''\
# names
USER PASS QUIT STAT LIST RETR DELE NOOP RSET
APOP TOP UIDL
OK ERR
AUTHORIZATION TRANSACTION\
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


