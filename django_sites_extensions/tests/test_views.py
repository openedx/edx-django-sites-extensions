"""
Tests for views which will trigger the middleware automatically.
"""
from django.contrib.redirects.models import Redirect
from django.test.testcases import TestCase
from django.urls import reverse


class ViewsTestCase(TestCase):
    """
    Test a views.
    """

    def setUp(self):
        super(ViewsTestCase, self).setUp()
        self.home_url = reverse('home')
        self.login_url = reverse('login')

        # if there is no redirect require, it will return 200.
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)

    def test_view_with_redirect_url(self):
        """
        Test that a Redirect URL is redirected towards the new url view.
        """
        Redirect.objects.create(
            site_id=1, old_path=self.home_url, new_path=self.login_url
        )
        with self.assertNumQueries(3):
            response = self.client.get(self.home_url)
            self.assertRedirects(
                response, self.login_url, status_code=301, target_status_code=200
            )

        # checking cache with complete redirect
        with self.assertNumQueries(2):
            response = self.client.get(self.home_url, follow=True)
            self.assertEqual(response.content.decode('utf-8'), 'login require')
