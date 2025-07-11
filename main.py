from stats import count_characters, get_words


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = get_words(book_text)
    character_dict = count_characters(book_text)

    print(str(len(word_count)) + " words found in the document")
    print(character_dict)


main()
