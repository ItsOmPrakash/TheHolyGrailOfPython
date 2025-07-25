# Implement a Python program that prompts the user for their first_name and last_name separately. 
# Define a function format_full_name(first, last) that returns the full name in the format "Last, First" 
# with both parts capitalized correctly (e.g., if input is "john" and "doe", output should be "Doe, John"). 
# Use appropriate string methods. Your program should print the formatted full name.

#-----------------------------------------------------

def main():
    firstName=input("What's your firstname: ")
    secondName= input("What's your lastname: ")
    format_full_name(firstName ,secondName)

def format_full_name(first,second):
    print(f"{second.title()}, {first.title()}") 

main()
