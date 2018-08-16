from data.models import Tournament, Packet, Question

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
        tournament_id=packet.tournament_id,
        name=packet.name,
        round_number=packet.round_number,
        packet_type=packet.packet_type
    )

    if created:
        print('created packet:', packet.name, packet.round_number)

    return obj


def get_or_create_question(question):
    obj, created = Question.objects.get_or_create(
        packet_id=question.packet_id,
        text_part_1=question.text_part_1,
        text_part_2=question.text_part_2,
        text_part_3=question.text_part_3,
        answer=question.answer,
        number=question.number
    )

    if created:
        print('Created question:', question.packet_id, question.number)

    return obj
