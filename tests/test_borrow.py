import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.mark.asyncio
async def test_borrow_book():
    client.post("/users/", json={
        "id": 1,
        "name": "John Doe",
        "email": "johndoe@example.com",
        "is_active": True
    })
    client.post("/books/", json={
        "id": 2,
        "title": "1984",
        "author": "George Orwell",
        "is_available": True
    })
    response = client.post("/borrow/", json={
        "id": 1,
        "user_id": 1,
        "book_id": 2,
        "borrow_date": "2024-12-01",
        "return_date": None
    })
    assert response.status_code == 200
    assert response.json()["user_id"] == 1
    assert response.json()["book_id"] == 2
