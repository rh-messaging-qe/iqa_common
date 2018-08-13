# -*- coding: utf-8 -*-


"""setup.py: setuptools control."""

from setuptools import setup

setup(
    name='iqa_common',
    version='0.1.1',
    packages=['iqa_common'],
    license='Apache 2.0',
    description='',
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    install_requires=[
        '',
    ],
    url='https://github.com/rh-messaging-qe/iqa_common',
    author='Dominik Lenoch',
    author_email='dlenoch@redhat.com'
)
