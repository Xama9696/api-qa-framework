import requests

from utils.logger import log_message


BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_posts():

    log_message("Testing GET /posts")

    response = requests.get(
        f"{BASE_URL}/posts"
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)

    assert len(data) > 0

    log_message("GET /posts passed")


def test_get_single_post():

    log_message("Testing GET /posts/1")

    response = requests.get(
        f"{BASE_URL}/posts/1"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1

    log_message("GET /posts/1 passed")


def test_invalid_post():

    log_message("Testing invalid endpoint")

    response = requests.get(
        f"{BASE_URL}/posts/99999"
    )

    assert response.status_code == 404