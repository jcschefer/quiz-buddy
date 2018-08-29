from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.db.models import Count
from data.models import Tournament, Packet, Keyword, KeywordTossupLinkage

# Create your views here.


def index(request):
    return HttpResponse(get_template('gameplay/index.html').render())


def about(request):
    return HttpResponse(get_template('gameplay/about.html').render())


def guides(request):
    packets = list(Packet.objects.all().order_by('tournament', 'round_number'))

    packet_ids_and_links = [{
        'packet_id': p.id,
        'title': '{} {}: {}'.format(p.tournament.name, p.tournament.year, p.name)
    } for p in packets]

    keywords = list(Keyword.objects.all().annotate(
        num_tossups=Count('keywordtossuplinkage')).order_by('-num_tossups'))

    keyword_ids_and_links = [{
        'keyword_id': k.id,
        'title': '{} ({})'.format(k.keyword, k.num_tossups)
    } for k in keywords]

    context = {
        'packet_ids_and_links': packet_ids_and_links,
        'keyword_ids_and_links': keyword_ids_and_links,
    }

    return HttpResponse(get_template('gameplay/guides.html').render(context))


def play(request):
    return HttpResponse(get_template('gameplay/play.html').render())
