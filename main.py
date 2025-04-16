import sys
from stats import word_count, char_count, sort_dict

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()

    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    word_count(get_book_text(sys.argv[1]))
    print("--------- Character Count -------")
    count_dict = char_count(get_book_text(sys.argv[1]))
    sorted_chars = sort_dict(count_dict)
    for dic in sorted_chars:
        if not dic["char"].isalpha():
            continue
        print(f"{dic["char"]}: {dic["count"]}")
    print("============= END ===============")

main()
