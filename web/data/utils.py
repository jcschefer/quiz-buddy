import random
from .models import Question

q = [
	Question(
		text = 'The answer is duck. blah blah blah blah blah blah blah blah blah blah blah blah',
		answer = 'duck',
	),
	Question(
		text = 'The answer is cat. blah blah blah blah blah blah blah blah blah blah blah blah',
		answer = 'cat',
	),
	Question(
		text = 'The answer is dog. blah blah blah blah blah blah blah blah blah blah blah blah',
		answer = 'dog',
	),
	Question(
		text = 'The answer is zebra. blah blah blah blah blah blah blah blah blah blah blah blah',
		answer = 'zebra',
	),
	Question(
		text = 'The answer is hamster. blah blah blah blah blah blah blah blah blah blah blah blah',
		answer = 'hamster',
	)
]

def fetch_random_question():
	return random.choice(q)
