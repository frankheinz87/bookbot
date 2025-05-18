def main (filepath):
    book = get_book_text (filepath)
    num_words = get_num_words (book)
    num_chars = get_num_chars (book)
    sorted_list=get_report (num_chars)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for item in sorted_list:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")

    print("============= END ===============")
     
def get_book_text (filepath):
    with open(filepath) as file_object:
        book_text=file_object.read()
    return book_text

from stats import get_num_words

from stats import get_num_chars

from stats import get_report

main("books/frankenstein.txt")