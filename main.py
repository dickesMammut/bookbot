from typing import Dict
from stats import get_num_words, get_num_characters # type: ignore

number_of_words: int = get_num_words() # type: ignore
print(f"{number_of_words} words found in the document")
number_of_characters: Dict[str, int] = get_num_characters()
print(number_of_characters)