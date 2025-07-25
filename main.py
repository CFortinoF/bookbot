import sys
from stats import get_num_words, get_chars, sorted_list_of_dictionaries

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_location = sys.argv[1]
    book = get_book_text(book_location)
    num_words = get_num_words(book)
    sorted_list = sorted_list_of_dictionaries(get_chars(book))


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_location}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for rec in sorted_list:
        print(f"{rec['char']}: {rec['num']}")

main()