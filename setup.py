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
    version='2.4.3',
    description='Custom extensions for the Django sites framework',
    long_description=long_description,
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
    ],
    keywords='Django sites edx',
    url='https://github.com/edx/edx-django-sites-extensions',
    author='edX',
    author_email='oscm@edx.org',
    license='AGPL',
    packages=['django_sites_extensions'],
    install_requires=[
        'django>=1.8,<2.0;python_version<"3"',
        'django>=1.11;python_version>"3"',
    ],
)
