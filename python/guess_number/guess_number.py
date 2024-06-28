import random as r
random_number = r.randrange(1, 100)
answer = 0
attempts = 1
print(random_number)

while True:
    answer = int(input("tell me a number: "))
    if answer == random_number:
        print(f"congratulations, you guessed the number in just {attempts} tries")
        break
    attempts += 1
    if answer > random_number:
        print("Too high")
    elif answer < random_number:
        print("Too low")