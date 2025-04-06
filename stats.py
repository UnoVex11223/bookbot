def get_book_text(filepath):
    with open(filepath, encoding="utf-8") as f:
        return f.read()

def number_of_characters(book_text):
    character_count_dictionary = {}
    for symbol in book_text.lower():
        if symbol not in character_count_dictionary:
            character_count_dictionary[symbol] = 1
        else:
            character_count_dictionary[symbol] += 1
    return character_count_dictionary

def sort_on(dict):
    return dict["count"]

def sort_character_counts(character_counts):
    character_list = []
    for character, count in character_counts.items():
        character_list.append({"character": character, "count": count})
    character_list.sort(reverse=True, key=sort_on)
    return character_list

def count_words(book_text):
    words = book_text.split()
    return len(words)


