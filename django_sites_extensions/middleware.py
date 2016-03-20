"""
Django sites framework middleware extensions for Open edX
"""
from django.conf import settings
from django.contrib.sites.middleware import CurrentSiteMiddleware
from django.contrib.sites.models import Site
from django.core.exceptions import ImproperlyConfigured


class CurrentSiteWithDefaultMiddleware(CurrentSiteMiddleware):
    """
    This is an extension of Django's CurrentSiteMiddleware. This extension
    allows for the specification of a default site to use in the case when
    the current site cannot be determined by examining the host of the
    incoming request.

    When using this middleware you should define a DEFAULT_SITE_ID setting
    which indicates the default site to fall back to.
    """

    def process_request(self, request):
        try:
            super(CurrentSiteWithDefaultMiddleware, self).process_request(request)
        except (Site.DoesNotExist, ImproperlyConfigured):
            site_id = getattr(settings, 'DEFAULT_SITE_ID', '')
            if site_id:
                request.site = Site.objects.get(pk=site_id)  # pylint: disable=no-member
            else:
                raise
