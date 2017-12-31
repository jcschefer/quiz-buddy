from django.db import models

import json

# Create your models here.
class Tournament(models.Model):
    name = models.CharField(max_length = 200)
    year = models.IntegerField()

class Packet(models.Model):
    tournament_id = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    name = models.CharField(max_length = 200)
    index = models.IntegerField(help_text='Order that the packet comes in the tournament')

class Question(models.Model):
    packet_id = models.ForeignKey(Packet, on_delete=models.CASCADE)
    text = models.CharField(max_length=1500)
    answer = models.CharField(max_length=250)

    def toJson(self):
        return json.dumps({'text': self.text, 'answer': self.answer})
