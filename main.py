import sys
from stats import count_words, number_of_characters, sort_character_counts

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    # Check command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)  # Exit with status code 1 to indicate error

    book_path = sys.argv[1]
    print("=========== BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    print(f"Found {word_count} total words")
    
    print("--------- Character Count -------")
    character_counts = number_of_characters(book_text)
    sorted_characters = sort_character_counts(character_counts)

    for item in sorted_characters:
        char = item["character"]
        count = item["count"]
        # Skip spaces and non-letter characters for clean output
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

main()