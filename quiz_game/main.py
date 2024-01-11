import random

print("Welcome to my computer quiz game! ") 

score = 0


playing = input("Do you want to play (yes or no): ")
# print(playing) 

if playing.lower() != "yes":
    quit() 
print("Okay! Let's play: ")

answer = input("What does GPU stand for? ")
if answer.lower() =="graphics processing unit":
    print("Correct") 
    score += 1
else:
    print("Incorrect")
    print("Correct answer is : graphics processing unit") 

answer = input("What does RAM stand for? ")
if answer.lower() =="random access memory":
    print("Correct")
    score += 1

else:
    print("Incorrect")
    print("Correct answer is : random access memory") 

answer = input("What does CPU stand for? ")
if answer.lower() =="central processing unit":
    print("Correct")
    score += 1

else:
    print("Incorrect")
    print("Correct answer is : central processing unit")

answer = input("What does HTML stand for? ")
if answer.lower() =="hyper text markup language":
    print("Correct") 
    score += 1

else:
    print("Incorrect")
    print("Correct answer is : hyper text markup language") 

print("----------YOUR RESULT-------------")

print("You got " + str(score) + " question correct")
get_percent = (score/4 )*100
print(f"Your accuracy is {get_percent}%")
    
