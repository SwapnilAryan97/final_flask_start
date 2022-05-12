"""This test the homepage"""


def test_request_main_menu_links(client):
    """This tests the home page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'href="/login"' in response.data
    assert b'href="/register"' in response.data


def test_auth_pages(client):
    """This tests the home page"""
    response = client.get("/dashboard")
    assert response.status_code == 302
    response = client.get("/register")
    assert response.status_code == 200
    response = client.get("/login")
    assert response.status_code == 200


def test_user_menu_links(client):
    """This tests the user links , without login"""
    response = client.get("/profile")
    assert response.status_code == 302
    response = client.get("/account")
    assert response.status_code == 302
    response = client.get("/logout")
    assert response.status_code == 302
    response = client.get("/users")
    assert response.status_code == 302


def test_user_menu_links_after_login(client):
    with client:
        """This tests the user menu links , after login"""
        register_response = client.post("/register", data={
            "email": "testuser1@test.com",
            "password": "test123!test",
            "confirm": "test123!test"
        },
                                        follow_redirects=True)
        login_response = client.post("/login", data={
            "email": "testuser1@test.com",
            "password": "test123!test"
        },
                                     follow_redirects=True)

        assert login_response.status_code == 400
        response = client.get("/profile")
        assert response.status_code == 302
        response = client.get("/account")
        assert response.status_code == 302
        response = client.get("/logout")
        assert response.status_code == 302
