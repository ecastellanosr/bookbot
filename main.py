from stats import get_num_words, count_character

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    frankenstein_fp = "./books/frankenstein.txt"
    book_text = get_book_text(frankenstein_fp)
    num_words = get_num_words(book_text)
    char_dict = count_character(book_text)
    print(f"{num_words} words found in the document")
    print(char_dict)

main()
