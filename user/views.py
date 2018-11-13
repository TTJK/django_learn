from django.shortcuts import redirect

# Create your views here.

from django.http import HttpResponse
from django.urls import reverse


def index(request):
    return HttpResponse("hello,wolrd!")



def response_redirect(request):
    return redirect(reverse("user:index"))