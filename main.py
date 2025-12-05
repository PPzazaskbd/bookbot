from stats import * 
import sys


def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    
    num = count_words(filepath)
    chars = count_chars(filepath)
    list_chars = dict_to_list(chars)
    list_chars.sort(reverse=True , key=sort_on)    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num} total words")
    print("--------- Character Count -------")
    
    for list in list_chars:
        if list["char"].isalpha() == False:
            continue
        print(f"{list["char"]}: {list["num"]}")




    print("============= END ===============")
    return 0






main()