""" django_sites_extensions application configuration """

from django.apps import AppConfig


class DjangoSitesExtensionsConfig(AppConfig):
    """ django_sites_extensions application configuration """
    name = 'django_sites_extensions'
    verbose_name = 'Django Sites Extensions'

    # noinspection PyUnresolvedReferences
    def ready(self):
        """ Set up for django_sites_extensions app """
        # pylint: disable=unused-variable
        # pylint: disable=unused-import
        # pylint: disable=import-outside-toplevel
        from django_sites_extensions import models
        from django_sites_extensions import signals
