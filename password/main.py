
# master_pwd = input("What is the master password: ")

# def view():
#     with open("pass.txt", "r") as f:
#         for line in f.readlines():
#             data = line.rstrip()
#             user, passw = data.split("!")
#             print("User: ", user, "Password : ", passw)

# def add():
#     name = input("Account Name: ")
#     pwd = input("Password: ") 

#     with open("pass.txt", "a") as f:
#         f.write(name +"!" + pwd + "\n")

        




# while True:
#     mode = input("Would you like to add a new password or view existing onec(view,add)(q to quit): ").lower()
#     if mode == "q":
#         break

#     if mode =="view":
#         view()
#     elif mode == "add":
#         add()
#     else:
#         print("Invalid mode.") 
#         continue 


class Person:
    def __init__(self,name,age,occu,aim):
        self.name = name
        self.age = age
        self.occu = occu
        self.aim = aim
    def info (self):
        print(f"Below the infomation of {self.name}")
        print(f"{self.name} is a {self.occu} . he is at {self.age} and he would like to become a {self.aim} ")
    def info_female (self):
        print(f"Below the infomation of {self.name}")
        print(f"{self.name} is a {self.occu} . she is at {self.age} and she would like to become a {self.aim} ")


while True:
    name = input("What's your name: ").lower()
    print(f"Welome {name} to join our community. Let's tell your biography")
    user_gender = input("Do you male or female : ").lower()
    user_age = input("Do you 18+ or not: ").lower()
    user_occu = input("What's you occupation: ").lower()
    user_aim = input("What's your aimbation(teacher, software developer): ").lower() 

    if user_gender == "male" and user_aim == "teacher":

        person1 = Person(name, user_age,user_occu, user_aim) 
        person1.info() 
        print("Wow, Great plan Those people who are teacher they are the builder of the nation")
        quit()

    elif user_gender == "female" and user_aim == "teacher":
        person1 = Person(name, user_age,user_occu, user_aim) 
        person1.info_female() 
        print("Wow, Great plan Those people who are teacher they are the builder of the nation")
        quit()

    elif user_gender == "male" and "software developer":

        person1 = Person(name, user_age,user_occu, user_aim) 
        person1.info()
        print("Wow, Great plan Those people who are software developer they are the high profesionate person")
        quit()

    elif user_gender == "female" and user_aim == "software developer":

        person1 = Person(name, user_age,user_occu, user_aim) 
        person1.info()
        print("Wow, Great plan Those people who are software developer they are the high profesionate person")
        quit()
            

    else:
        print("Oppos! sorry, you can't go to next without submit your bio")  
        continue  



    
