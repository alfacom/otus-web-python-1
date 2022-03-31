from pathlib import Path
from pprint import pprint
from typing import Sequence

import requests
from bs4 import BeautifulSoup


def get_path(path: str, port: int = 8000) -> str:
    return f'http://127.0.0.1:{port}{path}'


def get_from_path(path: str) -> requests.Response:
    response = requests.get(get_path(path))
    return response


def get_href(content: requests.Response) -> Sequence[str]:
    soup = BeautifulSoup(content.text, "html.parser")
    hrefs = soup.find_all('a')
    return [link.get('href') for link in hrefs]


def print_links(smthng: Sequence, to_where: str) -> None:
    if to_where == '0':
        pprint(smthng)
    else:
        log_file = Path() / 'log.txt'
        with log_file.open('a+') as fd:
            for line in smthng:
                fd.write(line)
                fd.write('\n')


def get_links(output: str, path: str = '/') -> Sequence[str]:
    content = get_from_path(path)
    all_links = get_href(content)
    print_links(all_links, output)
    return all_links


def main(output: str) -> None:
    all_links = get_links(output)
    for link in all_links:
        get_links(output, path=link)


if __name__ == '__main__':
    logging_to = input('Сохранить в файл или вывести в коносль?\r\n0) В консоль; 1) В файл\r\n>')
    main(logging_to)
