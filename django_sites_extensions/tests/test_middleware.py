"""
Tests for middleware extensions
"""
from django.contrib.redirects.models import Redirect
from django.contrib.sites.models import Site
from django.http import HttpRequest, HttpResponsePermanentRedirect
from django.test.testcases import TestCase

from django_sites_extensions.middleware import RedirectMiddleware


class RedirectMiddlewareTestCase(TestCase):
    """
    Test processing a request through the RedirectMiddleware
    """

    def setUp(self):
        super(RedirectMiddlewareTestCase, self).setUp()
        self.middleware = RedirectMiddleware()
        self.site = Site.objects.get(id=1)  # pylint: disable=no-member
        self.redirect = Redirect.objects.create(site_id=1, old_path='/foo', new_path='http://example.com/bar')

    def _make_request(self, path):
        """ Creates an HttpRequest """
        request = HttpRequest()
        request.path = path
        request.site = self.site
        return request

    def test_redirect_url(self):
        """
        Test that a Redirect URL is redirected
        """
        request = self._make_request('/foo')
        response = self.middleware.process_request(request)
        self.assertEqual(response.status_code, 301)
        self.assertTrue(isinstance(response, HttpResponsePermanentRedirect))
        self.assertEqual(response.get('location'), self.redirect.new_path)

    def test_normal_url(self):
        """
        Test that a normal URL is not redirected
        """
        request = self._make_request('/bar')
        self.assertIsNone(self.middleware.process_request(request))

    def test_redirects_cached(self):
        """
        Test that Redirect models get cached
        """
        request = self._make_request('/bar')
        with self.assertNumQueries(1):
            self.middleware.process_request(request)

        request = self._make_request('/bar')
        with self.assertNumQueries(0):
            self.middleware.process_request(request)
