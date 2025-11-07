# Implement a program that prompts the user for their full name. 
# Define a function get_initials(full_name) that takes a string and returns a new string of the initials, 
# with each initial capitalized and separated by a period. For example, if the input is "john fitzgerald kennedy", 
# the function should return "J.F.K.". You can achieve this by splitting the string into parts. 
# Your program should print the user's initials.


#---------------------------------------------------------------------------------------

def main():
    full_name= input("What is your full name: ").lower().strip()
    get_initials(full_name)

def get_initials(name):
    listed_name = name.split(" ")

    for words in listed_name :
        initials= words[0].upper()
        print(initials , end=".")
    
    print()

main()
