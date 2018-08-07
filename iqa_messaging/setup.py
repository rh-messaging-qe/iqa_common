# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""

from setuptools import setup

setup(
    name='iqa-messaging',
    version='0.1.11',
    packages=['iqa-messaging'],
    license='Apache 2.0',
    description='',
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    install_requires=[
        '',
    ],
    url='https://github.com/rh-messaging-qe/',
    author='Dominik Lenoch <dlenoch@redhat.com>',
    author_email='dlenoch@redhat.com'
)
