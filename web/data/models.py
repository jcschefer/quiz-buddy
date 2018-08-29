from django.db import models

from enum import Enum
import json


class Tournament(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField()


class Packet(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    round_number = models.IntegerField(help_text='Corresponding round from which the packet comes')


class Tossup(models.Model):
    packet = models.ForeignKey(Packet, on_delete=models.CASCADE)
    text_part_1 = models.CharField(max_length=1000)
    text_part_2 = models.CharField(max_length=1000, default='')
    text_part_3 = models.CharField(max_length=1000, default='')
    answer = models.CharField(max_length=250)
    number = models.IntegerField(
        help_text='Order in which the question comes in the packet', default=0)

    def toJson(self):
        return json.dumps({'text': self.get_full_text(), 'answer': self.answer})

    def get_full_text(self):
        return ' '.join([self.text_part_1, self.text_part_2, self.text_part_3])


class Keyword(models.Model):
    keyword = models.CharField(max_length=50)


class KeywordTossupLinkage(models.Model):
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    tossup = models.ForeignKey(Tossup, on_delete=models.CASCADE)
