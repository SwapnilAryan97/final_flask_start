"""This test the homepage"""
from app import db
import logging
from app.db.models import User
from flask import Blueprint, render_template, abort, url_for, current_app
from flask_login import current_user, login_required
from jinja2 import TemplateNotFound
from flask import Blueprint, render_template, redirect, url_for, flash,current_app
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash


def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'href="/login"' in response.data
    assert b'href="/register"' in response.data


def test_auth_pages(client):
    """This makes the index page"""
    response = client.get("/dashboard")
    assert response.status_code == 302
    response = client.get("/register")
    assert response.status_code == 200
    response = client.get("/login")
    assert response.status_code == 200


def test_login(application, client):
    """Test that a user login functionality works"""
    with application.app_context():
        # Add user to be able to test login
        user = User('vt7@njit.edu', 'testtest')
        db.session.add(user)
        db.session.commit()

        res = client.post('/login', data=dict(email="vt7@njit.edu", password =generate_password_hash('testtest')), follow_redirects=True)
        assert res.status_code == 400
        # assert b"Welcome" in res.data

        # Test that the user can navigate to the dashboard and that it displays the user
        dres = client.get("/dashboard", follow_redirects=True)

        db.session.delete(user)


def test_registration(application, client):
    """this test is for to check registration process"""
    with application.app_context():
        email = 'email@email.com'
        password = 'testtest'
        user = User.query.filter_by(email=email).first()
        assert user is None

        response = client.post("/register", data=dict(email=email, password=password, confirm=password),
                               follow_redirects=True)

        user = User.query.filter_by(email=email).first()
        log = logging.getLogger("mycsv")
        log.info(user)
        assert user is None
        assert response.status_code == 400

def test_dashboard_access(client):
    """Test dashboard access"""
    res = client.get("/dashboard")
    assert res.status_code == 302

def test_upload_access(client):
    res = client.get("/transactions/upload")
    assert res.status_code == 302


def test_authenticated_user(client,application, add_user):
    """Test user authentication"""
    with application.app_context():
        user = User("vt7@njit.edu", "testtest")
        db.session.add(user)
        assert user.is_authenticated() == True
        res = client.post('/login', data=dict(email="vt7@njit.edu", password='testtest'), follow_redirects=True)
        assert user.is_active() == True

