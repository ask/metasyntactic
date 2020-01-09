#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import codecs

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup  # noqa

from distutils.command.install import INSTALL_SCHEMES

os.environ["MS_NO_EVAL"] = "yes"
import metasyntactic
os.environ.pop("MS_NO_EVAL", None)
sys.modules.pop("metasyntactic", None)

packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir != '':
    os.chdir(root_dir)
src_dir = "metasyntactic"


def fullsplit(path, result=None):
    if result is None:
        result = []
    head, tail = os.path.split(path)
    if head == '':
        return [tail] + result
    if head == path:
        return result
    return fullsplit(head, [tail] + result)


for scheme in list(INSTALL_SCHEMES.values()):
    scheme['data'] = scheme['purelib']

for dirpath, dirnames, filenames in os.walk(src_dir):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith("."):
            del dirnames[i]
    for filename in filenames:
        if filename.endswith(".py"):
            packages.append('.'.join(fullsplit(dirpath)))
        else:
            data_files.append([dirpath, [os.path.join(dirpath, f) for f in
                filenames]])

if os.path.exists("README.rst"):
    long_description = codecs.open('README.rst', "r", "utf-8").read()
else:
    long_description = "See http://pypi.python.org/pypi/metasyntactic"

setup(
    name='metasyntactic',
    version=metasyntactic.__version__,
    description=metasyntactic.__doc__,
    author=metasyntactic.__author__,
    author_email=metasyntactic.__contact__,
    url=metasyntactic.__homepage__,
    platforms=["any"],
    packages=packages,
    data_files=data_files,
    zip_safe=False,
    test_suite="nose.collector",
    install_requires=['six'],
    tests_require=[],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: Artistic License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.5",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Utilities",
        "Topic :: Religion",
        "Topic :: Other/Nonlisted Topic",
        "Topic :: Internet :: Name Service (DNS)",
        "Topic :: Games/Entertainment :: Fortune Cookies",
        "Topic :: Documentation",
        "Topic :: Communications :: Usenet News",
        "Topic :: Communications :: Chat",
        "Topic :: Artistic Software",
        "Programming Language :: Perl",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries :: Perl Modules",
    ],
    entry_points={
        #"console_scripts": ["cl = cl.bin.cl:main"],
    },
    long_description=long_description,
)
