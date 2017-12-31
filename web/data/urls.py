from django.urls import path

from . import views

urlpatterns = [
    path('random_question', views.random_question, name='random_question'),
]
