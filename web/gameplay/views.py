from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template

# Create your views here.


def index(request):
    return HttpResponse(get_template('gameplay/index.html').render())


def about(request):
    return HttpResponse(get_template('gameplay/about.html').render())


def guides(request):
    return HttpResponse(get_template('gameplay/guides.html').render())


def play(request):
    return HttpResponse(get_template('gameplay/play.html').render())
