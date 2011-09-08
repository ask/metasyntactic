# -*- coding: utf-8 -*-
'''
.. highlight:: perl


########################
Acme::MetaSyntactic::tld
########################

****
NAME
****


Acme::MetaSyntactic::tld - The Top-Level Domain theme


***********
DESCRIPTION
***********


The list of top-level domainnames.

The source for the list is
`http://www.ics.uci.edu/pub/websoft/wwwstat/country-codes.txt <http://www.ics.uci.edu/pub/websoft/wwwstat/country-codes.txt>`_


***********
CONTRIBUTOR
***********


Idea by Scott Lanning (who suggested ISO 3166 country codes).

Introduced in version 0.06, published on January 18, 2005.


********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'tld'
DATA = '''\
# names
ad ae af ag ai al am an ao aq ar as at au aw ax az ba bb bd be bf bg bh
bi bj bm bn bo br bs bt bv bw by bz ca cc cd cf cg ch ci ck cl cm cn co
cr cs cu cv cx cy cz de dj dk dm do dz ec ee eg eh er es et fi fj fk fm
fo fr fx ga gb gd ge gf gh gi gl gm gn gp gq gr gs gt gu gw gy hk hm hn
hr ht hu id ie il in io iq ir is it jm jo jp ke kg kh ki km kn kp kr kw
ky kz la lb lc li lk lr ls lt lu lv ly ma mc md mg mh mk ml mm mn mo mp
mq mr ms mt mu mv mw mx my mz na nc ne nf ng ni nl no np nr nu nz om pa
pe pf pg ph pk pl pm pn pr ps pt pw py qa re ro ru rw sa sb sc sd se sg sh
si sj sk sl sm sn so sr st su sv sy sz tc td tf tg th tj tk tl tm tn to tp
tr tt tv tw tz ua ug uk um us uy uz va vc ve vg vi vn vu wf ws ye yt yu za
zm zr zw biz com edu gov int mil net org pro aero arpa coop info name nato\
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


