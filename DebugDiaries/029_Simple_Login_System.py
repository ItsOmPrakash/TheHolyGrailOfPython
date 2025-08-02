# Implement a Python program that simulates a login prompt. First, 
# create two variables at the top of your script, correct_username = "admin" and correct_password = "P@ssw0rd123". 
# Prompt the user to enter their username and password. 
# Define a function check_credentials(entered_user, entered_pass) that compares the user's input against the correct credentials. 
# The function should return one of three strings: "Login successful", "Incorrect password", or "Username not found". 
# Use nested conditional statements to check the username first, then the password.

correct_username = "admin"
correct_password = "P@ssw0rd123"

def main() :
    username = input("enter your username: ")
    password = input("enter your password: ")
    check_credentials(username, password)

def check_credentials(entered_user, entered_pass):
    if entered_user == correct_username :
        if entered_pass == correct_password :
            print("Login successful")
        else :
            print("Incorrect password")
    else :
        print("Username not found")

    


main()
