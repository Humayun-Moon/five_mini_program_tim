import getpass
import hashlib

MASTER_PASSWORD = "secure_master_password"

def get_hash(password):
    # Use a strong hashing algorithm (e.g., SHA-256) to store hashed passwords
    hash_object = hashlib.sha256(password.encode())
    return hash_object.hexdigest()

def authenticate():
    attempts = 3
    while attempts > 0:
        entered_password = getpass.getpass("Enter the master password: ")
        if get_hash(entered_password) == get_hash(MASTER_PASSWORD):
            return True
        else:
            attempts -= 1
            print(f"Incorrect password. {attempts} attempts remaining.")
    print("Authentication failed. Exiting.")
    return False

def view():
    with open("pass.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("!")
            print("User:", user, "Password:", passw)

def add():
    name = input("Account Name: ")
    pwd = getpass.getpass("Password: ")

    with open("pass.txt", "a") as f:
        f.write(name + "!" + get_hash(pwd) + "\n")

if authenticate():
    while True:
        print("\nOptions:")
        print("1. View passwords")
        print("2. Add a new password")
        print("q. Quit")

        choice = input("Enter your choice: ").lower()

        if choice == "q":
            break
        elif choice == "1":
            view()
        elif choice == "2":
            add()
        else:
            print("Invalid choice.")
