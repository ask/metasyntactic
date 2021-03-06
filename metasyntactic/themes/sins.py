# -*- coding: utf-8 -*-
'''

'''

name = 'sins'
DATA = '''\
# default
en
# names en
pride     greed      lust   anger  gluttony    envy     laziness
# names nl
ijdelheid gierigheid lust   wraak  vraatzucht  jaloezie traagheid
# names fr
orgueil   avarice    luxure colere gourmandise envie    paresse\
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


