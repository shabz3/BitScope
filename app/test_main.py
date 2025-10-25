from fastapi.testclient import TestClient
import pytest
from .main import app
import requests

client = TestClient(app)

def mock_get():
    raise Exception("API down")

def test_homepage_returns_200():
    response = client.get("/")
    assert response.status_code == 200
    assert "Conversion" in response.text

def test_homepage_returns_500(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(requests, "get", mock_get)
    response = client.get("/")
    assert response.status_code == 500
    assert response.json() == {"detail": "Failed to fetch"}

def test_404_page():
    response = client.get("/helloworld")
    assert response.status_code == 200
    assert "404" in response.text

def test_health_returns_200():
    response = client.get("/health")
    assert response.status_code == 200
    assert "ok" in response.text