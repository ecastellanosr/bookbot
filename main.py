from stats import get_num_words, count_character, sort
import sys 

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1] 
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    char_dict = count_character(book_text)
    sorted_list = sort(char_dict)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in sorted_list:
        print(f"{dict["char"]}: {dict["num"]}")

main()
