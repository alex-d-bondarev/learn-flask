import datetime
import time

from flask import Flask, request, g
from markupsafe import escape
from logging.config import fileConfig

from rfc3339 import rfc3339

fileConfig('logging.cfg')

app = Flask(__name__)


@app.before_request
def start_timer():
    g.start = datetime.datetime.now()


@app.after_request
def log_request(response):
    """Log request. Credit to
    https://dev.to/rhymes/logging-flask-requests-with-colors-and-structure--7g1

    :param response:
    :return:
    """
    if request.path == '/favicon.ico':
        return response

    now = datetime.datetime.now()
    duration = now - g.start
    timestamp = rfc3339(now, utc=True)

    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    host = request.host.split(':', 1)[0]
    args = dict(request.args)

    log_params = [
        ('method', request.method),
        ('path', request.path),
        ('status', response.status_code),
        ('duration', duration),
        ('time', timestamp),
        ('ip', ip),
        ('host', host),
        ('params', args)
    ]

    line_items = []
    for name, value in log_params:
        item = f'{name}={value}'
        line_items.append(item)
    line = " ".join(line_items)

    app.logger.info(line)

    return response


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello')
def hello():
    return 'Hello, World!'


@app.route('/about')
def about():
    return 'The about page'


@app.route('/print/<text>')
def print_text(text):
    return 'Given text %s' % escape(text)


@app.route('/translate')
def translate_http_code():
    http_code = request.args.get('http_code')
    app.logger.info(f'Processing http code {http_code}')
    return 'Given http code is %s' % escape(http_code)


if __name__ == "__main__":
    app.run()
