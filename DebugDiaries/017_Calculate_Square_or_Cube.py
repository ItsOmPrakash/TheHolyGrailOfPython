# Implement a Python program that prompts the user for a number and a choice ('square' or 'cube'). 
# Define a function calculate_power(number, operation) that takes the number (float) and the operation choice (string). 
# If the operation is 'square', return the number squared. If 'cube', return the number cubed.
# If the operation is invalid, return None. Your program should print the result or an "Invalid operation" message if None is returned.

#-----------------------------------------------------------------------

def main() :
    number= float(input("Whats the number: "))
    operation= input("Whats the oqperation you want to perform: ").lower().strip()

    if operation =="square" or operation == "cube":
        print(calculate_power(number, operation))
        
    else :
        print("Invalid operation")


def calculate_power(number, operation) :
    if operation =="square" :
        return pow(number,2)
    else :
        return pow(number,3)
    
main()