""" Django Sites framework models overrides """
from django.contrib.sites.models import Site, SiteManager
from django.core.exceptions import ImproperlyConfigured


def patched_get_current(self, request=None):
    """
    Monkey patched version of Django's SiteManager.get_current() function.

    Returns the current Site based on a given request or the SITE_ID in
    the project's settings. If a request is given attempts to match a site
    with domain matching request.get_host(). If a request is not given or
    a site cannot be found based on the host of the request, we return the
    site which matches the configured SITE_ID setting.
    """
    from django.conf import settings
    if request:
        try:
            return self._get_site_by_request(request)  # pylint: disable=protected-access
        except Site.DoesNotExist:
            pass

    if getattr(settings, 'SITE_ID', ''):
        return self._get_site_by_id(settings.SITE_ID)  # pylint: disable=protected-access

    raise ImproperlyConfigured(
        "You're using the Django \"sites framework\" without having "
        "set the SITE_ID setting. Create a site in your database and "
        "set the SITE_ID setting or pass a request to "
        "Site.objects.get_current() to fix this error."
    )


SiteManager.get_current = patched_get_current
