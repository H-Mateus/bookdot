def get_words(book_text):
    words = book_text.split()
    return words


def count_characters(book_text):
    char_dict = {}
    words_lower = book_text.lower()
    for i in words_lower:
        letters = i.split()
        for letter in letters:
            if letter not in char_dict:
                char_dict[letter] = 0
            char_dict[letter] += 1
    return char_dict
