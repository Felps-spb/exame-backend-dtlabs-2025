def test_register_user(client):
    user_data = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpassword"
    }
    response = client.post("/auth/register", json=user_data)
    assert response.status_code == 200
    assert "id" in response.json()

def test_login_user(client, test_user):
    login_data = {
        "username": "testuser",
        "password": "testpassword"
    }
    response = client.post("/auth/login", data=login_data)
    assert response.status_code == 200
    assert "access_token" in response.json()