Part of `edX code <http://code.edx.org/>`_.

edx-django-sites-extensions  |CI|_ |Codecov|_
=================================================
.. |CI| image:: https://github.com/edx/edx-django-sites-extensions/workflows/Python%20CI/badge.svg?branch=master
.. _CI: https://github.com/edx/edx-django-sites-extensions/actions?query=workflow%3A%22Python+CI%22

.. |Codecov| image:: http://codecov.io/github/edx/edx-django-sites-extensions/coverage.svg?branch=master
.. _Codecov: http://codecov.io/github/edx/edx-django-sites-extensions?branch=master


This package includes extensions to the Django "sites" framework
used by Open edX Django IDAs (independently deployable applications).

Overview
--------

In order to support multitenancy in an IDA, it is helpful to make use of
the `Django "sites" framework <https://docs.djangoproject.com/en/1.9/ref/contrib/sites/>`_.

One shortcoming of the Django "sites" framework is the fact that the CurrentSiteMiddleware
provided by the framework that adds the current site to incoming requests does not allow
you to fall back to a site that you can configure in settings in case the current site
cannot be determined from the host of the incoming request.

The Django app provided by this package overcomes this issue by monkey patching the
django.contrib.sites.models.SiteManager.get_current() function which is called by the
CurrentSiteMiddleware to determine the current site. The patched version of this function
will first try to determine the current site by checking the host of the incoming request
and attempting to match a site by domain. If a site cannot be found this way, it will fall
back to the default site configured by setting the SITE_ID setting.

Another issue with the Django "sites" framework is that it uses an in-memory cache of Site
models which makes it difficult to update models associated with the Site model via Django
admin and have those updates be reflected across all Python processes in a multi-process
application environment.

Again the Django app provided by this package monkey patches the private SiteManager query
functions that implement the in-memory caching mechanism to add a configurable timeout to
the Site cache allowing model updates to be reflected across all processes after the specified
timeout.

To enable this functionality in your Django project:

Install this package in your python environment
    ::

    $ pip install edx-django-sites-extensions

Add :code:`django.contrib.sites.middleware.CurrentSiteMiddleware` to your :code:`MIDDLEWARE_CLASSES` list.

Set the :code:`SITE_ID` setting::

    SITE_ID = 1

This package also provides a mechanism for settings up URL redirects for your application.
It makes use of the Django redirects app and provides middleware which will check for
Redirect models whose old_path field matches the path of the incoming request and redirects
those requests to the new_path of the Redirect model.

To enable this functionality in your Django project:

Install this package in your python environment
    ::

        $ pip install edx-django-sites-extensions

Add :code:`django_sites_extensions.middleware.RedirectMiddleware` to your :code:`MIDDLEWARE_CLASSES` list.

You can then use Django admin to create Redirect models.

Documentation
-------------

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

You can discuss this code in the `edx-code Google Group <https://groups.google.com/forum/#!forum/edx-code>`_.
