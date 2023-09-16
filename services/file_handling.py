import os
import sys

BOOK_PATH = 'book/i_ne_ostalos_nikogo_ru.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, page_size: int) -> tuple[str, int]:
    t = text[start:(start + page_size)][::-1]
    s = ',.!:;?'
    for ind, val in enumerate(t):
        if val in s and t[ind + 1] in s or val in s and t[ind - 1] in s:
            page_size -= 1
            continue
        if val not in s:
            page_size -= 1
        else:
            break
    res = text[start:(start + page_size)]
    return res, len(res)


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    with open(path, 'r', encoding='utf-8') as f:
        book_text = f.read()
    start_page = 0
    page_number = 1
    while start_page < len(book_text):
        page_bookmark, bookmark_size = _get_part_text(
            book_text, start_page, PAGE_SIZE)
        book[page_number] = page_bookmark.lstrip()
        page_number += 1
        start_page += bookmark_size


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))
