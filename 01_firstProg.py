# This is a comment used to increse the readability of the code
# Multiple lines of comments can be used using Hash symbols for each line

#-----------------------------------------------------------------------------------------
# This is a simple program that prints "Hello World!" to the console
print("Hello World!") 
# The print function is used to output data to the console

#-----------------------------------------------------------------------------------------

input("Enter a value : ")  # This line takes input from the user 
# input() function is used to take input from the user

#-----------------------------------------------------------------------------------------

Value = input("Enter a value : ")  # This line takes input from the user and stores it in the variable 'Value'
#variable 'Value' can be used to store the value entered by the user
print(Value)  # This line prints the value stored in the variable 'Value' to the console
# The variable is dynamically typed, meaning it can hold any type of data
# The type of the variable can be checked using the type() function
print(type(Value)) # This line prints the type of the variable 'Value' to the console


#-----------------------------------------------------------------------------------------
# input() function returns the value entered by the user as a string
# To solve this, we can convert the input to an integer or float using int() or float() functions 
# This is called Type Conversion
SecValue = int(input("Enter a value : ")) # int() will convert the string input into integer 
print(type(SecValue)) # This line prints the type of the variable 'Value' to the console
