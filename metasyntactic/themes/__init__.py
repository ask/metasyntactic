all_themes = set([
    'alphabet',
    'amber',
    'antlers',
    'barbapapa',
    'barbarella',
    'batman',
    'booze',
    'browser',
    'buffy',
    'chess',
    'colors',
    'colours',
    'constellations',
    'contrade',
    'counting_rhyme',
    'crypto',
    'currency',
    'dancers',
    'debian',
    'dilbert',
    'discworld',
    'donmartin',
    'dwarves',
    'elements',
    'facecards',
    'flintstones',
    'foo',
    'garbage',
    'garfield',
    'gems',
    'good_omens',
    'groo',
    'haddock',
    'hhgg',
    'invasions',
    'jabberwocky',
    'jamesbond',
    'jerkcity',
    'linux',
    'loremipsum',
    'lotr',
    'magic8ball',
    'magicroundabout',
    'magma',
    'metro',
    'monty_spam',
    'nis',
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
    'robin',
    'roman',
    'scooby_doo',
    'services',
    'shadok',
    'simpsons',
    'sins',
    'smtp',
    'space_missions',
    'sql',
    'stars',
    'state_flowers',
    'summerwine',
    'swords',
    'teletubbies',
    'thunderbirds',
    'tld',
    'tmnt',
    'tour_de_france',
    'trigan',
    'unicode',
    'us_presidents',
    'userfriendly',
    'vcs',
    'viclones',
    'weekdays',
    'yapc',
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



