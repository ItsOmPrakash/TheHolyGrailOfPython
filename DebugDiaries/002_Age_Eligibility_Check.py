# Implement a Python program that prompts the user for their age (as an integer). 
# Use a conditional statement (if-else) to check if the user is 18 years or older. 
# If they are, print "You are eligible to vote." Otherwise, print "You are not yet eligible to vote."

#-------------------------------------------------------------

ageVar= int(input("Tell me your age : "))

if ageVar>=18 :
    print("You are eligible to vote.")
else :
    print("You are not yet eligible to vote.")

