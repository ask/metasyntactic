# -*- coding: utf-8 -*-
'''
.. highlight:: perl


############################
Acme::MetaSyntactic::pokemon
############################

****
NAME
****


Acme::MetaSyntactic::pokemon - The Pokémon theme


***********
DESCRIPTION
***********


List of the 493 Pokémon characters that are officially known to exist
in the franchise.

This list is based on the following wikipedia article:
`http://en.wikipedia.org/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number <http://en.wikipedia.org/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number>`_.

The Wikipedia page lists \ *English names*\ , \ *Romanisation*\  and
\ *Trademarked Romaji*\ . For each Pokémon, the named linked internaly
by Wikipedia has been chosen.


***********
CONTRIBUTOR
***********


Abigail

Introduced in version 0.56, published on January 9, 2006.

Updated in version 0.57, published on January 16, 2006.

Updated in version 0.59, published on January 30, 2006.

Updated in version 0.64, published on March 6, 2006.

Updated in version 0.82, published on July 10, 2006.

Updated in version 0.99, published on November 6, 2006.


********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'pokemon'
DATA = '''\
# names
Bulbasaur
Ivysaur
Venusaur
Charmander
Charmeleon
Charizard
Squirtle
Wartortle
Blastoise
Caterpie
Metapod
Butterfree
Weedle
Kakuna
Beedrill
Pidgey
Pidgeotto
Pidgeot
Rattata
Raticate
Spearow
Fearow
Ekans
Arbok
Pikachu
Raichu
Sandshrew
Sandslash
Nidoran_female
Nidorina
Nidoqueen
Nidoran_male
Nidorino
Nidoking
Clefairy
Clefable
Vulpix
Ninetales
Jigglypuff
Wigglytuff
Zubat
Golbat
Oddish
Gloom
Vileplume
Paras
Parasect
Venonat
Venomoth
Diglett
Dugtrio
Meowth
Persian
Psyduck
Golduck
Mankey
Primeape
Growlithe
Arcanine
Poliwag
Poliwhirl
Poliwrath
Abra
Kadabra
Alakazam
Machop
Machoke
Machamp
Bellsprout
Weepinbell
Victreebel
Tentacool
Tentacruel
Geodude
Graveler
Golem
Ponyta
Rapidash
Slowpoke
Slowbro
Magnemite
Magneton
Farfetch_d
Doduo
Dodrio
Seel
Dewgong
Grimer
Muk
Shellder
Cloyster
Gastly
Haunter
Gengar
Onix
Drowzee
Hypno
Krabby
Kingler
Voltorb
Electrode
Exeggcute
Exeggutor
Cubone
Marowak
Hitmonlee
Hitmonchan
Lickitung
Koffing
Weezing
Rhyhorn
Rhydon
Chansey
Tangela
Kangaskhan
Horsea
Seadra
Goldeen
Seaking
Staryu
Starmie
Mr_Mime
Scyther
Jynx
Electabuzz
Magmar
Pinsir
Tauros
Magikarp
Gyarados
Lapras
Ditto
Eevee
Vaporeon
Jolteon
Flareon
Porygon
Omanyte
Omastar
Kabuto
Kabutops
Aerodactyl
Snorlax
Articuno
Zapdos
Moltres
Dratini
Dragonair
Dragonite
Mewtwo
Mew
Chikorita
Bayleef
Meganium
Cyndaquil
Quilava
Typhlosion
Totodile
Croconaw
Feraligatr
Sentret
Furret
Hoothoot
Noctowl
Ledyba
Ledian
Spinarak
Ariados
Crobat
Chinchou
Lanturn
Pichu
Cleffa
Igglybuff
Togepi
Togetic
Natu
Xatu
Mareep
Flaaffy
Ampharos
Bellossom
Marill
Azumarill
Sudowoodo
Politoed
Hoppip
Skiploom
Jumpluff
Aipom
Sunkern
Sunflora
Yanma
Wooper
Quagsire
Espeon
Umbreon
Murkrow
Slowking
Misdreavus
Unown
Wobbuffet
Girafarig
Pineco
Forretress
Dunsparce
Gligar
Steelix
Snubbull
Granbull
Qwilfish
Scizor
Shuckle
Heracross
Sneasel
Teddiursa
Ursaring
Slugma
Magcargo
Swinub
Piloswine
Corsola
Remoraid
Octillery
Delibird
Mantine
Skarmory
Houndour
Houndoom
Kingdra
Phanpy
Donphan
Porygon2
Stantler
Smeargle
Tyrogue
Hitmontop
Smoochum
Elekid
Magby
Miltank
Blissey
Raikou
Entei
Suicune
Larvitar
Pupitar
Tyranitar
Lugia
Ho_oh
Celebi
Treecko
Grovyle
Sceptile
Torchic
Combusken
Blaziken
Mudkip
Marshtomp
Swampert
Poochyena
Mightyena
Zigzagoon
Linoone
Wurmple
Silcoon
Beautifly
Cascoon
Dustox
Lotad
Lombre
Ludicolo
Seedot
Nuzleaf
Shiftry
Taillow
Swellow
Wingull
Pelipper
Ralts
Kirlia
Gardevoir
Surskit
Masquerain
Shroomish
Breloom
Slakoth
Vigoroth
Slaking
Nincada
Ninjask
Shedinja
Whismur
Loudred
Exploud
Makuhita
Hariyama
Azurill
Nosepass
Skitty
Delcatty
Sableye
Mawile
Aron
Lairon
Aggron
Meditite
Medicham
Electrike
Manectric
Plusle
Minun
Volbeat
Illumise
Roselia
Gulpin
Swalot
Carvanha
Sharpedo
Wailmer
Wailord
Numel
Camerupt
Torkoal
Spoink
Grumpig
Spinda
Trapinch
Vibrava
Flygon
Cacnea
Cacturne
Swablu
Altaria
Zangoose
Seviper
Lunatone
Solrock
Barboach
Whiscash
Corphish
Crawdaunt
Baltoy
Claydol
Lileep
Cradily
Anorith
Armaldo
Feebas
Milotic
Castform
Kecleon
Shuppet
Banette
Duskull
Dusclops
Tropius
Chimecho
Absol
Wynaut
Snorunt
Glalie
Spheal
Sealeo
Walrein
Clamperl
Huntail
Gorebyss
Relicanth
Luvdisc
Bagon
Shelgon
Salamence
Beldum
Metang
Metagross
Regirock
Regice
Registeel
Latias
Latios
Kyogre
Groudon
Rayquaza
Jirachi
Deoxys
Naetle
Hayashigame
Dodaitose
Hikozaru
Moukazaru
Goukazaru
Pochama
Pottaishi
Emperte
Mukkuru
Mukubird
Mukuhawk
Bippa
Bidaru
Koroboshi
Korotokku
Kolink
Rukushio
Rentorer
Subomie
Roserade
Zugaidosu
Rampard
Tatetops
Trideps
Minomutchi
Minomadam
Garmeil
Mitsuhoney
Beequeen
Pachirisu
Buoysel
Flowsel
Cherinbo
Cherimu
Karanakushi
Toritodon
Eteboss
Fuwante
Fuwaride
Mimirol
Mimilop
Mumage
Donkarasu
Nyarmar
Bunyatto
Lisyan
Sukanpu
Sukatanku
Domira
Dotakun
Bonsly
Mime_Jr
Pinpuku
Perap
Mikaruge
Fukamaru
Gabite
Gablias
Munchlax
Riolu
Lucario
Hipopotasu
Kabarudon
Scorpi
Dorapion
Greggle
Dokurog
Muskippa
Keikouo
Neorant
Tamanta
Yukikaburi
Yukinooh
Weavile
Jibacoil
Berobelt
Dosidon
Mojanbo
Elekible
Booburn
Togekiss
Megayanma
Leafia
Glacia
Glion
Manmoo
PolygonZ
Erlade
Dainose
Yonowahru
Yukimenoko
Rotom
Yuxie
Emurit
Agnome
Dialga
Palkia
Heatran
Regigigas
Giratina
Crecelia
Phione
Manaphy
Darkrai
Sheimi
Arseus\
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


