import books as b

books = b.books

def search():
    print("How would you like to search for the book?")
    print("1. By Title")
    print("2. By Author")
    print("3. By Year")
    print("4. Return")
    try:
        choice = int(input(""))
        response(choice)
    except ValueError:
        print("Please enter a valid number.")

def response(choice):
    if choice == 1:
        result = search_title(input("Enter the book title: "))
    elif choice == 2:
        result = search_author(input("Enter the author name: "))
    elif choice == 3:
        result = search_year(input("Enter the publication year: "))
    elif choice == 4:
        print("")
        return
    if result:
        print(f"Book found: {result}")
    else:
        print("Nothing found")

def search_title(name):
    for book in books:
        if name.lower() == book["name"].lower():
            return book
    return None

def search_author(name):
    for author in books:
        if name.lower() == author["author"].lower():
            return author
    return None

def search_year(name):
    for year in books:
        if name.lower() == year["date"].lower():
            return year
    return None