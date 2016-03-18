Part of `edX code`__.

__ http://code.edx.org/

edx-django-sites-extensions  |Travis|_ |Codecov|_
===================================================
.. |Travis| image:: https://travis-ci.org/edx/edx-django-sites-extensions.svg?branch=master
.. _Travis: https://travis-ci.org/edx/edx-django-sites-extensions

.. |Codecov| image:: http://codecov.io/github/edx/edx-django-sites-extensions/coverage.svg?branch=master
.. Codecov: http://codecov.io/github/edx/edx-django-sites-extensions?branch=master

This package includes extensions to the Django "sites" framework
used by edX Django IDAs (independently deployable applications).

Overview (please modify)
------------------------

In order to support multitenancy in an IDA, it is helpful to make use of
the `Django "sites" framework <https://docs.djangoproject.com/en/1.9/ref/contrib/sites/>`_.

One shortcoming of the Django "sites" framework is the fact that the CurrentSiteMiddleware
provided by the framework that adds the current site to incoming requests does not allow
you to fall back to a site that you can configure in settings in case the current site
cannot be determined from the host of the incoming request.

The django_sites_extensions.middleware.CurrentSiteWithDefaultMiddleware provided by this package
extends django.contrib.sites.middleware.CurrentSiteMiddleware to allow for this use case. To enable
this functionality in your Django project::

Install this package in your python environment::

    $ pip install edx-django-sites-extensions

Replace :code:`django.contrib.sites.middleware.CurrentSiteMiddleware` with
:code:`django_sites_extensions.middleware.CurrentSiteWithDefaultMiddleware`.

Add default site setting to Django settings::

    DEFAULT_SITE_ID = 1

Documentation (please modify)
-----------------------------

The docs for edx-django-sites-extensions are on Read the Docs:  https://edx-django-sites-extensions.readthedocs.org.

License
-------

The code in this repository is licensed under LICENSE_TYPE unless
otherwise noted.

Please see ``LICENSE.txt`` for details.

How To Contribute
-----------------

Contributions are very welcome.

Please read `How To Contribute <https://github.com/edx/edx-platform/blob/master/CONTRIBUTING.rst>`_ for details.

Even though they were written with ``edx-platform`` in mind, the guidelines
should be followed for Open edX code in general.

Reporting Security Issues
-------------------------

Please do not report security issues in public. Please email security@edx.org.

Mailing List and IRC Channel
----------------------------

You can discuss this code in the `edx-code Google Group`__
__ https://groups.google.com/forum/#!forum/edx-code
