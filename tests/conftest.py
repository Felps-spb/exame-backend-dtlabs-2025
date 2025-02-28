import pytest
import os
from fastapi.testclient import TestClient
from app.main import app
from app.utils.database import Base, engine

# Defina a variável de ambiente ANTES de importar a aplicação
os.environ["TESTING"] = "1"

# Cria as tabelas antes de qualquer teste
@pytest.fixture(scope="session", autouse=True)
def create_test_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="module")
def client():
    with TestClient(app) as client:
        yield client

@pytest.fixture(scope="module")
def test_user(client):
    user_data = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpassword"
    }
    response = client.post("/auth/register", json=user_data)
    return response.json()

@pytest.fixture(scope="module")
def auth_token(client, test_user):
    login_data = {
        "username": "testuser",
        "password": "testpassword"
    }
    response = client.post("/auth/login", data=login_data)
    return response.json()["access_token"]