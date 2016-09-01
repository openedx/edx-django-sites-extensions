Getting Started
===============
Install this package in your python environment::

    $ pip install edx-django-sites-extensions

Add :code:`django.contrib.sites.middleware.CurrentSiteMiddleware` to your :code:`MIDDLEWARE_CLASSES` list.

Set the :code:`SITE_ID` setting::

    SITE_ID = 1

Set up RedirectMiddleware
-------------------------

Add :code:`django_sites_extensions.middleware.RedirectMiddleware` to your :code:`MIDDLEWARE_CLASSES` list.

You can then use Django admin to create Redirect models.
