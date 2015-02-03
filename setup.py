#!/usr/bin/env python
import os
import sys

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

NAME = 'msisdn-cli'
DESCRIPTION = 'MSISDN Gateway CLI tool.'
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()
VERSION = open(os.path.join(here, 'VERSION')).read().strip()
AUTHOR = u"Mozilla (https://mozilla.org/)"
URL = u"https://github.com/mozilla-services/msisdn-cli"
CLASSIFIERS = ['Development Status :: 4 - Beta',
               'License :: OSI Approved :: Mozilla Public License 1.0 (MPL)',
               'Programming Language :: Python :: 3',
               'Programming Language :: Python :: 3.4',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 2.6',
               'Topic :: Internet :: WWW/HTTP']
KEYWORDS = ['msisdn', 'sms', 'browserid']
PACKAGES = [NAME.replace('-', '_')]
REQUIREMENTS = [
    'setuptools',
    'six',
    'docopt',
    'requests',
    'requests-hawk',
    'PyBrowserID',
]
DEPENDENCY_LINKS = []
ENTRY_POINTS = {
    'console_scripts': [
        'msisdn-cli = msisdn_cli:main',
    ]}

if __name__ == '__main__':  # Don't run setup() when we import this module.
    setup(name=NAME,
          version=VERSION,
          description=DESCRIPTION,
          long_description=README,
          classifiers=CLASSIFIERS,
          keywords=' '.join(KEYWORDS),
          author=AUTHOR,
          url=URL,
          license='BSD',
          packages=PACKAGES,
          include_package_data=True,
          zip_safe=True,
          install_requires=REQUIREMENTS,
          dependency_links=DEPENDENCY_LINKS,
          entry_points=ENTRY_POINTS)
