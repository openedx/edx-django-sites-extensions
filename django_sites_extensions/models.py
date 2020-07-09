""" Django Sites framework models overrides """
import datetime

# We import models as a whole here so that we can reference models.SITE_CACHE indirectly.
# When the cache is cleared, that variable gets reassigned, and we want to notice that.
from django.contrib.sites import models

from django.contrib.sites.models import Site, SiteManager
from django.core.exceptions import ImproperlyConfigured


# Dict which maps Site id/domain to a datetime
# when the corresponding when the corresponding
# Site model cached in SITE_CACHE should be flushed.
SITE_CACHE_TIMEOUTS = {}


def get_site_cache_ttl():
    """
    Get the SITE_CACHE_TTL timedelta.

    Defaults to 5 minutes if SITE_CACHE_TTL has not been configured in application settings.
    """
    # Imported here to avoid circular import
    from django.conf import settings  # pylint: disable=import-outside-toplevel
    return datetime.timedelta(0, getattr(settings, 'SITE_CACHE_TTL', 300))


def patched_get_current(self, request=None):
    """
    Monkey patched version of Django's SiteManager.get_current() function.

    Returns the current Site based on a given request or the SITE_ID in
    the project's settings. If a request is given attempts to match a site
    with domain matching request.get_host(). If a request is not given or
    a site cannot be found based on the host of the request, we return the
    site which matches the configured SITE_ID setting.
    """
    # Imported here to avoid circular import
    from django.conf import settings  # pylint: disable=import-outside-toplevel
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


def patched_get_site_by_id(self, site_id):
    """
    Monkey patched version of Django's SiteManager._get_site_by_id() function.

    Adds a configurable timeout to the in-memory SITE_CACHE for each cached Site.
    This allows for the use of an in-memory cache for Site models, avoiding one
    or more DB hits on every request made to the Django application, but also allows
    for changes made to models associated with the Site model and accessed via the
    Site model's relationship accessors to take effect without having to manual
    recycle all Django worker processes active in an application environment.
    """
    now = datetime.datetime.utcnow()
    site = models.SITE_CACHE.get(site_id)
    cache_timeout = SITE_CACHE_TIMEOUTS.get(site_id, now)
    if not site or cache_timeout <= now:
        site = self.get(pk=site_id)
        models.SITE_CACHE[site_id] = site
        SITE_CACHE_TIMEOUTS[site_id] = now + get_site_cache_ttl()
    return models.SITE_CACHE[site_id]


def patched_get_site_by_request(self, request):
    """
    Monkey patched version of Django's SiteManager._get_site_by_request() function.

    Adds a configurable timeout to the in-memory SITE_CACHE for each cached Site.
    This allows for the use of an in-memory cache for Site models, avoiding one
    or more DB hits on every request made to the Django application, but also allows
    for changes made to models associated with the Site model and accessed via the
    Site model's relationship accessors to take effect without having to manual
    recycle all Django worker processes active in an application environment.
    """
    host = request.get_host()
    now = datetime.datetime.utcnow()
    site = models.SITE_CACHE.get(host)
    cache_timeout = SITE_CACHE_TIMEOUTS.get(host, now)
    if not site or cache_timeout <= now:
        site = self.get(domain__iexact=host)
        models.SITE_CACHE[host] = site
        SITE_CACHE_TIMEOUTS[host] = now + get_site_cache_ttl()
    return models.SITE_CACHE[host]


SiteManager.get_current = patched_get_current
SiteManager._get_site_by_id = patched_get_site_by_id  # pylint: disable=protected-access
SiteManager._get_site_by_request = patched_get_site_by_request  # pylint: disable=protected-access
