#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# airtest web gui
#
import os

import click
import flask
import webbrowser


app = flask.Flask(__name__)

app.config['DEBUG'] = True

from routers import home, api
from routers import utils

app.register_blueprint(home.bp, url_prefix='')
app.register_blueprint(api.bp, url_prefix='/api')

def serve(*args, **kwargs):
    print 'Clean tempfiles ...'
    for file in os.listdir(utils.TMPDIR):
        filepath = os.path.join(utils.TMPDIR, file)
        if os.path.isfile(filepath):
            os.unlink(filepath)
    print 'Start server'
    app.run(*args, **kwargs)

@click.command(help='Run GUI in browser')
@click.option('--workdir', default=os.getcwd(), type=click.Path(file_okay=False), help='working directory')
@click.option('--reload', default=False, is_flag=True, help='For developer to auto reload code when code change')
def main(workdir, reload):
    os.environ['WORKDIR'] = workdir
    webbrowser.open('http://localhost:5000')
    serve(use_reloader=reload, debug=True)

if __name__ == '__main__':
    main()