"""Модуль функции работы с URL."""
import sys
from typing import Dict, List, Tuple

from app_code.rest_worker import api_handler  # type: ignore

NOT_CORRECT_URL: str = 'Не верно указан URL.'
GITHUB_URL: str = 'https://github.com/'


def url_parser(url: str) -> Tuple[str, str]:
    """Разбираем url, достаем ownrer и repo.

    Args:
        url: адрес репозитория.

    Returns:
        параметры owner и repo.
    """
    url_params: List[str] = url.split('/')
    if url.find(GITHUB_URL) < 0 or len(url_params) < 5:
        sys.stdout.write(NOT_CORRECT_URL)
        sys.exit()
    return url_params[-2], url_params[-1]


def url_check(owner: str, repo: str) -> bool:
    """Проверяем существование репозитория.

    Args:
        owner: владелец репозитория.
        repo: название репозитория.

    Returns:
        True если репозиторий существует, иначе False.
    """
    rest_resp: Dict[...] = api_handler('check_repo', (owner, repo,))
    return rest_resp.get('name', None) == repo
