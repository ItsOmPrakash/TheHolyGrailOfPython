# implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0.
#  If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. 
# Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.


#-------------------------------------------------------------


# taking users name as input
userInput = input("What's your name?? : ")
# making sure they get right input
userInput = userInput.strip().lower()

#checking the conditions
if  userInput.startswith("hello", 0) :
    print("$0")
elif userInput.startswith("h") :
    print("$20")
else :
    print("$100")

