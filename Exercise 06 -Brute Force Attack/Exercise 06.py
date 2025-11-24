def password_system_basic():
    correct_password = "5678910"  
    while True:
        user_input = input("Enter password: ")
        
        if user_input == correct_password:
            print("Access granted! Welcome to the system.")
            break
        else:
            print("Wrong password. Please try again.")
password_system_basic()