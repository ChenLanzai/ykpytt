# utils/api_helper.py
import requests


def send_request(method, url, json=None, **kwargs):
    """发请求，返回 response。"""
    return requests.request(method.upper(), url, json=json, **kwargs)


def assert_status_code(response, expected):
    """断言 HTTP 状态码。"""
    assert response.status_code == expected, (
        f"expected status {expected}, got {response.status_code}"
    )


def assert_json_has_keys(response, keys):
    """断言响应 JSON 里包含这些 key。keys 可以是 list 或单个 str。"""
    data = response.json()
    if isinstance(keys, str):
        keys = [keys]
    for key in keys:
        assert key in data, f"missing key: {key}"


def assert_json_field(response, key, expected):
    """断言响应 JSON 里 key 的值等于 expected。"""
    data = response.json()
    actual = data.get(key)
    assert actual == expected, f"{key}: expected {expected!r}, got {actual!r}"
