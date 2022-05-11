import logging

from app import db
from app.db.models import User, Song
from faker import Faker


def test_adding_user(application):
    log = logging.getLogger("myApp")
    with application.app_context():
        assert db.session.query(User).count() == 0
        assert db.session.query(Song).count() == 0
        # showing how to add a record
        # create a record
        user = User('keith@webizly.com', 'testtest')
        # add it to get ready to be committed
        db.session.add(user)
        # call the commit
        # db.session.commit()
        # assert that we now have a new user
        # assert db.session.query(User).count() == 1
        # finding one user record by email
        user = User.query.filter_by(email='keith@webizly.com').first()
        log.info(user)
        # asserting that the user retrieved is correct
        assert user.email == 'keith@webizly.com'
        # this is how you get a related record ready for insert
        user.songs = [Song("test", "smap"), Song("test2", "te")]
        # commit is what saves the songs
        db.session.commit()
        assert db.session.query(Song).count() == 2
        song1 = Song.query.filter_by(title='test').first()
        assert song1.title == "test"
        # changing the title of the song
        song1.title = "SuperSongTitle"
        # saving the new title of the song
        db.session.commit()
        song2 = Song.query.filter_by(title='SuperSongTitle').first()
        assert song2.title == "SuperSongTitle"
        # checking cascade delete
        db.session.delete(user)
        assert db.session.query(User).count() == 0
        assert db.session.query(Song).count() == 0


def test_login(client):
    """This tests for successful login"""
    with client:
        register_response = client.post("/register", data={
            "email": "test@test.com",
            "password": "testtest",
            "confirm": "testtest"
        },
                                        follow_redirects=True)

        assert register_response.status_code == 400
        assert register_response.request.path == url_for('auth.register')

        login_response = client.post("/login", data={
            "email": "test@test.com",
            "password": "WRONG-PASSWORD"
        },
                                     follow_redirects=True)
        # After successful login ,redirected to dashboard
        assert login_response.request.path == url_for('auth.login')
        assert login_response.status_code == 400
