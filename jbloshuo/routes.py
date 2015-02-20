#!/usr/bin/env python3
import os
from urllib.parse import urlencode

from bottle import Bottle, request, response, \
                   abort, redirect, \
                   view, TEMPLATE_PATH, \
                   static_file, template

from .email import send_email

LIB_DIR = os.path.split(__file__)[0]
TEMPLATE_PATH.append(os.path.join(LIB_DIR, 'views'))
app = Bottle()

@app.route('/')
@view('home')
def home():
    return {}

@app.route('/consultant')
@view('form')
def consultant():
    p = request.params.get
    return {
        'name_value': p('name', ''),
        'email_value': p('email', ''),
        'company_value': p('company', ''),
        'description_value': p('description', ''),
        'initiative_value': p('initiative', ''),
        'pay_value': p('pay'),
        'time_value': p('time'),

        'error_message': p('error-message'),
        'category': 'consultant',
        'category_pretty': 'a consultant',
        'description_noun': 'project',
        'pay_label': 'What is your <strong>budget</strong>?',
        'pay_options': [
            '$4,000',
            '$16,000',
            '$64,000',
            '$256,000 (or more)',
        ],
        'initiative_label': 'Why are you interested in conducting this project?',
        'initiative_placeholder': 'For example, is this part of a larger initiative?',
    }

@app.route('/employee')
@view('form')
def employee():
    p = request.params.get
    return {
        'name_value': p('name', ''),
        'email_value': p('email', ''),
        'company_value': p('company', ''),
        'description_value': p('description', ''),
        'initiative_value': p('initiative', ''),
        'pay_value': p('pay'),
        'time_value': p('time'),

        'error_message': p('error-message'),
        'category': 'employee',
        'category_pretty': 'an employee',
        'description_noun': 'position',
        'pay_label': 'What is the <strong>salary</strong>?',
        'pay_options': [
            '$64,000',
            '$128,000',
            '$256,000',
            '$512,000',
        ],
        'initiative_label': 'Why are you interested in hiring for this position at this time?',
        'initiative_placeholder': 'For example, is it for a new project, because of recent investment, &c.?',
    }

FIELDS = ['category',
          'name', 'email', 'company',
          'pay', 'time',
          'description', 'initiative']
TIMES = {'Full-time', 'Part-time'}
KINDS = {'employee', 'consultant'}

@app.post('/submit')
def submit():
    data = dict(request.forms)
    if 'submit' in data:
        del(data['submit'])

    for field in FIELDS:
        if field not in data or data[field] == '':
            data[field] = None

    if data['time'] not in TIMES:
        data['time'] = None
    if data['category'] not in KINDS:
        data['category'] = None

    if data['category'] == None:
        abort(400, 'Something went rather wrong. Try sending me an email instead.')
    elif None in data.values():
        data['error-message'] = 'Fill in all the fields.'
        for k, v in data.items():
            if v == None:
                data[k] = ''
        redirect('/%s?%s' % (data['category'], urlencode(data)))
    else:
        send_email(data)
        return template('submit')

@app.route('/style.css')
def css():
    return static_file('style.css', root = LIB_DIR)
