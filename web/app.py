import os

import flask as f
from flask import Flask
from flask.ext.assets import Environment, Bundle
from raven.contrib.flask import Sentry
import config.conf as conf

app = Flask(__name__)

app.config.from_object("web.config.conf")
sentry = Sentry(dsn=conf.SENTRY_DSN)

if not app.config["DEBUG_MODE"]:
    sentry.init_app(app)

assets = Environment(app)
assets.versions = 'hash:32'
main_js = Bundle("main_bundle.js", 
                 output='dist/main_bundle.%(version)s.js')
assets.register('js_all', main_js)

all_css = Bundle("style.css", 
                 output='dist/main.%(version)s.css')
assets.register('css_all', all_css)



@app.before_request
def something_before_request():
    pass

import controllers
import web.admin


# app.jinja_env.filters['markdown']  = markdown_text
