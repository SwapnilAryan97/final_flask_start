# project/tests/test_config.py
import logging
import os

import app.config


def test_development_config(application):
    application.config.from_object('app.config.DevelopmentConfig')

    assert application.config['DEBUG']
    assert not application.config['TESTING']


