# Implement a Python program that prompts the user to create a password. Define a function check_password_strength(password) 
# that takes the password string. This function should return a string indicating its strength:
    # "Strong" if the length is 10 or more characters.
    # "Medium" if the length is between 6 and 9 characters (inclusive).
    # "Weak" if the length is less than 6 characters.   

# Your program should then print the strength of the entered password.

#--------------------------------------------------------------------

def main():
    createPassword= input("create a password: ")
    check_password_strength(createPassword)


def check_password_strength(password):
    lenofPassword=len(password) 
    if lenofPassword>=10 :
        print("Strong")
    elif lenofPassword>=6 :
        print("Medium")
    else :
        print("Weak")


main()
