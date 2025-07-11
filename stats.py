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


# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(items):
    return items["num"]


def order_character_dict(char_dict):
    ordered_dict = []

    for char in char_dict:
        ordered_dict.append({"char": char, "num": char_dict[char]})
    ordered_dict.sort(reverse=True, key=sort_on)
    return ordered_dict
