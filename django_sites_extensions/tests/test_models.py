""" Tests for Django Sites framework models overrides """
from django.contrib.sites.models import Site
from django.core.exceptions import ImproperlyConfigured
from django.http import HttpRequest
from django.test.testcases import TestCase
from django.test.utils import override_settings


@override_settings(SITE_ID=1)
class PatchedSiteManagerTestCase(TestCase):
    """
    Tests for the patched version of Django's SiteManager.get_current()
    """

    def setUp(self):
        super(PatchedSiteManagerTestCase, self).setUp()
        self.foo_site = Site.objects.create(domain='foo.com')

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
