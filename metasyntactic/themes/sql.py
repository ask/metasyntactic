# -*- coding: utf-8 -*-
'''
.. highlight:: perl


########################
Acme::MetaSyntactic::sql
########################

****
NAME
****


Acme::MetaSyntactic::sql - The SQL theme


***********
DESCRIPTION
***********


This list contains the list of reserved words in SQL-92.

See `http://thedailywtf.com/forums/64833/ShowPost.aspx <http://thedailywtf.com/forums/64833/ShowPost.aspx>`_
for why you need this professiona^Wenterprise list in 
\ ``Acme::MetaSyntactic``\ .


***********
CONTRIBUTOR
***********


Philippe "BooK" Bruhat

I blame Maddingue for showing me this link, and rgs for
saying: \ *IL LE FAUT*\ . I blame \ ``#perlfr``\  in general for
the existence of \ ``Acme::MetaSyntactic``\ .

Introduced in version 0.71, published on April 24, 2006.


********
SEE ALSO
********


`Acme::MetaSyntactic <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic&mode=module>`_, `Acme::MetaSyntactic::List <http://search.cpan.org/search?query=Acme%3a%3aMetaSyntactic%3a%3aList&mode=module>`_.
'''

name = 'sql'
DATA = '''\
# names
ABSOLUTE ACTION ADD ALL ALLOCATE ALTER AND ANY ARE AS ASC ASSERTION AT
AUTHORIZATION AVG BEGIN BETWEEN BIT BIT_LENGTH BOTH BY CASCADE CASCADED
CASE CAST CATALOG CHAR CHARACTER CHAR_LENGTH CHARACTER_LENGTH CHECK CLOSE
COALESCE COLLATE COLLATION COLUMN COMMIT CONNECT CONNECTION CONSTRAINT
CONSTRAINTS CONTINUE CONVERT CORRESPONDING COUNT CREATE CROSS CURRENT
CURRENT_DATE CURRENT_TIME CURRENT_TIMESTAMP CURRENT_USER CURSOR DATE
DAY DEALLOCATE DEC DECIMAL DECLARE DEFAULT DEFERRABLE DEFERRED DELETE
DESC DESCRIBE DESCRIPTOR DIAGNOSTICS DISCONNECT DISTINCT DOMAIN DOUBLE
DROP ELSE END END_EXEC ESCAPE EXCEPT EXCEPTION EXEC EXECUTE EXISTS
EXTERNAL EXTRACT FALSE FETCH FIRST FLOAT FOR FOREIGN FOUND FROM FULL GET
GLOBAL GO GOTO GRANT GROUP HAVING HOUR IDENTITY IMMEDIATE IN INDICATOR
INITIALLY INNER INPUT INSENSITIVE INSERT INT INTEGER INTERSECT INTERVAL
INTO IS ISOLATION JOIN KEY LANGUAGE LAST LEADING LEFT LEVEL LIKE LOCAL
LOWER MATCH MAX MIN MINUTE MODULE MONTH NAMES NATIONAL NATURAL NCHAR
NEXT NO NOT NULL NULLIF NUMERIC OCTET_LENGTH OF ON ONLY OPEN OPTION
OR ORDER OUTER OUTPUT OVERLAPS PAD PARTIAL POSITION PRECISION PREPARE
PRESERVE PRIMARY PRIOR PRIVILEGES PROCEDURE PUBLIC READ REAL REFERENCES
RELATIVE RESTRICT REVOKE RIGHT ROLLBACK ROWS SCHEMA SCROLL SECOND SECTION
SELECT SESSION SESSION_USER SET SIZE SMALLINT SOME SPACE SQL SQLCODE
SQLERROR SQLSTATE SUBSTRING SUM SYSTEM_USER TABLE TEMPORARY THEN TIME
TIMESTAMP TIMEZONE_HOUR TIMEZONE_MINUTE TO TRAILING TRANSACTION TRANSLATE
TRANSLATION TRIM TRUE UNION UNIQUE UNKNOWN UPDATE UPPER USAGE USER USING
VALUE VALUES VARCHAR VARYING VIEW WHEN WHENEVER WHERE WITH WORK WRITE
YEAR ZONE\
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


