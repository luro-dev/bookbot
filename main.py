from stats import get_num_words_in_book, get_num_characters_in_book, dict_to_sorted_list
import sys


def get_book_text(filepath):
    file_contents = None
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    book_text_word_count = get_num_words_in_book(book_text)
# print(f"{frankenstein_text_word_count} words found in the document")

    character_counts = get_num_characters_in_book(book_text)
# print(character_counts)

    sorted_list_of_character_counts = dict_to_sorted_list(character_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {book_text_word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_list_of_character_counts:
        for k,v in item.items():
            print(f"{k}: {v}")
    print("============= END ===============")

main()
