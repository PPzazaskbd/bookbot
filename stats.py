
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

    

def count_words(text):
    
    return len(get_book_text(text).split())


def count_chars(text):
    dict = {}
    book = get_book_text(text)
    for char in book:
        char = char.lower()
        if char not in dict:
            dict[char] = 0
        dict[char] += 1
    return dict
                 
def dict_to_list(dict):
    list =[]
    for k,v in dict.items():
        list.append({
            "char" : k ,"num" : v
        })
    return list

def sort_on(item):
    return item["num"]