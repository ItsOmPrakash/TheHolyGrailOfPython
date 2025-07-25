# Implement a Python program that prompts the user to enter an integer. 
# Define a function describe_number(num) that returns a descriptive string about the number:
    # "Positive and Even"
    # "Positive and Odd"
    # "Negative and Even"
    # "Negative and Odd"
    # "Zero"
# Use combined conditional logic (and, or, nested if). Your program should print the description of the entered number.

#--------------------------------------------------------------

def main() :
    userInput= int(input("enter an integer: "))
    describe_number(userInput)

def describe_number(num):
    if num > 0  :
        if num% 2 ==0:
            print("Positive and Even")
        else :
            print("Positive and Odd")
    elif num < 0 :
        if num% 2 ==0 :
            print("Negative and Even")
        else :
            print("Negative and Odd")
    else :
        print("Zero")
        
main()