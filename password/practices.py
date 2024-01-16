master_pwd = input("Enter your password: ")

def add():
    name = input("Your name: ")
    password = input("Password: ")
    with open ("new_pass.txt", "a") as f:
        f.write(name + " " +password) 
def view():
    with open("new_pass.txt", "r") as f :
        for line in f.readlines():
            data = line.rstrip() 
            name , passw = data.split(" ")
            print(f"Name : {name}, password : {passw}")        
    


while True:
    mode = input("What do you want to  (add or view)(q to quit) your password: " ).lower()
    if mode == "q":
        break 
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Try again to")
        continue