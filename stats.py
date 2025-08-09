def get_num_words_in_book(book_words):
    num_words = len(book_words.split())
    return num_words 

def get_num_characters_in_book(book_words):
    # includes symbols and spaces
    character_count = {}

    for character in book_words:
        character = character.lower()
        if character not in character_count:
            character_count[character] = 1
        else:
            character_count[character] += 1
    return character_count

def dict_to_sorted_list(dictonary_of_character_counts):
    def dict_sorted_by_character_count(dictionary):
        return max(dictionary.values())

    letter_counts = []

    for key, value in dictonary_of_character_counts.items():
        letter_counts.append({key: value})

    letter_counts.sort(key=dict_sorted_by_character_count, reverse=True)

    return letter_counts
    
