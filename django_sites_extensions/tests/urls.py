""" ROOT_URLCONF for tests """
from django.conf.urls import url

from django_sites_extensions.tests import views


urlpatterns = [
    url(r'^home$', views.test, name='home'),
    url(r'^login', views.login, name='login'),
]
