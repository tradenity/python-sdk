"""A setuptools based setup module for python-sdk"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from codecs import open
from os import path
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as readme_file:
    readme = readme_file.read()

with open(path.join(here, 'HISTORY.rst'), encoding='utf-8') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    'requests',
    'booby',
    'bcrypt'
]

test_requirements = [
]

setup(
    name='tradenity',
    version='0.1.1',
    description="Python SDK for the Tradenity e-commerce REST API",
    long_description=readme + '\n\n' + history,
    author="Joseph Fouad",
    author_email='tradenity@tradenity.com',
    url='https://github.com/tradenity/python-sdk',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    entry_points={
        'console_scripts': [],
        },
    include_package_data=True,
    install_requires=requirements,
    license="APACHE",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
    ],
    test_suite='tests',
    tests_require=test_requirements,
)
