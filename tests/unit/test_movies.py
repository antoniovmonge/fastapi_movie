import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client():
    return TestClient(app)

def test_get_movies(client):
    """
    GIVEN
    WHEN get "movies" endpoint is called with GET method
    THEN response with status 200 and body with movies is returned
    """
    response = client.get("/movies/")
    response_dict = response.json()
    assert response.status_code == 200
    assert type(response_dict) == list
    assert len(response_dict) > 1

def test_get_movie_by_id(client):
    """
    GIVEN a movie id
    WHEN get_movies_by_id endpoint is called with GET method
    and id as path parameter
    THEN response with status 200 and body with movie is returned
    """
    response = client.get("/movies/1/")
    response_dict = response.json()
    assert response.status_code == 200
    assert type(response_dict) == list
    assert len(response_dict) == 1

def test_get_movie_incorrect_id(client):
    """
    GIVEN an movie id not registered in db
    WHEN get_movies_by_id endpoint is called with GET method
    and id as path parameter
    THEN response with status 404 and detail "not found" is returned
    """
    response = client.get("/movies/9999")
    response_dict = response.json()
    assert response.status_code == 404
    assert response_dict['detail'] == "Movie not found"
