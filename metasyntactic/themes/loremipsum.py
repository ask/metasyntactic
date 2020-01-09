# -*- coding: utf-8 -*-
'''

###############################
Acme::MetaSyntactic::loremipsum
###############################

****
NAME
****


Acme::MetaSyntactic::loremipsum - The Lorem Ipsum theme


***********
DESCRIPTION
***********


Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
commodo consequat. Duis aute irure dolor in reprehenderit in voluptate
velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat
cupidatat non proident, sunt in culpa qui officia deserunt mollit anim
id est laborum.

Confer `http://www.lipsum.com/ <http://www.lipsum.com/>`_.


***********
CONTRIBUTOR
***********


Jrme Fenal.


*******
CHANGES
*******



- \*
 
 2012-05-14 - v1.001
 
 Updated with an \ ``=encoding``\  pod command
 in Acme-MetaSyntactic-Themes version 1.001.
 


- \*
 
 2012-05-07 - v1.000
 
 Received its own version number in Acme-MetaSyntactic-Themes version 1.000.
 


- \*
 
 2005-03-14
 
 Introduced in Acme-MetaSyntactic version 0.13.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'loremipsum'
DATA = '''\
# names
lorem ipsum dolor sit amet consectetur adipisicing elit sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua enim ad minim veniam
quis nostrud exercitation ullamco laboris nisi aliquip ex ea commodo
consequat duis aute irure in reprehenderit voluptate velit esse cillum
eu fugiat nulla pariatur excepteur sint occaecat cupidatat non proident
sunt culpa qui officia deserunt mollit anim id est laborum

perspiciatis unde omnis iste natus error voluptatem accusantium doloremque
laudantium totam rem aperiam eaque ipsa quae ab illo inventore veritatis
quasi architecto beatae vitae dicta explicabo nemo ipsam quia voluptas
aspernatur aut odit fugit consequuntur magni dolores eos ratione sequi
nesciunt neque porro quisquam dolorem adipisci numquam eius modi tempora
incidunt magnam aliquam quaerat minima nostrum exercitationem ullam
corporis suscipit laboriosam aliquid commodi consequatur autem vel eum
iure quam nihil molestiae illum quo

at vero accusamus iusto odio dignissimos ducimus blanditiis praesentium
voluptatum deleniti atque corrupti quos quas molestias excepturi occaecati
cupiditate provident similique mollitia animi dolorum fuga harum quidem
rerum facilis expedita distinctio nam libero tempore cum soluta nobis
eligendi optio cumque impedit minus quod maxime placeat facere possimus
assumenda repellendus temporibus quibusdam officiis debitis necessitatibus
saepe eveniet voluptates repudiandae recusandae itaque earum hic tenetur
a sapiente delectus reiciendis voluptatibus maiores alias perferendis
doloribus asperiores repellat\
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


