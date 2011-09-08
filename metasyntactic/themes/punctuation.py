# -*- coding: utf-8 -*-
'''
.. highlight:: perl


################################
Acme::MetaSyntactic::punctuation
################################

****
NAME
****


Acme::MetaSyntactic::punctuation - The punctuation theme


***********
DESCRIPTION
***********


Names of various punctuation marks.

This list is based on a browsing session starting from:
`http://en.wikipedia.org/wiki/Punctuation <http://en.wikipedia.org/wiki/Punctuation>`_.


***********
CONTRIBUTOR
***********


Philippe "BooK" Bruhat.

Introduced in version 0.29, published on July 4, 2005.

Updated by Abigail in version 0.91, publish on September 11, 2006.


********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'punctuation'
DATA = '''\
# names
apostrophe prime
brackets
parentheses round_brackets parens fingernails
square_brackets
curly_brackets braces
angle_brackets chevrons fishhooks
corner_brackets
comma
dash emdash endash
ellipsis suspension_points
exclamation_mark inverted_exclamation_mark
full_stop period
hyphen
interrobang
question_mark inverted_question_mark
quotation_marks single_quotes double_quotes backquotes
angle_quotes single_angle_quotes double_angle_quotes
quotation_dash
guillemets
semicolon
slash solidus
space
interpunct
colon
ampersand
asteriks
asterism
at
backslash
bullet
caret
currency
dagger
degree
number_sign octothorpe
percent_sign permille_sign
pilcrow paragraph_mark
section_mark
tilde
underscore
umlaut deaeresis
pipe vertical_bar broken_bar\
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


