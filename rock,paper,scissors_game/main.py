import random

user_win = 0
computer_win = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input(f"Enter you choice {options}:(q to quit): ").lower() 
    if user_input == "q":
        break
    if user_input not in options:
        continue
    #Rock(0), Paper(1), Scissors(2)
    random_number = random.randint(0,2)
    computer_pick =options[random_number]
    print(f"Computer Pick {computer_pick}") 
    if user_input == computer_pick:
        print("The game draw")

    elif user_input == "rock" and computer_pick == "scissors":
        print("You win")
        user_win += 1
        
    elif user_input == "paper" and computer_pick == "rock":
        print("You win")
        user_win += 1 
        
    elif user_input == "scissors" and computer_pick == "paper":
        print("You win")
        user_win += 1
        
    else:
        print("You lost")
        computer_win += 1     
print("-----------SCORE BOARD-----------")           
print(f"Computer Win {computer_win} Times")
print(f"You Win {user_win} Times")
 

