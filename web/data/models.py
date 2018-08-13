from django.db import models

import json


class Tournament(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField()


class Round(models.Model):
    tournament_id = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    index = models.IntegerField(help_text='Order that the packet comes in the tournament')


class Question(models.Model):
    round_id = models.ForeignKey(Round, on_delete=models.CASCADE)
    text_part_1 = models.CharField(max_length=1000)
    text_part_2 = models.CharField(max_length=1000, default='')
    text_part_3 = models.CharField(max_length=1000, default='')
    answer = models.CharField(max_length=250)

    def toJson(self):
        joined_text = ' '.join([self.text_part_1, self.text_part_2, self.text_part_3])
        return json.dumps({'text': joined_text, 'answer': self.answer})
