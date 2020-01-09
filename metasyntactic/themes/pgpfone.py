# -*- coding: utf-8 -*-
'''

############################
Acme::MetaSyntactic::pgpfone
############################

****
NAME
****


Acme::MetaSyntactic::pgpfone - The PGPfone biometric word list


***********
DESCRIPTION
***********


A list of words representing binary values for use in key or signature
exchanges via speech. This is similiar to the military alphabet ("Alpha",
"Bravo", etc.) but it encodes 256 values twice into a two-syllable list and a
three-syllable list. Values are drawn alternately from each list to detect
transmission errors.

Details and the word list were drawn from this page:
`http://web.mit.edu/network/pgpfone/manual/#PGP000062 <http://web.mit.edu/network/pgpfone/manual/#PGP000062>`_


***********
CONTRIBUTOR
***********


David Golden


*******
CHANGES
*******



- \*
 
 2012-05-07 - v1.000
 
 Received its own version number in Acme-MetaSyntactic-Themes version 1.000.
 


- \*
 
 2006-06-26
 
 Introduced in Acme-MetaSyntactic version 0.80.
 


- \*
 
 2006-01-19
 
 Submitted by David Golden.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::MultiList <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aMultiList&mode=module>`_.
'''

name = 'pgpfone'
DATA = '''\
# default
:all
# names two
aardvark absurd accrue acme adrift adult afflict ahead aimless Algol
allow alone ammo ancient apple artist assume Athens atlas Aztec baboon
backfield backward basalt beaming bedlamp beehive beeswax befriend
Belfast berserk billiard bison blackjack blockade blowtorch bluebird
bombast bookshelf brackish breadline breakup brickyard briefcase Burbank
button buzzard cement chairlift chatter checkup chisel choking chopper
Christmas clamshell classic classroom cleanup clockwork cobra commence
concert cowbell crackdown cranky crowfoot crucial crumpled crusade cubic
deadbolt deckhand dogsled dosage dragnet drainage dreadful drifter dropper
drumbeat drunken Dupont dwelling eating edict egghead eightball endorse
endow enlist erase escape exceed eyeglass eyetooth facial fallout flagpole
flatfoot flytrap fracture fragile framework freedom frighten gazelle
Geiger Glasgow glitter glucose goggles goldfish gremlin guidance hamlet
highchair hockey hotdog indoors indulge inverse involve island Janus
jawbone keyboard kickoff kiwi klaxon lockup merit minnow miser Mohawk
mural music Neptune newborn nightbird obtuse offload oilfield optic orca
payday peachy pheasant physique playhouse Pluto preclude prefer preshrunk
printer profile prowler pupil puppy python quadrant quiver quota ragtime
ratchet rebirth reform regain reindeer rematch repay retouch revenge
reward rhythm ringbolt robust rocker ruffled sawdust scallion scenic
scorecard Scotland seabird select sentence shadow showgirl skullcap
skydive slingshot slothful slowdown snapline snapshot snowcap snowslide
solo spaniel spearhead spellbind spheroid spigot spindle spoilage spyglass
stagehand stagnate stairway standard stapler steamship stepchild sterling
stockman stopwatch stormy sugar surmount suspense swelter tactics talon
tapeworm tempest tiger tissue tonic tracker transit trauma treadmill
Trojan trouble tumor tunnel tycoon umpire uncut unearth unwind uproot
upset upshot vapor village virus Vulcan waffle wallet watchword wayside
willow woodlark Zulu
# names three
adroitness adviser aggregate alkali almighty amulet amusement antenna
applicant Apollo armistice article asteroid Atlantic atmosphere autopsy
Babylon backwater barbecue belowground bifocals bodyguard borderline
bottomless Bradbury Brazilian breakaway Burlington businessman butterfat
Camelot candidate cannonball Capricorn caravan caretaker celebrate
cellulose certify chambermaid Cherokee Chicago clergyman coherence
combustion commando company component concurrent confidence conformist
congregate consensus consulting corporate corrosion councilman crossover
cumbersome customer Dakota decadence December decimal designing
detector detergent determine dictator dinosaur direction disable
disbelief disruptive distortion divisive document embezzle enchanting
enrollment enterprise equation equipment escapade Eskimo everyday examine
existence exodus fascinate filament finicky forever fortitude frequency
gadgetry Galveston getaway glossary gossamer graduate gravity guitarist
hamburger Hamilton handiwork hazardous headwaters hemisphere hesitate
hideaway holiness hurricane hydraulic impartial impetus inception
indigo inertia infancy inferno informant insincere insurgent integrate
intention inventive Istanbul Jamaica Jupiter leprosy letterhead liberty
maritime matchmaker maverick Medusa megaton microscope microwave midsummer
millionaire miracle misnomer molasses molecule Montana monument mosquito
narrative nebula newsletter Norwegian October Ohio onlooker opulent
Orlando outfielder Pacific pandemic pandora paperweight paragon paragraph
paramount passenger pedigree Pegasus penetrate perceptive performance
pharmacy phonetic photograph pioneer pocketful politeness positive potato
processor prophecy provincial proximate puberty publisher pyramid quantity
racketeer rebellion recipe recover repellent replica reproduce resistor
responsive retraction retrieval retrospect revenue revival revolver
Sahara sandalwood sardonic Saturday savagery scavenger sensation sociable
souvenir specialist speculate stethoscope stupendous supportive surrender
suspicious sympathy tambourine telephone therapist tobacco tolerance
tomorrow torpedo tradition travesty trombonist truncated typewriter
ultimate undaunted underfoot unicorn unify universe unravel upcoming
vacancy vagabond versatile vertigo Virginia visitor vocalist voyager
warranty Waterloo whimsical Wichita Wilmington Wyoming yesteryear Yucatan\
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


