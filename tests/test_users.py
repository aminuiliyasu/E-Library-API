import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


@pytest.mark.asyncio
def test_create_user():
    response = client.post("/users/", json={
        "id": 1,
        "name": "Jane Smith",
        "email": "janesmith@example.com",
        "is_active": True
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Jane Smith"
@pytest.mark.asyncio
def test_list_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert len(response.json()) > 0  # Ensure at least one user exists
@pytest.mark.asyncio
def test_update_user():
    response = client.put("/users/1", json={
        "id": 1,
        "name": "Jane Updated",
        "email": "jane_updated@example.com",
        "is_active": False
    })
    assert response.status_code == 200
    assert response.json()["email"] == "jane_updated@example.com"
@pytest.mark.asyncio
def test_delete_user():
    response = client.delete("/users/1")
    assert response.status_code == 200
    response = client.get("/users/1")
    assert response.status_code == 404
