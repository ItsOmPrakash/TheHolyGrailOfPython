# Implement a Python program that prompts the user to enter a decimal number (float). 
# Use a numeric method or function to round this number to the nearest whole integer. 
# Print both the original number and the rounded integer.

#-------------------------------------------------------------

userInput=float(input("What number do you want to enter: "))
roundInput= round(userInput)
print(f"Here's the original number {userInput} and the rounded integer {roundInput}")

