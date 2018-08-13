from django.contrib import admin

from .models import Tournament, Round, Question

# Register your models here.
admin.site.register(Tournament)
admin.site.register(Round)
admin.site.register(Question)
