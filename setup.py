#!/usr/bin/env python
"""
Setup for edx-django-sites-extensions package
"""
import io

from setuptools import setup


with io.open('README.rst',  encoding='utf-8') as readme:
    long_description = readme.read()

setup(
    name='edx-django-sites-extensions',
    version='2.5.0',
    description='Custom extensions for the Django sites framework',
    long_description=long_description,
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
    ],
    keywords='Django sites edx',
    url='https://github.com/edx/edx-django-sites-extensions',
    author='edX',
    author_email='oscm@edx.org',
    license='AGPL',
    packages=['django_sites_extensions'],
    install_requires=[
        'django>=2.2,<2.3',
    ],
)
