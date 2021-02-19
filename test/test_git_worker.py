"""Тесты модуля Git worker."""
from datetime import date
from typing import Tuple

from app_code.git_worker import commits_top, open_close_old

TEST_REQUEST_DATA: Tuple[str, str, str, date, date, str] = (
    'ytisf',
    'theZoo',
    date(2020, 1, 1),
    date(2020, 11, 1),
    'master'
)
TEST_DAY_TO_OLD: int = 30
TEST_REQUEST_TYPE: str = 'pulls'


def test_open_close_old():
    """Тест функции статистики."""
    assert open_close_old(
        TEST_DAY_TO_OLD,
        TEST_REQUEST_TYPE,
        TEST_REQUEST_DATA,
    ) == (7, 32, 7)


def test_commits_top():
    """Тест функции статистики."""
    assert len(commits_top(TEST_REQUEST_DATA)) == 166
