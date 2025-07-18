# Assigning values to variables 
# python is dynamically typed language it means you dont needd to specially add data type to the variable
intVariable = 10
nameString = "om"


#----------------------------------------------------------------------------------------------------------------------------------------


# Printing the variables
print("Integer Variable:", intVariable)  # Output: Integer Variable: 10
# print function is used to print the value of the variable
# The print function can take multiple arguments and print them in a single line

#----------------------------------------------------------------------------------------------------------------------------------------


# Mutablility  - The ability to change the value of a variable after it has been created.
# In Python, variables are mutable by default, meaning you can change their values after they have been created.
# For example, you can change the value of intVariable to 20
intVariable = 20
print("Updated Integer Variable:", intVariable)  # Output: Updated Integer Variable: 20
# Mutablity is important because it allows you to modify the value of a variable without creating a new variable.
# But the exception is that some data types are immutable, meaning their values cannot be changed after creation.
# For example, strings are immutable in Python, meaning you cannot change the value of a string after it has been created.


#----------------------------------------------------------------------------------------------------------------------------------------

# casting - The process of converting a variable from one data type to another.
# For example, you can convert an integer to a string using the str() function.
strVariable = str(intVariable)  # Converting integer to string
print("String Variable:", strVariable)  # Output: String Variable: 20
# You can also convert a string to an integer using the int() function.
intVariableFromString = int(strVariable)  # Converting string to integer
print("Integer Variable from String:", intVariableFromString)  # Output: Integer Variable from String: 20
# if the string cannot be converted to an integer, it will raise a ValueError.
# Casting is useful when you need to perform operations on variables of different data types.


#----------------------------------------------------------------------------------------------------------------------------------------

# getting the type of a variable
print("Type of intVariable:", type(intVariable))  # Output: Type of intVariable: <class 'int'>
print("Type of nameString:", type(nameString))  # Output: Type of nameString
# type function is used to get the data type of a variable.

#----------------------------------------------------------------------------------------------------------------------------------------

# Python allows you to assign multiple values to multiple variables in a single line.
# This is known as tuple unpacking or multiple assignment.  
a, b, c = 1, 2, 3
print("Values of a, b, c:", a, b, c)  # Output
# Values of a, b, c: 1 2 3
# You can also assign the same value to multiple variables in a single line.
x = y = z = 10
print("Values of x, y, z:", x, y, z)  # Output: Values of x, y, z: 10 10 10 
# This is useful when you want to initialize multiple variables with the same value.    
# Unpacking is a powerful feature in Python that allows you to work with multiple variables efficiently.
# Unpacking a Collection (like a list or tuple) into multiple variables is also possible.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits  # Unpacking the list into variables
print("Fruits:", x, y, z)  # Output: Fruits: apple banana cherry
# Unpacking is useful when you want to extract values from a collection and assign them to individual variables.


#----------------------------------------------------------------------------------------------------------------------------------------

