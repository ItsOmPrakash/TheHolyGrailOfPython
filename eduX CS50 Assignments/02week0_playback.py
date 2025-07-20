

# Implement a program in Python that prompts the user for input and then outputs that same input,
# replacing each space with ... (i.e., three periods).

#-------------------------------------------------------

# taking user input
userInp = input("What do you want to say : ")
# removing space and using ...
userOut = userInp.replace(" " , "...")
# printing output
print(f"Here is your modified output: {userOut}")
