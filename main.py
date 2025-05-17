def main (filepath):
    book = get_book_text (filepath)
    num_words = get_num_words (book)
    num_chars = get_num_chars (book)
    print (f"{num_words} words found in the document")
    print (num_chars)
     
def get_book_text (filepath):
    with open(filepath) as file_object:
        book_text=file_object.read()
    return book_text

from stats import get_num_words

from stats import get_num_chars

main("books/frankenstein.txt")