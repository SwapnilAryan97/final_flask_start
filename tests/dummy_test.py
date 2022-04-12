import unittest


def test_request_index(client):
    """This makes the first page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello, World!" in response.data
