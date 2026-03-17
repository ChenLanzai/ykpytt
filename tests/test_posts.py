import pytest
from utils.api_helper import (
    send_request,
    assert_status_code,
    assert_json_has_keys,
    assert_json_field,
)
from utils.config_loader import load_yaml

CONFIG = load_yaml("data/posts.yaml")


def test_get_posts_list(base_url):
    """获取帖子列表：返回 200，且为非空列表"""
    path = CONFIG["posts_list"]["path"]
    expected_status = CONFIG["posts_list"]["expected_status"]
    url = f"{base_url}{path}"

    resp = send_request("GET", url)

    assert_status_code(resp, expected_status)
    data = resp.json()
    assert isinstance(data, list) and len(data) > 0
    assert "id" in data[0] and "title" in data[0]


@pytest.mark.parametrize("post_id", CONFIG["get_single_post"]["post_ids"])
def test_get_single_post(base_url, post_id):
    """获取单个帖子详情"""
    path_tpl = CONFIG["get_single_post"]["path_template"]
    path = path_tpl.format(post_id=post_id)
    expected_status = CONFIG["get_single_post"]["expected_status"]
    url = f"{base_url}{path}"

    resp = send_request("GET", url)

    assert_status_code(resp, expected_status)
    assert_json_field(resp, "id", post_id)
    assert_json_has_keys(resp, ["title", "body"])


@pytest.mark.parametrize("case", CONFIG["create_post"]["cases"])
def test_create_post(base_url, case):
    """创建帖子"""
    path = CONFIG["create_post"]["path"]
    expected_status = CONFIG["create_post"]["expected_status"]
    url = f"{base_url}{path}"
    payload = {"title": case["title"], "body": case["body"], "userId": case["userId"]}

    resp = send_request("POST", url, json=payload)

    assert_status_code(resp, expected_status)
    assert_json_field(resp, "title", case["title"])
    assert_json_field(resp, "body", case["body"])
    assert_json_field(resp, "userId", case["userId"])
    assert_json_has_keys(resp, "id")


@pytest.mark.parametrize("case", CONFIG["update_post"]["cases"])
def test_update_post(base_url, case):
    """更新帖子"""
    path_tpl = CONFIG["update_post"]["path_template"]
    path = path_tpl.format(post_id=case["post_id"])
    url = f"{base_url}{path}"
    payload = {
        "id": case["post_id"],
        "title": case["title"],
        "body": case["body"],
        "userId": case["userId"],
    }

    resp = send_request("PUT", url, json=payload)

    assert_status_code(resp, 200)
    assert_json_field(resp, "id", case["post_id"])
    assert_json_field(resp, "title", case["title"])
