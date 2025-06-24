#book report
import sys
if len(sys.argv) == 2:
    path_to_file = sys.argv[1]
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    
from stats import get_num_words, get_char_counts, sort_dictionary
if __name__ == "__main__":
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(path_to_file)} total words")
    print("--------- Character Count -------")
    chars = get_char_counts(path_to_file)
    sorted_chars = sort_dictionary(chars)
    for items in sorted_chars:
        print(f"{items["char"]}: {items["num"]}")
    
    
    print("============= END ===============")