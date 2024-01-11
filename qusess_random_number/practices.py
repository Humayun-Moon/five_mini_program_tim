import random

print("Welcome to the battle, now We are going to play a awesome war")

player = input("Would you like to play the game (yes or else): ")

if player != "yes":
    quit()
else:
    print("Let's ready to play") 


top_of_range = input("Enter a number to top of range: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please, type a number larger than 0")
else:
    print("Please, Type a number to go next")

user_random = random.randint(0,top_of_range)
quesses = 0

while True:
    quesses += 1
    uesr_quess = input("Enter you Quess: ")
    if uesr_quess.isdigit():
        uesr_quess = int(uesr_quess)
    else:
        print("You can't type anything without number")
        print("Enter the a number to go aheah")
        continue

    if uesr_quess == user_random:
        print("You got it and win the war")
        print(f"You became able to win after {quesses} times try") 

        # break 
        quit()
    elif uesr_quess > user_random:
        print("You were above the number")
    else:
        print("You were below the number") 



       

