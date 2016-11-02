#!/usr/bin/env python
"""
Setup for edx-django-sites-extensions package
"""
from setuptools import setup, find_packages


with open('README.rst') as readme:
    long_description = readme.read()

setup(
    name='edx-django-sites-extensions',
    version='2.2.0',
    description='Custom extensions for the Django sites framework',
    long_description=long_description,
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
    ],
    keywords='Django sites edx',
    url='https://github.com/edx/edx-django-sites-extensions',
    author='edX',
    author_email='oscm@edx.org',
    license='AGPL',
    packages=find_packages(exclude=['tests', '*.tests']),
    install_requires=[
        'django>=1.8,<1.11',
    ],
)
