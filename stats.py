
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

    

def count_words(text):
    
    return len(get_book_text(text).split())


