from stats import get_num_words_in_book, get_num_characters_in_book

def get_book_text(filepath):
    file_contents = None
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    frankenstein_text = get_book_text("books/frankenstein.txt")
    frankenstein_text_word_count = get_num_words_in_book(frankenstein_text)
    print(f"{frankenstein_text_word_count} words found in the document")
    
    character_counts = get_num_characters_in_book(frankenstein_text)
    print(character_counts)
main()
