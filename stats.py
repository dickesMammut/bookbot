from typing import Dict

def get_book_text(fp: str) -> str:
    with open(fp, encoding="utf-8") as f:
        file_contents: str = f.read()
    return file_contents

def get_num_words(fp: str) -> int:
    book_text: str = get_book_text(fp)
    list_of_words: list[str] = book_text.split()
    number_of_words: int = len(list_of_words)
    return number_of_words

def get_num_characters(fp: str) -> Dict[str, int]:
    book_text: str = get_book_text(fp).lower()
    num_of_characters: Dict[str, int] = {}
    c: str = ""
    for c in book_text:
        if c in num_of_characters.keys():
            num_of_characters[c] += 1
        else:
            num_of_characters[c] = 1

    return num_of_characters

def get_sorted_dict(num_of_chars: Dict[str, int]) -> list:
    sorted_chars: list = sorted(num_of_chars.items(), key = lambda item: item[1], reverse = True)
    return sorted_chars
