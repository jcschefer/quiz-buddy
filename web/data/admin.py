from django.contrib import admin

from .models import Tournament, Packet, Question

# Register your models here.
admin.site.register(Tournament)
admin.site.register(Packet)
admin.site.register(Question)
