# Implement a Python program that prompts the user to enter a word or phrase. 
# Define a function is_palindrome(text) that determines if the input is a palindrome. 
# The function must first "clean" the input string by converting it to lowercase and removing all spaces. 
# Then, it should check if the cleaned string is equal to its reverse. 
# (Hint: you can reverse a string s with s[::-1]). The function should return True if it's a palindrome and False otherwise. 
# Your program should print a message like "'[user's input]' is a palindrome." or "'[user's input]' is not a palindrome."

#--------------------------------------------------------------------------------------
def main() :
    userInput = input("What srting do you want to check: ").lower().strip()
    is_palindrome(userInput)

def is_palindrome(text) :
    if text == text[::-1] :
        print(f"{text} is a palindrome")
    else :
        print(f"{text} is not a palindrome")
    
main()