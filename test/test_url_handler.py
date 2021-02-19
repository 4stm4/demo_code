"""Тесты модуля URL handler."""
import pytest
from app_code.url_handler import url_check, url_parser

TEST_URL: str = 'https://github.com/ytisf/theZoo'
GITHUB_URL_FAKE: str = 'https://gitbuh.com/'
TEST_OWNER: str = 'ytisf'
TEST_FAKE_OWNER: str = 'ded_moroz'
TEST_REPO: str = 'theZoo'
TEST_FAKE_REPO: str = 'THEzOO'


def test_url_check():
    """Тест функции проверки существования репозитория."""
    assert url_check(TEST_OWNER, TEST_REPO)


def test_url_check_fake_repo():
    """Тест функции проверки существования репозитория.

    Note:
        Несуществующий репозиторий.
    """
    assert not url_check(TEST_OWNER, TEST_FAKE_REPO)


def test_url_check_fake_owner():
    """Тест функции проверки существования репозитория.

    Note:
        Несуществующий пользователь.
    """""
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        url_check(TEST_FAKE_OWNER, TEST_REPO)
    assert pytest_wrapped_e.type == SystemExit


def test_url_parser():
    """Тест функции распарсивания URL."""
    assert url_parser(TEST_URL) == (TEST_OWNER, TEST_REPO)


def test_url_parser_fake_github():
    """Тест функции распарсивания URL.

    Note:
        Неверный URL github.
    """""
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        url_parser(GITHUB_URL_FAKE)
    assert pytest_wrapped_e.type == SystemExit
