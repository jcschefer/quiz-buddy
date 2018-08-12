from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse
from subprocess import Popen, PIPE
import tempfile
import datetime
from data.utils import fetch_random_question
import os.path

DEFAULT_QUESTION_NUMBER = 20

# Create your views here.


def random_guide(request):
    params = {
        'title': 'Random Study Guide',
        'date': datetime.date.today().strftime('%x'),
        'questions': [fetch_random_question() for i in range(DEFAULT_QUESTION_NUMBER)]
    }

    template = get_template('guide.tex')
    rendered_template = template.render(params).encode('utf-8')

    with tempfile.TemporaryDirectory() as tempdir:
        process = Popen(['pdflatex', '-output-directory', tempdir], stdin=PIPE, stdout=PIPE)
        process.communicate(rendered_template)

        with open(os.path.join(tempdir, 'texput.pdf'), 'rb') as f:
            pdf = f.read()

    r = HttpResponse(content_type='application/pdf')
    r.write(pdf)
    return r
