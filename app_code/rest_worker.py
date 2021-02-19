"""Обработчик request запросов."""
import json
import sys
from json.decoder import JSONDecodeError
from typing import Dict

from requests import exceptions, get

URLS: Dict[str, str] = {
    'check_repo': 'https://api.github.com/repos/%s/%s',
    'commits': """https://api.github.com/repos/%s/%s/commits?since=%sT00:00:00Z&until=%sT23:59:59Z&base=%s&page=%s&per_page=100""",
    'pulls': """https://api.github.com/repos/%s/%s/pulls?since=%sT00:00:00Z&until=%sT23:59:59Z&per_page=100&base=%s&page=%s&state=all""",
    'issues': """https://api.github.com/repos/%s/%s/issues?since=%sT00:00:00Z&until=%sT23:59:59Z&per_page=100&base=%s&page=%s&state=all""",
    'test_url': 'https://%splayrix.ru/',
    'wrong_test_url': 'http://yanbex.ru/%s'
}
HTTP_OK: int = 200
BAD_JSON: str = 'JSON decode error.'


def api_handler(url: str, *args) -> Dict:
    """Метод обработки request запросов.

    Args:
        url: URL репозитория.

    Returns:
        Ответ от REST API.
    """
    headers = {'accept': 'application/vnd.github.v3+json'}
    query = URLS[url] % args[0]
    responce = get(query, headers=headers)
    if responce.status_code != HTTP_OK:
        error_text: str = 'URL: {0}. ERROR: {1}'.format(
            query, responce.status_code)
        sys.stdout.write(error_text)
        sys.exit()
    try:
        resp_data = json.loads(responce.text)
    except JSONDecodeError:
        sys.stdout.write(BAD_JSON)
        sys.exit()
    return resp_data
