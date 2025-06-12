def get_num_words(text):
    words = text.split()
    count = len(words)
    return count

def count_character(text):
    text = text.lower()
    char_count = {}
    for letter in text:
        if letter not in char_count:
            char_count[letter] = 1
        else:
            char_count[letter] += 1
    return char_count
