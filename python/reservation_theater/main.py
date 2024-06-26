exit = True
theater = [[0 for _ in range(10)] for _ in range(5)]

def main():
    print('Welcome to the theater reservation system')
    while exit:
        response = presentation()
        check_response(response)

def presentation():
    print('1. Show seats')
    print('2. Reserve seats')
    print('3. Cancel seats')
    print('4. Exit')
    try:
        response = int(input('Option: '))
    except:
        print('Invalid response')
    return response

def check_response(response):
    global exit
    if response == 1:
        show_seats()
    elif response == 2:
        reserve_seats()
    elif response == 3:
        cancel_seat()
    elif response == 4:
        exit = False
        input('Thank you for using our services')
    else:
        print('Invalid response')

def show_seats():
    for row in theater:
        print(' '.join(str(seat) for seat in row))
    input()

def reserve_seats():
    show_seats()
    row = int(input('1 is top row and 5 is bottom row\nWhich row do you want to reserve: '))
    seat = int(input('1 is leftmost seat and 10 is rightmost seat\nWhich seat do you want to reserve: '))
    row -= 1
    seat -= 1
    if theater[row][seat] == 0:
        theater[row][seat] = 1
        print('Seat reserved')

def cancel_seat():
    show_seats()
    row = int(input('1 is top row and 5 is bottom row\nWhich row do you want to cancel: '))
    seat = int(input('1 is leftmost seat and 10 is rightmost seat\nWhich seat do you want to cancel: '))
    row -= 1
    seat -= 1
    if theater[row][seat] == 1:
        theater[row][seat] = 0
        print('Seat canceled')

if __name__ == '__main__':
    main()