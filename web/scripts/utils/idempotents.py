from data.models import Tournament, Packet, Tossup, Keyword, KeywordTossupLinkage
from .keywords import get_tossup_keywords

'''
Only adds objects into the database if they don't already exist so that db scripts can be ran
with idempotency.
'''


def get_or_create_tournament(tournament):
    obj, created = Tournament.objects.get_or_create(
        name=tournament.name,
        year=tournament.year
    )

    if created:
        print('Created tournament:', tournament.name, tournament.year)

    return obj


def get_or_create_packet(packet):
    obj, created = Packet.objects.get_or_create(
        tournament=packet.tournament,
        name=packet.name,
        round_number=packet.round_number
    )

    if created:
        print('created packet:', packet.name, packet.round_number)

    return obj


def get_or_create_tossup(tossup):
    obj, created = Tossup.objects.get_or_create(
        packet=tossup.packet,
        text_part_1=tossup.text_part_1,
        text_part_2=tossup.text_part_2,
        text_part_3=tossup.text_part_3,
        answer=tossup.answer,
        number=tossup.number
    )

    if created:
        print('Created tossup:', tossup.packet, tossup.number)

    for keyword in get_tossup_keywords(obj):
        kw, created = Keyword.objects.get_or_create(keyword=keyword)
        if created:
            print('created keyword:', keyword)

        linkage, created = KeywordTossupLinkage.objects.get_or_create(keyword=kw, tossup=obj)
        if created:
            print('linked keyword id', kw.id, 'to tossup id', obj.id)

    return obj
