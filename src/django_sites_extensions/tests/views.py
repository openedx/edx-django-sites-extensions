""" Views used only for test setup """
from django.http import HttpResponse


def test(request):
    """ Placeholder test view """
    return HttpResponse("ok")


def login(request):
    """ Placeholder test view """
    return HttpResponse("login require")
