Getting Started
===============
Install this package in your python environment:

.. code-block:: bash

    $ pip install edx-django-sites-extensions

Replace :code:`django.contrib.sites.middleware.CurrentSiteMiddleware` with
:code:`django_sites_extensions.middleware.CurrentSiteWithDefaultMiddleware`.

Add default site setting to Django settings:

.. code-block:: bash

    DEFAULT_SITE_ID = 1
