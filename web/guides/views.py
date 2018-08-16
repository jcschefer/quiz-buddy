from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse
from subprocess import Popen, PIPE
import tempfile
import datetime
from data.utils import fetch_random_question
from data.models import Packet, Question
import os.path

DEFAULT_QUESTION_NUMBER = 20

# Create your views here.


def random_guide(request):
    # must manually compile the question text because templates don't support complex things
    random_questions = [fetch_random_question() for i in range(DEFAULT_QUESTION_NUMBER)]

    params = {
        'title': 'Random Study Guide',
        'date': datetime.date.today().strftime('%x'),
        'questions': questions_to_template_arg(random_questions)
    }

    return render_guide(params)


def packet_guide(request, packet_id):
    packet = Packet.objects.get(id=packet_id)
    tournament = packet.tournament
    selected_questions = Question.objects.filter(packet=packet).order_by('number')
    params = {
        'title': '{} {}: {}'.format(tournament.name, tournament.year, packet.name),
        'date': datetime.date.today().strftime('%x'),
        'questions': questions_to_template_arg(selected_questions)
    }

    return render_guide(params)


def questions_to_template_arg(questions):
    return [{
        'text': ' '.join(['\\textbf{', q.text_part_1, '(*)}', q.text_part_2, q.text_part_3]),
        'answer': q.answer
    } for q in questions]


def render_guide(template_params):
    template = get_template('guide.tex')
    rendered_template = template.render(template_params).encode('utf-8')

    with tempfile.TemporaryDirectory() as tempdir:
        process = Popen(['pdflatex', '-output-directory', tempdir], stdin=PIPE, stdout=PIPE)
        process.communicate(rendered_template)

        try:
            with open(os.path.join(tempdir, 'texput.pdf'), 'rb') as f:
                r = HttpResponse(content_type='application/pdf')
                r.write(f.read())
                return r
        except FileNotFoundError:
            with open(os.path.join(tempdir, 'texput.log'), 'r') as f:
                print(f.read())
            raise Exception('Error compiling template, check logs...')
