# Implement a program that prompts the user for a raw filename string. 
# Define a function format_filename(raw_name) that performs the following clean-up operations on the string:
    # Removes any leading or trailing whitespace.
    # Converts the entire string to lowercase.
    # Replaces any internal spaces with hyphens (-).
    # If the filename does not already end with a common file extension (e.g., .txt, .csv, .py), it appends .txt to the end.
# Your program should print the cleaned and formatted filename.

user_input= input("enter a filename: ").lower().strip()
user_input= user_input.replace(" ","-")
file_ext= (".txt",".csv",".py",".pdf",".html",".java", ".xml")

has_ext=0
for ext in file_ext :
    if user_input.endswith(ext):
        has_ext=1
        print("Here is your cleaned file name ", user_input)

if not has_ext:
    user_input +=".txt"
    print ("Here is your cleaned file name", user_input)

