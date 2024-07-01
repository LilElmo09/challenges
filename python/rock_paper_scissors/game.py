import random as r

options = ['rock', 'paper', 'scissors']

# Player choices
player_choice = ''
pc_choice = ''

# Statistics
wins = 0
losses = 0
draws = 0

while True:
    # Player's choice
    player_choice = input("Choose: Rock, Paper, or Scissors (Or write 'Exit' to end the game): ").lower()
    pc_choice = options[r.randrange(0,3)] 

    # Exit
    if player_choice == "exit":
        print(f"Final results: You won {wins} time(s), computer won {losses} time(s), draws {draws} time(s)")
        input("Thanks for playing")
        break
    
    if player_choice not in options:
        print("Invalid input. Please choose from 'rock', 'paper', or 'scissors'.\n")
        continue
    # Draw
    if player_choice == pc_choice:
        draws += 1
        print("Draw\n")
    # Paper vs Rock
    elif player_choice == options[1] and pc_choice == options[0]:
        wins += 1
        print("You win\n")
    # Rock vs Scissors
    elif player_choice == options[2] and pc_choice == options[1]:
        wins += 1
        print("You win\n")
    elif player_choice == options[0] and pc_choice == options[2]:
        wins += 1
        print("You win\n")
    else:
        losses += 1
        print("PC wins\n")
