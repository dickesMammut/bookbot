import sys
from typing import Dict
from stats import get_num_words, get_num_characters, get_sorted_dict # type: ignore

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    PATH_TO_BOOK: str = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {PATH_TO_BOOK}...")
    print("----------- Word Count ----------")
    number_of_words: int = get_num_words(PATH_TO_BOOK) # type: ignore
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")

    number_of_characters: Dict[str, int] = get_num_characters(PATH_TO_BOOK)
    sorted_list_of_characters: list = get_sorted_dict(number_of_characters)
    char_count: Dict
    for char_count in sorted_list_of_characters:
        if char_count[0].isalpha():
            print(f"{char_count[0]}: {char_count[1]}")