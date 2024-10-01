import pytest
from fastapi.testclient import TestClient
from app.api.app import app

client = TestClient(app)

def test_root():
    """Test the root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Cognitive CORE API"}

def test_process():
    """Test the process endpoint."""
    response = client.post("/process/", json={"data": "Hello"})
    assert response.status_code == 200
    assert response.json() == {"result": "HELLO"}
