# Dictionary to store registered users
registered_users = {}

def register():
    print("=== Register ===")
    while True:
        newuser = input("Username : ")
        if newuser in registered_users:
            print("Username already exists, Try another one")
            continue
        newpass = input("Password : ")
        confpass = input("Confirm Password : ")
        
        if newpass == confpass:
            registered_users[newuser] = newpass
            print("Registration successful.\n")
            break
        else:
            print("Passwords do not match. Try again.\n")

def login():
    print("=== Login ===")
    username = input("Username: ")
    password = input("Password: ")
    
    if username in registered_users:
        if registered_users[username] == password:
            print("Logged in successfully.")
        else:
            print("Incorrect password.")
    else:
        print("Username not found. Please register.")
        register()
        login() 

def run():
    while True:
        choice = input("Do you have an account? (yes/no): ").strip().lower()
        if choice == "yes":
            login()
            break
        elif choice == "no":
            register()
            login()
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

run()

