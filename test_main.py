from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_search_valid_term():
    response = client.get("/search?term=liver")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) <= 10

def test_search_short_term():
    response = client.get("/search?term=li")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_search_empty_term():
    response = client.get("/search?term=")
    assert response.status_code == 200 or response.status_code == 422

def test_term_details_valid():
    response = client.get("/term-details?term=Liver")
    assert response.status_code in [200, 404]

def test_term_details_invalid():
    response = client.get("/term-details?term=RandomNonExistingTerm123")
    assert response.status_code in [200, 404]
