""" ROOT_URLCONF for tests """
from django.conf.urls import url

from django_sites_extensions.tests import views


urlpatterns = [
    url(r'^$', views.test),
]
