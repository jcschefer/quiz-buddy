from django.urls import path

from . import views

urlpatterns = [
    path('random_tossup', views.random_tossup, name='random_tossup'),
]
