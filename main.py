

def main():
    filepath = "books/frankenstein.txt"
    books = get_book_text(filepath)
    num = count_words(books)
    print(f"Found {num} total words")
    return None




def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

    

def count_words(text):
    
    return len(text.split())





main()