"""Тестируем модуль Rest worker."""
import pytest
from app_code.rest_worker import api_handler

TEST_URL_WRONG_JSON: str = 'test_url'
TEST_URL: str = 'check_repo'


def test_api_handler_json_wrong():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        api_handler(TEST_URL_WRONG_JSON, ('job.',))
    assert pytest_wrapped_e.type == SystemExit


def test_api_handler():
    assert type(api_handler(TEST_URL, ('ytisf', 'theZoo',))) == dict
