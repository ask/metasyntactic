# -*- coding: utf-8 -*-
'''
.. highlight:: perl


#############################
Acme::MetaSyntactic::currency
#############################

****
NAME
****


Acme::MetaSyntactic::currency - The currency theme


***********
DESCRIPTION
***********


The official three-letter currency codes, as defined by ISO 4217.

The list was taken from the ISO web site:
`http://www.iso.org/iso/en/prods-services/popstds/currencycodeslist.html <http://www.iso.org/iso/en/prods-services/popstds/currencycodeslist.html>`_.


***********
CONTRIBUTOR
***********


Philippe "BooK" Bruhat.

Introduced in version 0.36, published (one day late) on August 23, 2005.


********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'currency'
DATA = '''\
# names
AED
AFN
ALL
AMD
ANG
AOA
ARS
AUD
AWG
AZM
BAM
BBD
BDT
BGN
BHD
BIF
BMD
BRL
BSD
BWP
BYR
BZD
CAD
CDF
CHF
CNY
CRC
CUP
CVE
CYP
CZK
DJF
DKK
DOP
DZD
EEK
EGP
ERN
ETB
EUR
FJD
FKP
GBP
GEL
GHC
GIP
GMD
GNF
GTQ
GYD
HKD
HNL
HRK
HUF
IDR
ILS
INR
IQD
IRR
ISK
JMD
JOD
JPY
KES
KGS
KHR
KMF
KPW
KRW
KWD
KYD
KZT
LAK
LBP
LKR
LRD
LTL
LVL
LYD
MAD
MDL
MKD
MMK
MNT
MOP
MTL
MUR
MWK
MYR
MZM
NGN
NIO
NOK
NPR
NZD
OMR
PEN
PGK
PHP
PKR
PLN
PYG
QAR
RUB
RWF
SAR
SBD
SCR
SDD
SEK
SGD
SHP
SIT
SKK
SLL
SOS
SRD
STD
SYP
SZL
THB
TJS
TMM
TND
TOP
TTD
TWD
TZS
UAH
UGX
USD
UYU
UZS
VEB
VND
VUV
WST
XAF
XAG
XAU
XBA
XBB
XBC
XBD
XCD
XDR
XFO
XFU
XOF
XPD
XPF
XPT
XTS
XXX
YER
ZAR
ZMK
ZWD\
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


