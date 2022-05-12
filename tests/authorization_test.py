"""This tests login , registration and dashboard authentication"""

from flask import url_for


def test_register(client):
    with client:
        """This tests the user menu links AFTER login"""
        register_response = client.post("/register", data={
            "email": "test@test.com",
            "password": "testtest",
            "confirm": "testtest"
        },
                                        follow_redirects=True)
        login_response = client.post("/login", data={
            "email": "test@test.com",
            "password": "testtest"
        },
                                     follow_redirects=True)

        assert login_response.status_code == 400
        response = client.get("/profile")
        assert response.status_code == 302
        response = client.get("/account")
        assert response.status_code == 302
        response = client.get("/logout")
        assert response.status_code == 302


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


def test_dashboard_access(client):
    """This tests for successful access to dashboard after login"""
    with client:
        register_response = client.post("/register", data={
            "email": "test@test.com",
            "password": "testtest",
            "confirm": "testtest"
        },
                                        follow_redirects=True)

        login_response = client.post("/login", data={
            "email": "test@test.com",
            "password": "testtest"
        }, follow_redirects=True)
        assert login_response.request.path == url_for('auth.login')
        assert login_response.status_code == 400


def test_dashboard_access_denied(client):
    """This tests for unsuccessful access to dashboard after login"""
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
        assert login_response.request.path == url_for('auth.login')
        assert login_response.status_code == 400
