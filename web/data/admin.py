from django.contrib import admin

from .models import Tournament, Packet, Tossup

# Register your models here.
admin.site.register(Tournament)
admin.site.register(Packet)
admin.site.register(Tossup)
