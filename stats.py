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

def sort_on(dict):
    return dict["num"]

def sort(dictionary):
    list = []
    for key in dictionary:
        if key.isalpha():
            char_dict = {"char": key, "num": dictionary[key]}
            list.append(char_dict)
    list.sort(reverse=True, key=sort_on)
    return list
