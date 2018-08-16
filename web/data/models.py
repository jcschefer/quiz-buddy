from django.db import models

from enum import Enum
import json


class PacketType(Enum):
    TOSSUP = 'TOSSUP'
    BONUS = 'BONUS'


class Tournament(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField()


class Packet(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    round_number = models.IntegerField(help_text='Corresponding round from which the packet comes')
    packet_type = models.CharField(max_length=20, help_text='Oneof PacketType values')


class Question(models.Model):
    packet = models.ForeignKey(Packet, on_delete=models.CASCADE)
    text_part_1 = models.CharField(max_length=1000)
    text_part_2 = models.CharField(max_length=1000, default='')
    text_part_3 = models.CharField(max_length=1000, default='')
    answer = models.CharField(max_length=250)
    number = models.IntegerField(
        help_text='Order in which the question comes in the packet', default=0)

    def toJson(self):
        joined_text = ' '.join([self.text_part_1, self.text_part_2, self.text_part_3])
        return json.dumps({'text': joined_text, 'answer': self.answer})
