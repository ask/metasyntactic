"""metasyntactic - Themed metasyntactic variables names"""

VERSION = (0, 99)
__version__ = ".".join(map(str, VERSION[0:3])) + "".join(VERSION[3:])
__author__ = "Ask Solem"
__contact__ = "ask@celeryproject.org"
__homepage__ = "http://github.com/ask/metasyntactic/"
__docformat__ = "restructuredtext en"

import os
import sys
if not os.environ.get("MS_NO_EVAL", False):
    from metasyntactic.themes import (all_themes, get, iterate,
                                      random, UnknownTheme)


__all__ = ["all_themes", "get", "iterate", "random", "UnknownTheme"]
