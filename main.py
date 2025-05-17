def main (filepath):
    book = get_book_text (filepath)
    num_words = count_words (book)
    print (f"{num_words} words found in the document")
     
def get_book_text (filepath):
    with open(filepath) as file_object:
        book_text=file_object.read()
    return book_text

def count_words (text):
    words=text.split()
    cnt_words= len(words)
    return cnt_words

main("books/frankenstein.txt")