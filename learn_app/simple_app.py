from flask import Flask, request
from markupsafe import escape

app = Flask(__name__)


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
    return 'Given http code is %s' % escape(http_code)


if __name__ == "__main__":
    app.run()
