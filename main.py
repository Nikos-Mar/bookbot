import sys
from stats import sort_chars_dict
from stats import get_word_count
from stats import get_chars_dict

def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    if (len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_book = sys.argv[1]
    

    chars_list = sort_chars_dict(get_chars_dict(get_book_text(path_to_book)))
    
    

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")

    print(f"Found {get_word_count(get_book_text(path_to_book))} total words")

    print("--------- Character Count -------")

    for d in chars_list:
        if (d["char"].isalpha()):
            print(f"{d["char"]}: {d["num"]}")
        
    print("============= END ===============")


main()