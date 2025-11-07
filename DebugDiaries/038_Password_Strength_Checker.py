# Implement a program that prompts the user for a password. Define a function check_password_strength(password) 
# that returns a string describing its strength. The function should perform multiple checks using a combination of string methods 
# and conditionals:
    # Weak: Length is less than 8 characters.
    # Medium: Length is between 8 and 11 characters (inclusive) and contains at least one uppercase letter OR one digit.
    # Strong: Length is 12 or more characters AND it contains at least one uppercase letter AND at least one digit.
# Your program should print the strength of the password.


def main():
    password= input("Enter your password: ")
    if password != None :
        check_password_strength(password)


def check_password_strength(password):
    pass_length=len(password)
    if pass_length < 8 :
        print("Your password strength is WEAK")
    elif 8<= pass_length<12 :
        if  is_upper(password) or password.isalnum():
            print("Your password strength is MEDIUM. You can improve")
        else:
            print("Your password strength is WEAK")
    elif pass_length>=12:
        if not is_upper(password) and password.isalnum():
            print("Your password strength is WEAK")
        else:
            print("Your password strength is STRONG")
    else:
        print("Invalid Operation")

def is_upper(password):
    for char in password:
        if not char.isupper():
            return False
        else:
            return True

main()

