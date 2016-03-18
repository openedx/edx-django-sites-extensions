"""
Tests for Django sites framework middleware extensions
"""
from django.contrib.sites.models import Site
from django.http import HttpRequest
from django.test.testcases import TestCase
from django.test.utils import override_settings

from django_sites_extensions.middleware import CurrentSiteWithDefaultMiddleware


@override_settings(SITE_ID=None)
class CurrentSiteWithDefaultMiddlewareTestCase(TestCase):
    """
    Tests for the CurrentSiteWithDefaultMiddleware
    """
    def test_current_site_from_request_host(self):
        """
        Test that current site can be determined from request host
        """
        request = HttpRequest()
        request.META['HTTP_HOST'] = 'example.com'
        middleware = CurrentSiteWithDefaultMiddleware()
        middleware.process_request(request)
        self.assertEqual(request.site.id, 1)  # pylint: disable=no-member

    def test_current_site_no_default_set(self):
        """
        Test that exception is raised when no default site is defined
        and the current site cannot be determined from the request host
        """
        request = HttpRequest()
        request.META['HTTP_HOST'] = 'fake-server.com'
        middleware = CurrentSiteWithDefaultMiddleware()
        with self.assertRaises(Site.DoesNotExist):
            middleware.process_request(request)

    @override_settings(DEFAULT_SITE_ID=1)
    def test_current_site_with_default_set(self):
        """
        Test that default site is used when default set is configured
        and the current site cannot be determined from the request host
        """
        request = HttpRequest()
        request.META['HTTP_HOST'] = 'fake-server.com'
        middleware = CurrentSiteWithDefaultMiddleware()
        middleware.process_request(request)
        self.assertEqual(request.site.id, 1)  # pylint: disable=no-member
