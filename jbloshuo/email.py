from smtplib import SMTP_SSL as SMTP
from email.mime.text import MIMEText
from textwrap import fill

config = {
    'to': '_@thomaslevine.com',
    'smtp': ,
    'address': ,
    'password': ,
}



TEMPLATE = '''
Hi Thomas,

%(name)s seeks a %(category)s for %(company)s.%(employee_time)s

Description
------------------------
%(description)s

Rationale
------------------------
%(rationale)s
'''

def template(data):
    if data['category'] == 'employee':
        data['employee_time'] = 'This is a %s position.' % data['time'].lower()
    else:
        data['employee_time'] = ''
    before_wrapping = TEMPLATE % data
    return '\n\n'.join(map(fill, re.split(r'\n{2,}', before_wrapping)))

def send_confirmation(data):
    msg = MIMEText(TEMPLATE % data, 'plain')
    msg['Subject'] = 'Job inquiry from %s' 
    msg['To'] = config['to']
    msg['Reply-To'] = data['email']
    conn = SMTP(config['smtp'])
    conn.login(config['address'], config['password'])
    conn.sendmail(config['to'], config['to'], msg.as_string())
    conn.close()
