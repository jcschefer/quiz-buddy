from django.shortcuts import render
from django.http import HttpResponse

from .utils import fetch_random_tossup

# Create your views here.
def random_tossup(request):
    return HttpResponse(fetch_random_tossup().toJson())
