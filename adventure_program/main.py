print("Welcome to explore yourself /n with the brave mind")

name = input("Enter your name: ").lower()
print(f"Welcome again, {name} let's go to the explore yourself") 

answer = input(f"Hey {name}! Your back have blocked in the wall just you have two side to go so, now have to choice (left/right):-- ")

if answer == "right":
    print("Ok, You made the right dicision and you reached in the last edge now you have to choice your aimbition like (farmer/skill):--  ")
    right_input = input("farmer/skill:-- ")
    if right_input == "farmer":
        print("Wow, What an idia now you have to do cultivate your father land and take care of your parants")
    elif right_input == "skill":
        print("Great Plan It's going to best now what may you do(Web Developer or Software Developer)?")
        right_input_elif = input("web /software:--  ")
        if right_input_elif == "web":
            print("What a plan, This skills is high demendable but you need to a long terms dissare to learn and be patience")
        elif right_input_elif == "software":
            print("Wow , you want to become a computer programer I can't believe it because of it's need to a right mindset and have to do a lot of hard work but I now you are so lazy but it possiable if you keep doing consistensly")
        else: 
            print("Sorry, You can't do anything you are keep waiting to death")    



elif answer == "left":
    print("Wow, Good plan now you have to do marri fast do you agree or not")
    left_input = input("yes/not:-- ")
    if left_input == "yes":
        print("Oppops! Very poor idia at this moment if you want to marriy then you can't spend time to explore yourself")
    elif left_input == "not":
        print("Ok, Now you may do one thing that is alive long like that") 
    else:
        print("Sorry, You can't do anything you are keep waiting to death")    
        
else:
    print("Sorry, You can't do anything you are keep waiting to death")    