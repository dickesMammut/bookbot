from typing import Dict
from stats import get_num_words, get_num_characters, get_sorted_dict # type: ignore

print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")
number_of_words: int = get_num_words() # type: ignore
print(f"Found {number_of_words} total words")
print("--------- Character Count -------")

number_of_characters: Dict[str, int] = get_num_characters()
sorted_list_of_characters: list = get_sorted_dict(number_of_characters)
char_count: Dict
for char_count in sorted_list_of_characters:
    if char_count[0].isalpha():
        print(f"{char_count[0]}: {char_count[1]}")