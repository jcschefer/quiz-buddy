import random
from .models import Question

q = [
    Question(
        text_part_1='The answer is duck. blah blah blah blah blah blah blah blah blah blah blah blah',
        answer='duck',
    ),
    Question(
        text_part_1='The answer is cat. blah blah blah blah blah blah blah blah blah blah blah blah',
        answer='cat',
    ),
    Question(
        text_part_1='The answer is dog. blah blah blah blah blah blah blah blah blah blah blah blah',
        answer='dog',
    ),
    Question(
        text_part_1='The answer is zebra. blah blah blah blah blah blah blah blah blah blah blah blah',
        answer='zebra',
    ),
    Question(
        text_part_1='The answer is hamster. blah blah blah blah blah blah blah blah blah blah blah blah',
        answer='hamster',
    )
]


def fetch_random_question():
    return random.choice(q)
