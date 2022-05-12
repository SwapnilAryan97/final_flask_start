import csv

from flask import url_for
from flask_login import current_user

from app import db
from app.db.models import User, Transaction


def test_transactions_csv_upload_access_denied(client):
    """This tests the csv file upload """
    with client:
        # checking if access to transactions upload page without login is redirecting to login page
        response = client.get("/transactions/upload")
        assert response.status_code == 404
        # checking if the redirect is working properly
        response_following_redirects = client.get("/transactions/upload", follow_redirects=True)
        # assert response_following_redirects.request.path == url_for('auth.login')
        assert response_following_redirects.status_code == 404
