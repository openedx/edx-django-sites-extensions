""" Tests for Django Sites framework models overrides """
import datetime

from django.contrib.sites.models import Site
from django.core.exceptions import ImproperlyConfigured
from django.http import HttpRequest
from django.test.testcases import TestCase
from django.test.utils import override_settings

from django_sites_extensions.models import SITE_CACHE_TIMEOUTS


@override_settings(SITE_ID=1)
class PatchedSiteManagerTestCase(TestCase):
    """
    Tests for the patched version of Django's SiteManager.get_current()
    """

    def setUp(self):
        super().setUp()
        self.foo_site = Site.objects.create(domain='foo.com')

    def test_site_cache_timeout_when_none(self):
        """
        Test site cache when SITE_CACHE_TIMEOUT is None for the given site.
        """
        request = HttpRequest()
        request.META['HTTP_HOST'] = self.foo_site.domain

        # Test getting current site by request host
        site = Site.objects.get_current(request)
        with self.assertNumQueries(0):
            site = Site.objects.get_current(request)

        del SITE_CACHE_TIMEOUTS[site.domain]
        with self.assertNumQueries(1):
            site = Site.objects.get_current(request)

        # Test getting current site by default site ID
        site = Site.objects.get_current()
        with self.assertNumQueries(0):
            site = Site.objects.get_current()

        del SITE_CACHE_TIMEOUTS[site.id]
        with self.assertNumQueries(1):
            site = Site.objects.get_current()

    def test_site_cache_timeout_when_expired(self):
        """
        Test site cache when SITE_CACHE_TIMEOUT is expired for the given site.
        """
        request = HttpRequest()
        request.META['HTTP_HOST'] = self.foo_site.domain
        past = datetime.datetime.utcnow() - datetime.timedelta(0, 300)

        # Test getting current site by request host
        site = Site.objects.get_current(request)
        with self.assertNumQueries(0):
            site = Site.objects.get_current(request)

        SITE_CACHE_TIMEOUTS[site.domain] = past
        with self.assertNumQueries(1):
            site = Site.objects.get_current(request)

        # Test getting current site by default site ID
        site = Site.objects.get_current()
        with self.assertNumQueries(0):
            site = Site.objects.get_current()

        SITE_CACHE_TIMEOUTS[site.id] = past
        with self.assertNumQueries(1):
            site = Site.objects.get_current()

    def test_current_site_from_request_host(self):
        """
        Test that current site can be determined from request host
        """
        request = HttpRequest()
        request.META['HTTP_HOST'] = self.foo_site.domain
        site = Site.objects.get_current(request)
        self.assertEqual(site.id, self.foo_site.id)

    def test_current_site_with_default(self):
        """
        Test that default site is used when default set is configured
        and the current site cannot be determined from the request host
        """
        request = HttpRequest()
        request.META['HTTP_HOST'] = 'bar.com'
        site = Site.objects.get_current(request)
        self.assertEqual(site.id, 1)

    def test_current_site_with_no_request(self):
        """
        Test that default site is used when no request is passed to
        SiteManager.get_current()
        """
        site = Site.objects.get_current()
        self.assertEqual(site.id, 1)

    @override_settings(SITE_ID=None)
    def test_current_site_no_default_set(self):
        """
        Test that exception is raised when no default site is defined
        and the current site cannot be determined from the request host
        """
        request = HttpRequest()
        request.META['HTTP_HOST'] = 'bar.com'
        with self.assertRaises(ImproperlyConfigured):
            Site.objects.get_current(request)
