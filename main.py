import os
import sys
from stats import num_of_words, num_of_characters,sorted_count

def get_book_text(book):
    with open(book, 'r') as f:
        file_content = f.read()
    return file_content


def main():
    b_path = sys.argv[1]
    char_count = sorted_count(b_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {b_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_of_words(b_path)} total words")
    print("--------- Character Count -------")
    for item in char_count:
        print(f"{item['char']}: {item['count']}")
    print("============= END ===============")

  
if len(sys.argv) == 2:
    main()
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    
