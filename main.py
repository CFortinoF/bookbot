from stats import get_num_words, get_chars, sorted_list_of_dictionaries

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    book_location = "books/frankenstein.txt"
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