from django.shortcuts import render
from django.http import HttpResponse

from .utils import fetch_random_question

# Create your views here.
def random_question(request):
    return HttpResponse(fetch_random_question().toJson())
