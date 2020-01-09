# -*- coding: utf-8 -*-
'''

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

The list was taken from the ISO web site: `http://www.iso.org/ <http://www.iso.org/>`_.


***********
CONTRIBUTOR
***********


Philippe "BooK" Bruhat.


*******
CHANGES
*******



- \*
 
 2015-08-10 - v1.005
 
 Updated the source URL, and
 published in Acme-MetaSyntactic-Themes version 1.047.
 


- \*
 
 2013-07-22 - v1.004
 
 Updated the source URL, and
 published in Acme-MetaSyntactic-Themes version 1.034.
 


- \*
 
 2013-01-14 - v1.003
 
 Updated the source URL, and
 updated from the source web site in Acme-MetaSyntactic-Themes version 1.029.
 


- \*
 
 2012-10-29 - v1.002
 
 Updated from the source web site in Acme-MetaSyntactic-Themes version 1.025.
 


- \*
 
 2012-09-10 - v1.001
 
 Updated from the source web site in Acme-MetaSyntactic-Themes version 1.018.
 


- \*
 
 2012-05-07 - v1.000
 
 Updated with historical (withdrawn) currencies, made updatable, and
 received its own version number in Acme-MetaSyntactic-Themes version 1.000.
 


- \*
 
 2005-08-23
 
 Introduced in Acme-MetaSyntactic version 0.36, published (one day late).
 



********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'currency'
DATA = '''\
# default
current
# names current
AED
AFN
ALL
AMD
ANG
AOA
ARS
AUD
AWG
AZN
BAM
BBD
BDT
BGN
BHD
BIF
BMD
BND
BOB
BOV
BRL
BSD
BTN
BWP
BYR
BZD
CAD
CDF
CHE
CHF
CHW
CLF
CLP
CNY
COP
COU
CRC
CUC
CUP
CVE
CZK
DJF
DKK
DOP
DZD
EGP
ERN
ETB
EUR
FJD
FKP
GBP
GEL
GHS
GIP
GMD
GNF
GTQ
GYD
HKD
HNL
HRK
HTG
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
LSL
LTL
LVL
LYD
MAD
MDL
MGA
MKD
MMK
MNT
MOP
MRO
MUR
MVR
MWK
MXN
MXV
MYR
MZN
NAD
NGN
NIO
NOK
NPR
NZD
OMR
PAB
PEN
PGK
PHP
PKR
PLN
PYG
QAR
RON
RSD
RUB
RWF
SAR
SBD
SCR
SDG
SEK
SGD
SHP
SLL
SOS
SRD
SSP
STD
SVC
SYP
SZL
THB
TJS
TMT
TND
TOP
TRY
TTD
TWD
TZS
UAH
UGX
USD
USN
USS
UYI
UYU
UZS
VEF
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
XFU
XOF
XPD
XPF
XPT
XSU
XTS
XUA
XXX
YER
ZAR
ZMW
ZWL
# names historic
ADP
AFA
ALK
ANG
AOK
AON
AOR
ARA
ARP
ARY
ATS
AYM
AZM
BAD
BEC
BEF
BEL
BGJ
BGK
BGL
BOP
BRB
BRC
BRE
BRN
BRR
BUK
BYB
CHC
CNX
CSD
CSJ
CSK
CYP
DDM
DEM
ECS
ECV
EQE
ESA
ESB
ESP
FIM
FRF
GEK
GHC
GHP
GNE
GNS
GQE
GRD
GWE
GWP
HRD
IDR
IEP
ILP
ILR
ISJ
ITL
LAJ
LSM
LTT
LUC
LUF
LUL
LVR
MAF
MGF
MLF
MTL
MTP
MVQ
MXP
MZE
MZM
NIC
NLG
PEH
PEI
PES
PLZ
PTE
RHD
ROK
ROL
RUR
SDD
SDG
SDP
SIT
SKK
SRG
SUR
TJR
TMM
TPE
TRL
TRY
UAK
UGS
UGW
UYN
UYP
VEB
VEF
VNC
XFO
XRE
YDD
YUD
YUM
YUN
ZAL
ZMK
ZRN
ZRZ
ZWC
ZWD
ZWN
ZWR\
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


