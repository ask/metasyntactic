#!/bin/bash
DEST="metasyntactic/themes"
INIT="$DEST/__init__.py"

SKIP_SOURCES="Alias.pm
              List.pm
              Locale.pm
              MultiList.pm
              RemoteList.pm
              Themes.pm
              any.pm"

INIT_CODE="
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


"

CODE="
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

"

contains() {
    found=0
    needle=$1
    haystack=$2
    for item in $haystack; do
        if [ "$item" == "$needle" ]; then
            found=1
            break
        fi
    done
    echo $found
}

mkdir -p "$DEST"
rm -f "$DEST/*.py"
> "$INIT"
echo "all_themes = set(["    >> "$INIT"

for source in $*; do
    bs=$(basename "$source")

    if [ $(contains "$bs" "$SKIP_SOURCES") == "0" ]; then
        theme=${bs%.pm}
        echo "> generating $theme..."
        echo "    '$theme',"  >> "$INIT"
        dest="$DEST/${theme}.py"
        docstring=$(pod2rst < "$source")
        data=$(perl -nle 'chomp;
                if(/^__DATA__$/){$x=1}else{print if$x}' "$source")
        echo "# -*- coding: utf-8 -*-"  >  "$dest"
        echo "'''"                      >> "$dest"
        echo "$docstring" | iconv -c -t utf-8 >> "$dest"
        echo "'''"                      >> "$dest"
        echo                            >> "$dest"

        echo "name = '$theme'"          >> "$dest"

        echo "DATA = '''\\"""           >> "$dest"
        echo "$data\\"                  >> "$dest"
        echo "'''"                      >> "$dest"
        echo "$CODE"                    >> "$dest"

    fi
done

echo "])"           >> "$INIT"
echo "$INIT_CODE"   >> "$INIT"
