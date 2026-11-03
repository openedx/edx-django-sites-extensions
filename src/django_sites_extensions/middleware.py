"""
Django middleware extensions for Open edX
"""
from django.conf import settings
from django.core.cache import cache
from django.contrib.redirects.models import Redirect
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class RedirectMiddleware(MiddlewareMixin):
    """
    Redirects requests for URLs persisted using the django.contrib.redirects.models.Redirect model.
    """
    def process_request(self, request):
        """
        Redirects the current request if there is a matching Redirect model
        with the current request URL as the old_path field.
        """
        site = request.site
        cache_key = f'{settings.REDIRECT_CACHE_KEY_PREFIX}-{site.domain}'
        redirects = cache.get(cache_key)
        if redirects is None:
            redirects = {redirect.old_path: redirect.new_path for redirect in Redirect.objects.filter(site=site)}
            cache.set(cache_key, redirects, settings.REDIRECT_CACHE_TIMEOUT)
        redirect_to = redirects.get(request.path)
        if redirect_to:
            return redirect(redirect_to, permanent=True)
        return None
