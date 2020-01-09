# -*- coding: utf-8 -*-
'''

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

The cast, characters, and cameo lists comes from
`https://en.wikipedia.org/wiki/List_of_Batman_television_series_characters <https://en.wikipedia.org/wiki/List_of_Batman_television_series_characters>`_.


***********
CONTRIBUTOR
***********


Philippe Bruhat (BooK).


*******
CHANGES
*******



- \*
 
 2017-06-12 - v1.001
 
 Updated with the cast, characters, and cameos from the Batman television series
 in Acme-MetaSyntactic-Themes version 1.050.
 
 This update is a tribute to Adam West, who passed away on June 9, 2017.
 


- \*
 
 2012-05-07 - v1.000
 
 Received its own version number in Acme-MetaSyntactic-Themes version 1.000.
 


- \*
 
 2005-01-14
 
 Introduced in Acme-MetaSyntactic version 0.01.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'batman'
DATA = '''\
# default
onomatopoeia
# names onomatopoeia
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
z_zwap      zzzzzwap
# names cast
Adam_West
Burt_Ward
Yvonne_Craig
Alan_Napier
Neil_Hamilton
Stafford_Repp
Madge_Blake
Byron_Keith
David_Lewis
Van_Williams
Bruce_Lee
Julie_Newmar Lee_Meriwether Eartha_Kitt
Vincent_Price
Cesar_Romero
Victor_Buono
David_Wayne
George_Sanders Otto_Preminger Eli_Wallach
Burgess_Meredith
Frank_Gorshin John_Astin
Cliff_Robertson
Art_Carney
Tallulah_Bankhead
Roddy_McDowall
Liberace
Barbara_Rush
Walter_Slezak
Malachi_Throne
Rudy_Vallee
Jacques_Bergerac
Roger_C_Carmel
Ethel_Merman
Milton_Berle
Shelley_Winters
Carolyn_Jones
Zsa_Zsa_Gabor
Van_Johnson
Maurice_Evans
Michael_Rennie
Joan_Collins
Ida_Lupino
Anne_Baxter
#_names_characters
Bruce_Wayne Batman
Dick_Grayson Robin
Barbara_Gordon Batgirl
Alfred_Pennyworth
Commissioner_James_Gordon
Chief_Miles_Clancy_O_Hara
Aunt_Harriet_Cooper
Mayor_Linseed
Warden_Crichton
Britt_Reid Green_Hornet
Kato
The_Catwoman
Egghead
The_Joker
King_Tut Professor_William_McElroy
Mad_Hatter Jervis_Tetch
Mr_Freeze Art_Schivel
The_Penguin
The_Riddler
Shame
Archer
Black_Widow
Bookworm
Chandell Harry
Nora_Clavicle
Clock_King
False_Face
Lord_Marmaduke_Ffogg
Freddy_the_Fence Freddy_Touche
Colonel_Gumm
Lola_Lasagne Lulu_Schultz
Louie_the_Lilac
Ma_Parker
Marsha_Queen_of_Diamonds
Minerva
Minstrel
Puzzler
Sandman Dr_Somnambular
Siren Lorelei_Circe
Dr_Cassandra_Spellcraft
Zelda_the_Great
#_names_cameo
Jerry_Lewis
George_Cisar
Dick_Clark
Van_Williams
Bruce_Lee
Sammy_Davis_Jr
Bill_Dana Josw_Jimwnez
Howard_Duff Sam_Stone
Werner_Klemperer Colonel_Klink
Ted_Cassidy Lurch
Don_Ho
Andy_Devine Santa_Claus
Art_Linkletter
Edward_G_Robinson
Suzy_Knickerbocker Aileen_Mehle
Cyril_Lord Carpet_King\
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


