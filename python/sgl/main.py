import add_book as ab
import books as b
import search_book as sb

books = b.books
exit = False

def home():
    print("Welcome to the library")
    while exit == False:
        print("What would you like to do? (Enter the number of the option)")
        print("1. Add")
        print("2. Search")
        print("3. Exit")
        try:
            response = int(input(""))
            check_response(response)
        except ValueError:
            print("Please enter a valid number.")


def check_response(response):
    if response == 1:
        # add book
        ab.add()
        return
    elif response == 2:
        # search book
        sb.search()
        return
    elif response == 3:
        global exit
        input("Thank you for using our service")
        exit = True
        return exit

# main
if __name__ == "__main__":
    home()