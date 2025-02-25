def main():
    from stats import counter
    from stats import l_counter
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = counter(text)
    letter_count = l_counter(text)
    print(f"{words} words found in the document")
    print(letter_count)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
