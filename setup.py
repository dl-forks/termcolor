#!/usr/bin/env python
# coding: utf-8
# Copyright (c) 2008-2011 Volvox Development Team
# License: /COPYING.txt
# Author: Konstantin Lepa <konstantin.lepa@gmail.com>

import os
from distutils.core import setup
from termcolor import __version__

prjdir = os.path.dirname(__file__)

def read(filename):
    return open(os.path.join(prjdir, filename)).read()

LONG_DESC = read('README.rst') + '\nCHANGES\n=======\n\n' + read('CHANGES.rst')


setup(name='termcolor',
      version=__version__,
      description='ANSII Color formatting for output in terminal.',
      long_description=LONG_DESC,
      author='Konstantin Lepa',
      license='MIT',
      author_email='konstantin.lepa@gmail.com',
      url='http://pypi.python.org/pypi/termcolor',
      packages=['termcolor'],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Terminals'
      ]
      )
