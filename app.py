"""Результаты анализа."""
from argparse import Namespace
from datetime import date
from sys import argv, stdout
from typing import Tuple

from app_code.cli_parser import create_parser  # type: ignore
from app_code.git_worker import commits_top, open_close_old  # type: ignore
from app_code.url_handler import url_check, url_parser  # type: ignore

ISSUES_DAY_TO_OLD: int = 14
PULLS_DAY_TO_OLD: int = 30


def main():
    """Основная программа."""
    input_params: Namespace = create_parser(argv[1:])
    owner: str
    repo: str
    owner, repo = url_parser(input_params.u)
    if url_check(owner, repo):
        request_data: Tuple[str, str, date, date, str] = (
            owner,
            repo,
            input_params.s,
            input_params.e,
            input_params.b,
        )
        result_commits: str = commits_top(request_data)
        result_pulls: Tuple[int, int, int] = open_close_old(
            PULLS_DAY_TO_OLD,
            'pulls',
            request_data,
        )
        result_issues: Tuple[int, int, int] = open_close_old(
            ISSUES_DAY_TO_OLD,
            'issues',
            request_data,
        )
        stdout.write(result_commits)
        stdout.write(
            'Количество открытых = %s, закрытых = %s, \
            старых = %s pull requests.\n' % result_pulls,
        )
        stdout.write(
            'Количество открытых = %s, закрытых = %s, \
            старых = %s issues.\n' % result_issues,
        )


if __name__ == '__main__':
    main()
