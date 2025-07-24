# Implement a Python program that prompts the user to enter an integer.
# Use conditional statements (if, elif, else) to determine if the number is positive, negative, or zero, 
# and print an appropriate message (e.g., "The number is positive.", "The number is negative.", or "The number is zero.").

#-------------------------------------------------------------

intVar= int(input("what number do you wanna check: "))

if intVar > 0 :
    print("The number is positive.") 
elif intVar < 0 :
    print("The number is negative.")
else :
    print("The number is zero.")
    