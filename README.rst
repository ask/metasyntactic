######################################################
 metasyntactic - Themed metasyntactic variables names
######################################################

:Version: 1.0.14

Synopsis
========

This is a port of the excellent Perl module `Acme::MetaSyntactic`_,
written by Phillipe (BooK) Bruhat.

In fact it is automatically generated from Acme::MetaSynctacic.
And this particular version was generated from version 0.99.

The original CONTRIBUTORS file is shipped with this distribution.

.. _`Acme::MetaSyntactic`:
    http://search.cpan.org/dist/Acme-MetaSyntactic/lib/Acme/MetaSyntactic.pm

Usage
=====

General
-------

Get a list of all themes::

    >>> import metasyntactic
    >>> metasyntactic.all_themes
    set(...)


Get random theme::

    >>> metasyntactic.random()
    <module 'metasyntactic.themes.stars' from 'metasyntactic/themes/stars.py'>


Get random metavariable from random theme::

    >>> metasyntactic.random().random()
    ['Barbouille']

Get 4 random metavariables from random theme::

    >>> metasyntactic.random().random(4)
    ['eve', 'irene', 'frank', 'ellen']

Get random metavariables from 4 random themes::

    >>> [theme.random() for theme in metasyntactic.random(4)]
    ['Barbouille', 'Fragarach', 'Grumpy', 'the_Lord_of_the_Rings']

Get 2 random metavariables from 4 random themes::

    >>> [theme.random(2) for theme in metasyntactic.random(4)]
    [['Lupa', 'Civetta'],
     ['spigot', 'physique'],
     ['Patrice_Petit', 'Yvette_Chauvire'],
     ['GiNG_GiNG', 'DOINK_DOINK_DOINK_DOINK']]

Themes
------

::

    # Get theme by theme name
    >>> foo = metasyntactic.get("foo")
    >>> foo
    <module 'metasyntactic.themes.foo' from 'metasyntactic/themes/foo.py'>

    # Get random name
    >>> foo.random()
    'fubar'

    # Get several random names.
    >>> foo.random(8)
    ['bar', 'xyzzy', 'foobar', 'thud', 'foo', 'fred', 'garply', 'quux']

    # Get all names
    >>> foo.all()
    set(....)


Categories
==========

::

    # Get random name in specific category
    >>> foo.random(8, category="fr")
    ['truc', 'test1', 'machin', 'titi', 'tutu', 'pipo', 'test2', 'tata']

    # get default category
    >>> foo.default()
    'en'

    # get all available categories
    >>> foo.categories()
    set(['en', 'fr', 'nl'])

    # get all names in specific category
    >>> foo.all(category="fr")
    set(...)

    >>> yapc = metasyntactic.get("yapc")

    >>> yapc.random(4, section="america north")
    ['Buffalo', 'Pittsburgh', 'Boca_Raton', 'Saint_Louis']

    >>> yapc.sections()
    set(['america north',
         'america south',
         'asia',
         'australia',
         'brazil',
         'canada',
         'europe',
         'israel',
         'taipei'])


Installation
============

You can install `metasyntactic` either via the Python Package Index (PyPI)
or from source.

To install using `pip`,::

    $ pip install metasyntactic

To install using `easy_install`,::

    $ easy_install metasyntactic

If you have downloaded a source tarball you can install it
by doing the following,::

    $ python setup.py build
    # python setup.py install # as root


Bug tracker
===========

If you have any suggestions, bug reports or annoyances please report them
to our issue tracker at http://github.com/ask/metasyntactic/issues/

License
=======

This software is licensed under the `Artistic License`.
And I don't reserve any copyright for this work, as all the hard work
should be credited to the original authors.
