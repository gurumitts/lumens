from flask import Flask
from flask import render_template, Response, request, abort
from babel.dates import format_timedelta
import json
import logging
import os


app = Flask(__name__)

logs_location = '/var/log/lumens'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/logs/')
def logs(log=None):
    logs = []
    if log is None:
        for log in os.listdir(logs_location):
            logs.append(log)
    return render_template('logs.html', logs=logs)


@app.route('/logs/<log>')
def view_log(log=None):
    fo = open('%s/%s' % (logs_location, log), 'r')
    contents = fo.read()
    fo.close()
    return Response(contents, mimetype='text/plain')


@app.route('/toggle', methods=['POST'])
def toggle():
    if request.method == 'POST':
        led = request.form['led']
        logging.getLogger('lumens').debug('toggle switch web %s' % led)
        lumen_control.toggle(led)
    return 'ko'


def start(_lumens):
    global lumen_control
    lumen_control = _lumens

    # app.debug = True
    app.run(host='0.0.0.0', threaded=True)

