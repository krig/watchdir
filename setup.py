#!/usr/bin/env python

from distutils.core import setup

setup(name='watchdir',
      version='1.0',
      description='Watch a directory for changes using inotify',
      author='Kristoffer Gronlund',
      author_email='krig@koru.se',
      url='https://github.com/krig/watchdir',
      packages=[],
      scripts=['watchdir'],
      requires=['pyinotify']
     )
