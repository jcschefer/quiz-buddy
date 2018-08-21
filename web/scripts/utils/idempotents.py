from data.models import Tournament, Packet, Tossup

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
        print('Created get_or_create_tossup:', tossup.packet_id, tossup.number)

    return obj
