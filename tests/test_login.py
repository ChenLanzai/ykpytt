import requests
import pytest


def test_get_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    resp = requests.get(url)
    assert resp.status_code == 200
    json_data = resp.json()
    assert isinstance(json_data, list)
    assert len(json_data) > 0


