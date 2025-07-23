
# Python program can handle multiple aguments in the print() function 
# Printing multiple arguments in Python's print() function

#--------------------------------------------------------------------------------------------------------------

# Using commas to separate the arguments
print("Hello", "World", "from", "Python")  # This will print: Hello World from Python
# The print function can take multiple arguments separated by commas
# Each argument will be printed with a space in between by default


#--------------------------------------------------------------------------------------------------------------

# Using string concatenation to join strings  
print("Hello" + " " + "World") # This will print: Hello World 
# String concatenation is done using the + operator and it combines the strings into one
# You need to add spaces manually if required and must convert non-string types to string using str() function


#--------------------------------------------------------------------------------------------------------------

# Using the sep parameter to change the separator 
print("Mango", "Banana", "Apple", sep=",") # This will print: Mango,Banana,Apple
# The sep parameter is used to specify the separator between the arguments in the print function 
# By default, the separator is a space, but you can change it to any string you want


#--------------------------------------------------------------------------------------------------------------

# Using the end parameter to change the end character
name = input("Enter your name: ")  # Taking input from the user
print("Hello", end="")  # This will print: Hello without a newline at the end and will continue on the same line 
print(name) # The name entered by the user will be printed on the same line after "Hello"
# The end parameter is used to specify what to print at the end of the output
# By default, it is a newline character, but you can change it to any string you want


#--------------------------------------------------------------------------------------------------------------

# Using formatted strings (f-strings) for better readability
name = input("Enter your name: ")  # Taking input from the user
age = int(input("Enter your age: "))  # Taking input from the user and converting it to an integer
print(f"Hello {name}, you are {age} years old.")  # This will print: Hello <name>, you are <age> years old.
# f-strings are a way to format strings in Python, allowing you to embed expressions inside string literals
# They are prefixed with 'f' and allow you to include variables directly in the string using curly braces {}
 

#--------------------------------------------------------------------------------------------------------------

# Using the format() method for string formatting
name = input("Enter your name: ")  # Taking input from the user
age = int(input("Enter your age: "))  # Taking input from the user and converting it to an integer
print("Hello {}, you are {} years old ." .format(name, age)) # This will print: Hello <name>, you are <age> years old.
# The format() method is used to format strings in Python
# It allows you to insert variables into a string using curly braces {}


#--------------------------------------------------------------------------------------------------------------

# Using Joining strings with join() method
Name = ["Mango", "Banana", "Apple"]  # List of fruits
fruits = "," .join(name)  # Joining the list of fruits into a single string with a comma as a separator
print(fruits)  # This will print: Mango,Banana,Apple
# The join() method is used to join elements of an iterable (like a list) into a single string
# You can specify the separator string to be used between the elements
# It is commonly used to create a single string from a list of strings


#--------------------------------------------------------------------------------------------------------------
