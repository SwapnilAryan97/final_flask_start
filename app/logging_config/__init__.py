import logging
import os
from logging.config import dictConfig

import flask
from flask import request, current_app

# from app.logging_config.log_formatters import RequestFormatter
from app import config
log_con = flask.Blueprint('log_con', __name__)


@log_con.before_app_request
def before_request_logging():
    log = logging.getLogger("myApp")
    log.info("REQUEST")


@log_con.after_app_request
def after_request_logging(response):
    if request.path == '/favicon.ico':
        return response
    elif request.path.startswith('/static'):
        return response
    elif request.path.startswith('/bootstrap'):
        return response

    log = logging.getLogger("myApp")
    log.info("RESPONSE")
    return response


@log_con.before_app_first_request
def setup_logs():
    # set the name of the apps log folder to logs
    logdir = config.Config.LOG_DIR
    # make a directory if it doesn't exist
    if not os.path.exists(logdir):
        os.mkdir(logdir)
    logging.config.dictConfig(LOGGING_CONFIG)


LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
        'csv': {
            'format': '%(asctime)s : %(message)s'
        },
        'req': {
            'format': '%(asctime)s : %(message)s'
        },

    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',  # Default is stderr
        },
        'file.handler': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': os.path.join(config.Config.LOG_DIR, 'handler.log'),
            'maxBytes': 10000000,
            'backupCount': 5,
        },
        'file.handler.myapp': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'req',
            'filename': os.path.join(config.Config.LOG_DIR, 'myapp.log'),
            'maxBytes': 10000000,
            'backupCount': 5,
        },
        'file.handler.csv': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'csv',
            'filename': os.path.join(config.Config.LOG_DIR, 'csv.log'),
            'maxBytes': 10000000,
            'backupCount': 5,
        },
    },
    'loggers': {
        '': {  # root logger
            'handlers': ['default', 'file.handler'],
            'level': 'DEBUG',
            'propagate': True
        },
        '__main__': {  # if __name__ == '__main__'
            'handlers': ['default', 'file.handler'],
            'level': 'DEBUG',
            'propagate': True
        },
        'myApp': {  # if __name__ == '__main__'
            'handlers': ['file.handler.myapp'],
            'level': 'INFO',
            'propagate': False
        },
        'mycsv': {  # if __name__ == '__main__'
            'handlers': ['file.handler.csv'],
            'level': 'INFO',
            'propagate': False
        },

    }
}