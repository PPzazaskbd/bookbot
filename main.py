from stats import count_words


def main():
    filepath = "books/frankenstein.txt"
    
    num = count_words(filepath)
    print(f"Found {num} total words")
    return None






main()