def test_get_health_all(client, auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = client.get("/health/all", headers=headers)
    assert response.status_code == 200
    assert "servers" in response.json()

def test_get_health_single_server(client, auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}
    server_ulid = "01JN49V9CGGY3XY8STNP1DVHBG"
    response = client.get(f"/health/{server_ulid}", headers=headers)
    assert response.status_code == 200
    assert response.json()["status"] in ["online", "offline"]