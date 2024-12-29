path_to_file = "books/frankenstein.txt"


def words_count(text):
    words = text.split()
    count = 0
    for _ in words:
        count += 1

    return count


def letter_count(text):
    letter_dict = {}

    for letter in text.lower():
        if letter.isalpha():
            if letter not in letter_dict:
                letter_dict[letter] = 0
            else:
                letter_dict[letter] += 1
        else:
            continue

    return letter_dict


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
