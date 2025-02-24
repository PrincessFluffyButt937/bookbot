def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = counter(text)
    print(f"{words} words found in the document")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def counter(book):
    list = book.split()
    return len(list)


main()
