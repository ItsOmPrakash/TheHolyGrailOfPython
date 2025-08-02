# Implement a Python program that prompts a user for a desired username. 
    # Define a function clean_and_validate(username) that performs the following:
    # Removes any leading or trailing whitespace from the username.
    # Replaces all spaces within the username with an underscore _.
    # Converts the entire username to lowercase.
    # After cleaning, it checks if the username's length is between 5 and 15 characters (inclusive).
    # The function should return the cleaned, valid username. 
    # If the length is invalid after cleaning, it should return None. 
# Your program should print the valid username or a message like "Invalid username length." if the function returns None.

#-------------------------------------------------------------------------------------

def main( ):
    username = input("Whats your desired username: ")
    validatedUsername =clean_and_validate(username)

    if validatedUsername == None :
        print("Invalid username length.")
    else :
        print(f"Here's your clean and validated username {validatedUsername}")

def clean_and_validate(username) :
    username = username.strip().lower()
    username = username.replace(" ", "_")
    lenofusername= len(username)
    if lenofusername >= 5 and lenofusername <=15 :
        return username
    else :
        return None 

main()