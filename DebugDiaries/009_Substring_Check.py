# Implement a Python program that prompts the user for two strings: a main_string and a substring. 
# Use a string method to check if the substring exists within the main_string (case-sensitive). 
# Print "Substring found!" if it exists, otherwise print "Substring not found."

#-------------------------------------------------------------

main_string= input("Whats the main String: ")
substring= input("What do you want to find: ")

if substring in main_string :
    print("Substring found!")
else :
    print("Substring not found")
    