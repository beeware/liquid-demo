#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='github',
    version='1.0.0',
    packages=find_packages(),
    author="Russell keith-Magee",
    description="A standalone app wrapper around the GitHub web interface",
    options={
        'app': {
            'formal_name': 'GitHub',
            'bundle': 'org.example'
        },
        'macos': {
            'app_requires': [
                'toga-cocoa'
            ],
            'icon': 'icons/macos',
        },
    }
)
