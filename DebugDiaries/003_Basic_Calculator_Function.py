# Implement a Python function named add_two_numbers that takes two numeric arguments, num1 and num2. 
# The function should return their sum. In your main program, get two numbers from the user, 
# convert them to the appropriate numeric type, call the add_two_numbers function, and print the result.

#-------------------------------------------------------------

def main() :
    num1=float(input("Enter first number: "))
    num2=float(input("Enter second number: "))
    add_two_number(num1, num2)

def add_two_number(num1, num2):
    print(F"Sum of two number is {num1 + num2}")

main()
