from random import choice
from .models import Tossup

def fetch_random_tossup():
    return choice(list(Tossup.objects.all()))
