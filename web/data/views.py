from django.shortcuts import render
from django.http import HttpResponse

from .models import Question

# Create your views here.
def random_question(request):
    q = Question(
        text = 'The answer is duck. blah blah blah blah blah blah blah blah blah blah blah blah', 
        answer = 'duck'
    )
    return HttpResponse(q.toJson())
