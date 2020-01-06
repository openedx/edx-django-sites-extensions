""" Views used only for test setup """
from django.http import HttpResponse


def test(request):  # pylint: disable=unused-argument
    """ Placeholder test view """
    return HttpResponse("ok")


def login(request):  # pylint: disable=unused-argument
    """ Placeholder test view """
    return HttpResponse("login require")
