def main (filepath):
    book = get_book_text (filepath)
    print (book)

def get_book_text (filepath):
    with open(filepath) as file_object:
        book_text=file_object.read()
    return book_text

main("books/frankenstein.txt")