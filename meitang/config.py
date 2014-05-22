# -*- coding: utf-8 -*-

import os

from .utils import make_dir

PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


class BaseConfig(object):

    PROJECT = "meitang"

    # Get app root path, also can use flask.root_path.
    # ../../config.py
    #PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    DEBUG = False
    TESTING = False

    #ADMINS = ['youremail@yourdomain.com']

    # http://flask.pocoo.org/docs/quickstart/#sessions
    SECRET_KEY = 'secret key'

    LOG_FOLDER = os.path.join(PROJECT_ROOT, 'logs')
    make_dir(LOG_FOLDER)


class DefaultConfig(BaseConfig):

    DEBUG = True

    SQLALCHEMY_ECHO = True
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///' + PROJECT_ROOT + '/production.sqlite'
    # MYSQL for production.
    #SQLALCHEMY_DATABASE_URI = 'mysql://username:password@server/db?charset=utf8'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/virgo?charset=utf8'

    #SQLALCHEMY_DATABASE_URI = 'mysql://root:JGtm@2014@115.29.140.202/virgo?charset=utf8'


    # Flask-babel: http://pythonhosted.org/Flask-Babel/
    #ACCEPT_LANGUAGES = ['zh']
    #BABEL_DEFAULT_LOCALE = 'en'


class TestConfig(BaseConfig):
    TESTING = True
    WTF_CSRF_ENABLED = False

    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + PROJECT_ROOT + '/test.sqlite'
