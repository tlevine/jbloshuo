#!/usr/bin/env python3
import os

from bottle import Bottle, request, response, \
                   abort, redirect, \
                   view, TEMPLATE_PATH, \
                   static_file

from .queries import hierarchy, subhierarchy

LIB_DIR = os.path.split(__file__)[0]
TEMPLATE_PATH.append(os.path.join(LIB_DIR, 'views'))
app = Bottle()

@app.route('/')
@view('home')
def home():
    return {}

@app.route('/submit')
@view('submit')
def submit():
    return {}

@app.route('/style.css')
def css():
    return static_file('style.css', root = LIB_DIR)

"""

@app.get('/!/<querystr:path>/')
@view('thread')
def search(querystr):
    db = Database()
    query = Query(db, querystr)
    if query.count_messages() == 1:
        message = next(iter(query.search_messages()))
        title = message.get_header('subject')
        try:
            parts = [(i + 1, part.get_filename('No description')) \
                     for i, part in enumerate(message.get_message_parts())]
            body = message.get_part(1)
        except UnicodeDecodeError:
            parts = []
            body = 'There was an encoding problem with this message.'
    else:
        title = 'Results for "%s"' % querystr
        parts = []
        body = None

    return {
        'title': title,
        'parts': parts,
        'body': body,
        'threads': list(hierarchy(query)),
    }

@app.get('/!/<querystr:path>/<n:int>')
def attachment(querystr, n):
    db = Database()
    query = Query(db, querystr)
    if query.count_messages() != 1:
        redirect('/!/%s/' % querystr)
    else:
        message = next(iter(query.search_messages()))
        parts = message.get_message_parts()
        i = n - 1
        if i >= len(parts):
            redirect('/!/%s/' % querystr)
        else:
            part = parts[i]
            content_type = part.get_content_type()
            response.content_type = content_type
         #  response.charset = part.get_content_charset()

            fn = part.get_filename()
            if fn != None:
                response.headers['content-disposition'] = 'filename="%s";' % unidecode(fn).replace('"', '')

            payload = message.get_part(n)
            if 'html' in content_type.lower():
                return clean_html(payload)
            else:
                return payload

@app.route('/!')
@app.route('/!/')
def exclaim():
    redirect('/')

@app.route('/!/<querystr:path>')
def slash(querystr):
    redirect('/!/' + querystr.rstrip('/') + '/')
"""
