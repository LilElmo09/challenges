import books as b

book = []
def add ():
    print("Enter the requested data")
    name = input("Book title: ")
    author = input("Author's name: ")
    date = input("Publication date: ")
    book = {
        "name": name,
        "author": author,
        "date": date
    }
    b.books.append(book)
    print("Successfully added \n")