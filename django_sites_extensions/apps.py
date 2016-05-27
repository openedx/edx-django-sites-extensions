""" django_sites_extensions application configuration """
from django.apps import AppConfig


class DjangoSitesExtensionsConfig(AppConfig):
    """ django_sites_extensions application configuration """
    name = 'django_sites_extensions'
    verbose_name = 'Django Sites Extensions'

    def ready(self):
        """ Set up for django_sites_extensions app """
        from django_sites_extensions import models
        from django_sites_extensions import signals
