#!/usr/bin/env python

from setuptools import setup, find_packages
from jubaweather.version import get_version

setup(
    name             = 'jubaweather',
    version          = get_version(),
    description      = 'regression analysis of the weather',
    packages         = find_packages(),
    install_requires = [
        'pyyaml',
        'jubatus',
    ],
    entry_points     = {
        'console_scripts': [
            'jubaweather = jubaweather.main:main',
        ]
    },
)
