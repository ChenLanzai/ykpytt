import pytest
from utils.config_loader import load_yaml

_CONFIG = load_yaml("data/posts.yaml")


@pytest.fixture(scope="session")
def base_url():
    return _CONFIG["base_url"]


@pytest.fixture(scope="session")
def posts_config():
    return _CONFIG
