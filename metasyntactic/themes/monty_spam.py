# -*- coding: utf-8 -*-
'''

###############################
Acme::MetaSyntactic::monty_spam
###############################

****
NAME
****


Acme::MetaSyntactic::monty_spam - The Monty Python SPAM theme


***********
DESCRIPTION
***********


The breakfast of champions: \ *egg and bacon; egg,
sausage, and bacon; egg and SPAM; egg, bacon, and SPAM; egg, bacon,
sausage and SPAM; SPAM, bacon, sausage, and SPAM; SPAM, egg, SPAM, SPAM,
bacon, and SPAM; SPAM, SPAM, SPAM, egg, and SPAM; SPAM, SPAM, SPAM,
SPAM, SPAM, SPAM, baked beans, SPAM, SPAM, SPAM, and SPAM; or lobster
thermidor aux crevettes with a mornay sauce garnished with truffle pate,
brandy, and a fried egg on top and SPAM.*\ 

List taken from the Monthy Python spam sketch, available at
`http://www.cusd.claremont.edu/~mrosenbl/spamfiction.html#mp <http://www.cusd.claremont.edu/~mrosenbl/spamfiction.html#mp>`_.


***********
CONTRIBUTOR
***********


Philippe "BooK" Bruhat, inspired by Ricardo Signes.


*******
CHANGES
*******



- \*
 
 2012-05-07 - v1.000
 
 Received its own version number in Acme-MetaSyntactic-Themes version 1.000.
 


- \*
 
 2005-07-18
 
 Introduced in Acme-MetaSyntactic version 0.31.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'monty_spam'
DATA = '''\
# names
bacon
baked_beans
egg
egg_and_bacon
egg_and_SPAM
egg_bacon_and_SPAM
egg_bacon_sausage_and_SPAM
egg_bacon_SPAM_and_sausage
egg_bacon_SPAM_and_sausage_without_the_SPAM
egg_sausage_and_bacon
eggs
historian
lobster_thermidor_aux_crevettes_with_a_mornay_sauce_garnished_with_truffle_pate_brandy_and_a_fried_egg_on_top_and_SPAM
lovely_SPAM
Mr_Bun
Mrs_Bun
policeman
SPAM
SPAM_bacon_sausage_and_SPAM
SPAM_egg_sausage_and_SPAM
SPAM_egg_SPAM_SPAM_bacon_and_SPAM
SPAM_SPAM_SPAM_egg_and_SPAM
SPAM_SPAM_SPAM_SPAM_SPAM_SPAM_baked_beans_SPAM_SPAM_SPAM_and_SPAM
the_Green_Midget_cafe_at_Bromley
the_Hungarian
tomato
vikings
waitress
wonderful_SPAM\
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


