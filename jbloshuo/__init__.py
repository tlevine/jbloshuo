from .routes import app

def run():
    app.run(server = 'cherrypy', reloader = True, port = 8083, host = '127.0.0.1')
