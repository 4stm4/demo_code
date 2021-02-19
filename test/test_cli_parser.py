"""Тесты модуля CLI parser."""
import argparse
import datetime

import pytest
from app_code.cli_parser import create_parser

TEST_ARGS: list = ['-u', 'https://github.com/ytisf/theZoo',
                   '-s', '2020-11-11', '-e', '2020-11-16']
TEST_PARAMS = argparse.Namespace(
    b='master',
    e=datetime.date(2020, 11, 16),
    s=datetime.date(2020, 11, 11),
    u='https://github.com/ytisf/theZoo'
)


def test_create_parser():
    """Тест функции проверки парсера."""
    assert create_parser(TEST_ARGS) == TEST_PARAMS
