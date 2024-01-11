import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please type a number larger than 0")
        quit()
else:
    print("Please type a number next time")   
    quit()

random_num = random.randint(0,top_of_range)
guesses = 0

while True:
    guesses +=1
    user_quess = input("Make a guess: ")
    if user_quess.isdigit():
        user_quess = int(user_quess)
    else:
        print("Please type a number next time")

    if user_quess == random_num:
        print("You got it") 
        print(f"You got it in {guesses} guesses")        

        quit()
    elif user_quess > random_num:
        print("You were above the number")
    else:
        print("You were below the number")    
        


