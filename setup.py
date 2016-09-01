#!/usr/bin/env python
"""
Setup for edx-django-sites-extensions package
"""
from setuptools import setup, find_packages


with open('README.rst') as a, open('AUTHORS') as b:
    long_description = '{}\n\n{}'.format(a.read(), b.read())

setup(
    name='edx-django-sites-extensions',
    version='2.1.0',
    description='Custom extensions for the Django sites framework',
    long_description=long_description,
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
    ],
    keywords='Django sites edx',
    url='https://github.com/edx/edx-django-sites-extensions',
    author='edX',
    author_email='oscm@edx.org',
    license='AGPL',
    packages=find_packages(exclude=['tests', '*.tests']),
    install_requires=[
        'django>=1.8,<1.9',
    ],
)
