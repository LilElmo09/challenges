import json

menu = 'menu.json'
exit = False
total = 0

with open(menu, 'r') as file:
    menu = json.load(file)

def presentation():
    print('Welcome to the coffee shop')
    print('This is our menu:')
    for x in menu['coffee']:
        print(f"{menu['coffee'].index(x) + 1}. {x['name']}\t${x['price']}")
    response()
    print(total)

def response():
    global exit, total
    while not exit:
        try:
            value = search_coffee(int(input("Enter the number of the coffee you want to order (0 to exit): ")))
            if exit:
                break
            quantity = int(input("How many units?: "))
            result = value * quantity
            total += result
        except ValueError:
            print("Invalid option")
    return total

def search_coffee(number):
    global exit
    if number == 0:
        exit = True
        return 0
    elif 1 <= number <= len(menu['coffee']):
        return menu['coffee'][number - 1]['price']
    else:
        print('Invalid number')
        return 0
        

if __name__ == "__main__":
    presentation()