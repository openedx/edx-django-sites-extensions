""" ROOT_URLCONF for tests """

from django_sites_extensions.tests import views
from django.urls import path


urlpatterns = [
    path('home', views.test, name='home'),
    path('login', views.login, name='login'),
]
