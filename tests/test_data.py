def test_post_sensor_data(client, auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    sensor_data = {
        "server_ulid": "01JN49V9CGGY3XY8STNP1DVHBG",
        "timestamp": "2024-02-19T12:34:56Z",
        "temperature": 25.5,
        "humidity": 60.2,
        "voltage": 220.0,
        "current": 1.5
    }
    response = client.post("/data", json=sensor_data, headers=headers)
    assert response.status_code == 200
    assert "id" in response.json()

def test_get_sensor_data(client, auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = client.get("/data", headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)