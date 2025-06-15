
def get_book_text(path_to_file) :
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents
def num_words() :
    split_words = get_book_text("books/frankenstein.txt").split()
    num_words = len(split_words)
    print(f"{num_words} words found in the document")