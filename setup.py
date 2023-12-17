# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='partition',
    version='0.0.1',
    description='Partition module for dividing main set to equal subsets',
    long_description=readme,
    author='Ömür Gültekin',
    author_email='gultekin.omur@gmail.com',
    url='',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

