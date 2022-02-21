def print_upper_words(words):
    """prints words in uppercase"""

    for word in words:
        print(word.upper())


# print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])


def print_upper_words_e(words):
    """prints upper letter words that starts with "e" or "E"""

    for word in words:
        if word[0].lower() == "e":
            print(word.upper())

# print_upper_words_e(["hello", "ellen", "goodbye", "english", "Earl"])


def print_upper_words_letters(words, must_start_with):

    """prints upper letter words that starts with pass in letters"""
    for word in words: 
        for letter in must_start_with:
            if word[0].lower() == letter.lower():
                print(word.upper())

# print_upper_words_letters(["hello", "sing", "school", "morning"], must_start_with=["s", "h"])
 