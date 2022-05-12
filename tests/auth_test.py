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


