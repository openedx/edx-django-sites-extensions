""" django_sites_extensions module signals """
from django.conf import settings
from django.core.cache import cache
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

# NOTE: We only setup the signal for the Redirect model if the requisite app is installed.
# This ensures we avoid errors at startup for projects that do not have the app installed.
if 'django.contrib.redirects' in settings.INSTALLED_APPS:
    from django.contrib.redirects.models import Redirect

    @receiver(post_delete, sender=Redirect)
    @receiver(post_save, sender=Redirect)
    def clear_redirect_cache(sender, instance, **kwargs):  # pylint: disable=unused-argument
        """
        Clears the Redirect cache
        """
        cache_key = f'{settings.REDIRECT_CACHE_KEY_PREFIX}-{instance.site.domain}'
        cache.delete(cache_key)
