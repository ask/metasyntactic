all_themes = set([
    'abba',
    'afke',
    'alice',
    'alphabet',
    'amber',
    'antlers',
    'asterix',
    'barbapapa',
    'barbarella',
    'batman',
    'ben_and_jerry',
    'bible',
    'booze',
    'bottles',
    'browser',
    'buffy',
    'calvin',
    'camelidae',
    'care_bears',
    'chess',
    'colors',
    'colours',
    'constellations',
    'contrade',
    'counting_rhyme',
    'counting_to_one',
    'crypto',
    'currency',
    'dancers',
    'debian',
    'dilbert',
    'discworld',
    'doctor_who',
    'donmartin',
    'dwarves',
    'elements',
    'evangelion',
    'fabeltjeskrant',
    'facecards',
    'fawlty_towers',
    'flintstones',
    'french_presidents',
    'garbage',
    'garfield',
    'gems',
    'good_omens',
    'groo',
    'haddock',
    'hhgg',
    'iata',
    'icao',
    'invasions',
    'jabberwocky',
    'jamesbond',
    'jerkcity',
    'linux',
    'loremipsum',
    'lotr',
    'lucky_luke',
    'magic8ball',
    'magicroundabout',
    'magma',
    'mars',
    'metro',
    'monty_spam',
    'muses',
    'nis',
    'nobel_prize',
    'norse_mythology',
    'octothorpe',
    'olympics',
    'opcodes',
    'oulipo',
    'pantagruel',
    'pasta',
    'pause_id',
    'peanuts',
    'pgpfone',
    'phonetic',
    'pie',
    'planets',
    'pm_groups',
    'pokemon',
    'pooh',
    'pop2',
    'pop3',
    'pornstars',
    'pumpkings',
    'punctuation',
    'pynchon',
    'python',
    'quantum',
    'regions',
    'reindeer',
    'renault',
    'robin',
    'roman',
    'scooby_doo',
    'screw_drives',
    'services',
    'shadok',
    'simpsons',
    'sins',
    'smtp',
    'smurfs',
    'space_missions',
    'sql',
    'stars',
    'state_flowers',
    'summerwine',
    'swords',
    'tarot',
    'teletubbies',
    'thunderbirds',
    'tld',
    'tmnt',
    'tokipona',
    'tour_de_france',
    'trigan',
    'unicode',
    'us_presidents',
    'userfriendly',
    'vcs',
    'viclones',
    'wales_towns',
    'weekdays',
    'yapc',
    'zodiac',
    'contributors',
    'foo',
])

from importlib import import_module
from random import choice, shuffle

theme_list = list(all_themes)


class UnknownTheme(KeyError):
    pass


def get(theme):
    if theme in all_themes:
        return import_module('metasyntactic.themes.%s' % (theme, ))
    raise UnknownTheme(theme)


def iterate():
    for theme in all_themes:
        yield get(theme)


def random(n=1):
    shuffle(theme_list)
    if n == 1:
        return get(choice(theme_list))
    return [get(theme) for theme in theme_list[:n]]



