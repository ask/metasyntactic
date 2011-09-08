# -*- coding: utf-8 -*-
'''
.. highlight:: perl


###########################
Acme::MetaSyntactic::batman
###########################

****
NAME
****


Acme::MetaSyntactic::batman - The batman theme


***********
DESCRIPTION
***********


The fight sound effects from the 60s serial.

All the bat sounds come from this page:
`http://www.usfamily.net/web/wpattinson/otr/batman/batfight.htm <http://www.usfamily.net/web/wpattinson/otr/batman/batfight.htm>`_

You can find photos of the serie's onomatopoeias here:
`http://www.batmania.com.ar/paginas/serie_onomatopeyas.htm <http://www.batmania.com.ar/paginas/serie_onomatopeyas.htm>`_.


***********
CONTRIBUTOR
***********


Philippe Bruhat.

Introduced in version 0.01, published on January 14, 2005.


********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'batman'
DATA = '''\
# names
aieee       aiieee    awk         awkkkkkk
bam         bang      bang_eth    bap
biff        bloop     blurp       boff
bonk        clange    clank       clank_est
clash       clunk     clunk_eth   crash
crr_aaack   crraack   cr_r_a_a_ck crunch
crunch_eth  eee_yow   flrbbbbb    glipp
glurpp      kapow     kayo        ker_plop
ker_sploosh klonk     krunch      ooooff
ouch        ouch_eth  owww        pam
plop        pow       powie       qunckkk
rakkk       rip       slosh       sock
spla_a_t    splatt    sploosh     swa_a_p
swish       swoosh    thunk       thwack
thwacke     thwape    thwapp      touche
uggh        urkk      urkkk       vronk
whack       whack_eth wham_eth    whamm
whap        zam       zamm        zap
zapeth      zgruppp   zlonk       zlopp
zlott       zok       zowie       zwapp
z_zwap      zzzzzwap\
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


