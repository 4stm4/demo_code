"""Модуль работы с Github REST API."""
from collections import Counter
from datetime import date, timedelta
from typing import Dict, List, Optional, Tuple

from app_code.rest_worker import api_handler  # type: ignore

COMMITS_PER_PAGE: int = 100
TOP_COMMITER_CNT: int = 30


def commits_top(request_data: Tuple[str, str, date, date, str]) -> str:
    """Самые активные участники.

    Note:
        Таблица из 2 столбцов: login автора, количество его коммитов.
        Таблица отсортирована по количеству коммитов по убыванию.
        Не более 30 строк. Анализ производится на заданном периоде времени
        и заданной ветке.

    Args:
        request_data: данные для запроса. Tuple(owner, type,\
        date_start, date_end, branch) owner владелец репозитория;\
        repo репозиторий; date_start период времени,\
        начало временного отрезка; date_end период времени,\
        конец временного отрезка; branch заданная ветка.

    Returns:
        таблица с результатами.

    """
    current_page: int = 1
    pages_end: bool = False
    commiters: Counter = Counter()
    while not pages_end:
        commits: Dict[str, str] = api_handler(
            'commits',
            request_data + (current_page,),
        )
        if len(commits) == COMMITS_PER_PAGE:
            current_page += 1
        else:
            pages_end = True
        for commit in commits:
            login: str = commit['commit']['author']['name']
            commiters[login] += 1
    top_rate_string: str = 'Самые активные участники:\
        login автора, количество коммитов.\n'
    for commiter in commiters.most_common(TOP_COMMITER_CNT):
        top_rate_string += '{0:40s} {1:6d} \n'.format(*commiter)
    return top_rate_string


def open_close_old(
    days_to_old: int,
    request_type: str,
    request_data: Tuple[str, str, date, date, str],
) -> Tuple[int, int, int]:
    """Статистика по pull requests и issues.

    Args:
        days_to_old: количество дней для 'устаревания'.
        request_type: type issues или pulls
        request_data: данные для запроса. Tuple(owner, repo,\
        date_start, date_end, branch)

    Returns:
        Кортеж с тремя показателями [открытые, закрытые, устаревшие].

    """
    current_page: int = 1
    pages_end: bool = False
    cnt_open: int = 0
    cnt_close: int = 0
    cnt_old: int = 0
    date_old: Optional[str] = str(date.today() - timedelta(days=days_to_old))
    while not pages_end:
        pulls: List[Dict[str, str]] = api_handler(
            request_type,
            request_data + (current_page,),
        )
        if len(pulls) == COMMITS_PER_PAGE:
            current_page += 1
        else:
            pages_end = True
        for pull in pulls:
            if pull.get('state', '') == 'open':
                cnt_open += 1
                if pull.get('created_at', '1900-01-01') < str(date_old):
                    cnt_old += 1
            elif pull.get('state', '') == 'closed':
                cnt_close += 1
    return (cnt_open, cnt_close, cnt_old)
