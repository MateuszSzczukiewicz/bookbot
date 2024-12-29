path_to_file = "books/frankenstein.txt"


def words_count(text):
    words = text.split()
    count = 0
    for _ in words:
        count += 1

    return count


def main():
    with open(path_to_file) as f:
        file_contents = f.read()
        print(words_count(file_contents))


main()
