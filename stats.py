def get_book_text(filename) :
    with open(filename) as f:
        file_contents = f.read()
        return file_contents
    
def num_words(filename) :
    split_words = get_book_text(filename).split()
    num_words = len(split_words)
    print(f"Found {num_words} total words")

def character_repeat(text) :
    lowercase = text.lower()
    
    characters_dict = {}

    for char in lowercase :
        if char in characters_dict :
            characters_dict[char] += 1
        else :
            characters_dict[char] = 1

    return characters_dict
    print(characters_dict)

def sort_dict(characters_dict) :
    result_list = []

    for char, count in characters_dict.items() :
        if char.isalpha():
            result_list.append({"char": char, "num": count})

    result_list.sort(key=lambda x: x["num"], reverse=True)
    return result_list
