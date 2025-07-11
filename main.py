import sys

from stats import count_characters, get_words, order_character_dict


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    book_text = get_book_text(sys.argv[1])
    word_count = get_words(book_text)
    character_dict = count_characters(book_text)
    ordered_dict = order_character_dict(character_dict)

    print("============ BOOKBOT ============")
    print("Analyzing book found at " + sys.argv[1] + "...")
    print("----------- Word Count ----------")
    print("Found " + str(len(word_count)) + " total words")
    print("--------- Character Count -------")
    for char in ordered_dict:
        if char["char"].isalpha():
            print(char["char"] + ": " + str(char["num"]))
    print("============= END ===============")


if len(sys.argv) == 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main()
