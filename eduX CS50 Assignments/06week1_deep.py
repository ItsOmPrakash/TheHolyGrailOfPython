# Implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, 
# Outputting "Yes" if the user inputs 42 or (case-insensitively) "forty-two" or "forty two". Otherwise output "No".


#-----------------------------------------------------------------------------------------------------------


# taking user input
answer = input("What's the answer to the great question of Life, Universe, Everything : ")
# making sure the correct string is checked
answer = answer.strip().lower()


if answer == "42" :
    print("yes")
elif answer == "forty-two" :
    print("yes")
elif answer == "forty two" :
    print("yes")
else :
    print("no")

