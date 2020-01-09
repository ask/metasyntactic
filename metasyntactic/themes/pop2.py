# -*- coding: utf-8 -*-
'''

#########################
Acme::MetaSyntactic::pop2
#########################

****
NAME
****


Acme::MetaSyntactic::pop2 - The pop2 theme


***********
DESCRIPTION
***********


This theme list all the POP2 commands, responses and states,
as listed in RFC 937.

See `http://www.ietf.org/rfc/rfc937.txt <http://www.ietf.org/rfc/rfc937.txt>`_ for details regarding
the POP2 protocol.

The history of the POP2 RFC is as follows: RFC 937 obsoletes RFC 918.
This is a much shorter history than POP3's.


***********
CONTRIBUTOR
***********


Philippe "BooK" Bruhat.


*******
CHANGES
*******



- \*
 
 2012-05-07 - v1.000
 
 Received its own version number in Acme-MetaSyntactic-Themes version 1.000.
 


- \*
 
 2006-04-03
 
 Introduced in Acme-MetaSyntactic version 0.68.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'pop2'
DATA = '''\
# names
HELO FOLD READ RETR ACKS ACKD NACK QUIT
OK Error
CALL NMBR SIZE XFER EXIT 
LSTN AUTH MBOX ITEM NEXT DONE\
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


