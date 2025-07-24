# Implement a Python program that prompts the user to enter an email address. 
# Define a function validate_email(email_str) that takes the email string as input. 
# Inside the function, use string methods and conditional statements to perform a basic validation:
    # It must contain exactly one '@' symbol.
    # It must contain at least one '.' (dot) symbol after the '@' symbol.
    # The '@' symbol must appear before the first '.' symbol.
# The function should return True if all conditions are met, False otherwise. 
# Your program should then print whether the entered email is 'Valid' or 'Invalid'.

#-----------------------------------------------------------------------------

def main():
    email_str = input("Enter your email address: ")
    value = validate_email(email_str)
    if value ==True :
        print("Valid")
    else :
        print("Invalid")

def validate_email(email_id):
    if "@" in email_id :
        a = email_id.split("@")
        x, y= a

        if "." in x :
            return False
        elif "." in y :
            return True
        else :
            return False
    else :
        return False
    
main()






#REMARK -------
# email validation code is partially correct but has issues with 
# handling multiple '@' symbols and rigorously enforcing the "before the first dot" rule.