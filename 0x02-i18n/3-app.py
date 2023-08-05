#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect, url_for
from flask_babel import Babel
"""
Parametrize your templates
"""


app = Flask(__name__)


babel = Babel(app)


class Config(object):
    """Configs class for Babel"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


@app.route('/')
def index():
    """Displays Hello HBNB!"""
    return render_template('3-index.html')


@babel.localeselector
def get_locale():
    """Retrives locale language"""
    locale = request.args.get('locale')
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(Config.LANGUAGES)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
