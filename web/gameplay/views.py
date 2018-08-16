from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from data.models import Tournament, Packet

# Create your views here.


def index(request):
    return HttpResponse(get_template('gameplay/index.html').render())


def about(request):
    return HttpResponse(get_template('gameplay/about.html').render())


def guides(request):
    packets = list(Packet.objects.all().order_by('tournament', 'round_number'))

    ids_and_links = [{
        'packet_id': p.id,
        'title': '{} {}: {}'.format(p.tournament.name, p.tournament.year, p.name)
    } for p in packets]

    context = {
        'ids_and_links': ids_and_links,
    }

    return HttpResponse(get_template('gameplay/guides.html').render(context))


def play(request):
    return HttpResponse(get_template('gameplay/play.html').render())
