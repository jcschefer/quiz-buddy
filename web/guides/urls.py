from django.urls import path

from . import views

urlpatterns = [
    path('random', views.random_guide, name='random'),
    path('packet/<int:packet_id>', views.packet_guide, name='packet_guide'),
]
