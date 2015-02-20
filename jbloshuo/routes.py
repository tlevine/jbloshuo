#!/usr/bin/env python3
import os

from bottle import Bottle, request, response, \
                   abort, redirect, \
                   view, TEMPLATE_PATH, \
                   static_file

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
    return {
        'category': 'consultant',
        'category_pretty': 'a consultant',
        'description_noun': 'project',
        'pay_label': 'What is your budget? (Choose the closest one.)',
        'pay_options': [
            '$4,000',
            '$16,000',
            '$64,000',
            '$256,000 (or more)',
        ],
        'initiative_label': 'Why are you interested in conducting this project? For example, is this part of a larger initiative?',
    }

@app.route('/employee')
@view('form')
def employee():
    return {
        'category': 'employee',
        'category_pretty': 'an employee',
        'description_noun': 'position',
        'pay_label': 'What is the salary? (Choose the closest one.)',
        'pay_options': [
            '$64,000',
            '$128,000',
            '$256,000',
            '$512,000',
        ],
        'initiative_label': 'Why are you interested in conducting this project? For example, is this part of a larger initiative?',
    }

@app.route('/submit')
@view('submit')
def submit():
    return {}

@app.route('/style.css')
def css():
    return static_file('style.css', root = LIB_DIR)
