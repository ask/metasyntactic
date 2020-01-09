# -*- coding: utf-8 -*-
'''

###############################
Acme::MetaSyntactic::magic8ball
###############################

****
NAME
****


Acme::MetaSyntactic::magic8ball - The magic8ball theme


***********
DESCRIPTION
***********


The legendary fortune-telling toy, in yet another computer
programmed incarnation, this time using Acme::MetaSyntactic!

This metasyntactic Magic 8 Ball may be nice, even useful for
important choices in your life, but be sure to ask the Public
8 Ball as well: `http://8ball.federated.com/ <http://8ball.federated.com/>`_.

The Magic 8 Ball answers list can be found here
`http://www.fiendation.com/people/chris/eight.htm <http://www.fiendation.com/people/chris/eight.htm>`_ and here
`http://www.brtb.com/articles/magic8index.shtml <http://www.brtb.com/articles/magic8index.shtml>`_ and here
`http://8ball.ofb.net/answers.html <http://8ball.ofb.net/answers.html>`_.


***********
CONTRIBUTOR
***********


Philippe "BooK" Bruhat.


*******
CHANGES
*******



- \*
 
 2012-05-07 - v1.000
 
 Received its own version number in Acme-MetaSyntactic-Themes version 1.000.
 


- \*
 
 2005-05-30
 
 Corrected (4 items were missing)
 in Acme-MetaSyntactic version 0.24.
 


- \*
 
 2005-04-25
 
 Introduced in Acme-MetaSyntactic version 0.19.
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'magic8ball'
DATA = '''\
# names
As_I_See_It_Yes
Ask_Again_Later
Better_Not_Tell_You_Now
Cannot_Predict_Now
Concentrate_and_Ask_Again
Don_t_Count_On_It
It_Is_Certain
It_Is_Decidedly_So
Most_Likely
My_Reply_Is_No
My_Sources_Say_No
Outlook_Good
Outlook_Not_So_Good
Reply_Hazy_Try_Again
Signs_Point_to_Yes
Very_Doubtful
Without_a_Doubt
Yes
Yes_Definitely
You_May_Rely_On_It\
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


