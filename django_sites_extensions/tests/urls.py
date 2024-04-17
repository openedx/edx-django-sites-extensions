""" ROOT_URLCONF for tests """

from django.urls import path

from django_sites_extensions.tests import views

urlpatterns = [
    path('home', views.test, name='home'),
    path('login', views.login, name='login'),
]
