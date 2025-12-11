import sys
from stats import word_counter, character_counter, sort_characters

def get_book_text(file_path):
    file_contents = ""
    with open(file_path, encoding='utf-8-sig') as f:
        file_contents = f.read()

    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    content = get_book_text(sys.argv[1])
    char_count = character_counter(content)
    sorted_chars = sort_characters(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_counter(content)} total words")
    print("--------- Character Count -------")
    for char in sorted_chars:
        print(f"{char["char"]}: {char["num"]}")


main()
        
