def counter(book):
    list = book.split()
    return len(list)

def l_counter(x):
    dict = {}
    small = x.lower()
    for l in small:
        if l in dict:
           dict[l] = dict[l] + 1
        else:
            dict[l] = 1

    return dict