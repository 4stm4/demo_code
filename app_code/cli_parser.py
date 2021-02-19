"""Парсер параметров командной строки."""
from argparse import ArgumentParser, Namespace
from datetime import date

START_YEAR = 1900


def create_parser(args: list) -> Namespace:
    """Coздаем парсер входных параметров.

    Returns:
        параметры командной строки.

    """
    parse_params = ArgumentParser(
        prog='app',
        description='Тестовое задание для Playrix.',
        epilog='Захарченко Алексей (i@4stm4.ru). 15 ноября 2020 года.',
    )
    parse_params.add_argument(
        '-u',
        type=str,
        required=True,
        metavar='URL РЕПОЗИТОРИЯ',
        help='URL публичного репозитория на github.com.',
    )
    parse_params.add_argument(
        '-s',
        default=date(START_YEAR, 1, 1),
        type=date.fromisoformat,
        metavar='ДАТА НАЧАЛА',
        help='Дата начала анализа. Формат ввода YYYY-MM-DD.',
    )
    parse_params.add_argument(
        '-e',
        default=date.today(),
        type=date.fromisoformat,
        metavar='ДАТА ОКОНЧАНИЯ',
        help='Дата окончания анализа. Формат ввода YYYY-MM-DD.',
    )
    parse_params.add_argument(
        '-b',
        default='master',
        type=str,
        metavar='ВЕТКА РЕПОЗИТОРИЯ',
        help='Ветка репозитория. По умолчанию - master.',
    )
    return parse_params.parse_args(args)
