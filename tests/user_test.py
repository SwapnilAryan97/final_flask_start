import logging

from app import db
from app.db.models import User, Transaction
from faker import Faker
from sqlalchemy.sql import functions


def test_adding_user(application):
    log = logging.getLogger("myApp")
    with application.app_context():
        assert db.session.query(User).count() == 0
        assert db.session.query(Transaction).count() == 0
        user = User('tnvrra393@gmail.com', 'spiderCLAW')
        db.session.add(user)
        db.session.commit()
        assert db.session.query(User).count() == 1
