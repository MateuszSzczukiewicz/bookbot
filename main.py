from collections import Counter
from typing import Dict

path_to_file = "books/frankenstein.txt"


def words_count(text: str) -> int:
    """Counts the number of words in the provided text."""
    return len(text.split())


def letter_count(text: str) -> Dict[str, int]:
    """Counts the occurrences of each letter in the provided text."""
    return Counter(letter for letter in text.lower() if letter.isalpha())


def main():
    with open(path_to_file) as f:
        file_contents = f.read()

        book_letter_dict = letter_count(file_contents)
        book_words_count = words_count(file_contents)

        print(f"--- Begin report of {path_to_file} ---")
        print(f"{book_words_count} words found in the document")
        print()
        for letter, count in book_letter_dict.items():
            print(f"The '{letter}' character was found {count} times")
        print("--- End report ---")


main()
