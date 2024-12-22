import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.mark.asyncio
async def test_create_book():
    response = client.post("/books/", json={
        "id": 1,
        "title": "1984",
        "author": "George Orwell",
        "is_available": True
    })
    assert response.status_code == 200
    assert response.json()["title"] == "1984"

@pytest.mark.asyncio
async def test_list_books():
    response = client.get("/books/")
    assert response.status_code == 200
    assert len(response.json()) > 0
