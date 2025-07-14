
# Variable are the containers for storing data values. 
# Variables are created when you assign a value to them.
# In Python, variables do not need to be declared with a specific type,
# They are dynamically typed.
# Variable names can contain letters, numbers, and underscores, but cannot start with a number.
# Variable names are case-sensitive, meaning that 'myVariable' and 'myvariable' are different variables.
# Variable names should be descriptive and meaningful to improve code readability.
# Variable names should not be the same as Python keywords or built-in functions.

#-------------------------------------------------------------------------------------------------------------------------------

# Example of variable declaration and assignment
intVeriable = 27
floatVariable = 3.14
stringVariable = "Hello, World!"    
boolVariable = True 
listVariable = [1, 2, 3, 4, 5]
tupleVariable = (1, 2, 3)  
dictVariable = {"name": "Alice", "age": 30, "city": "New York"} 
setVariable = {1, 2, 3, 4, 5}  # A set is an unordered collection of unique elements
# None is a special constant in Python that represents the absence of a value or a null value
noneVariable = None


#-------------------------------------------------------------------------------------------------------------------------------

# Printing the variables
print("Integer Variable:", intVeriable)  # Output: Integer Variable: 27
print("Float Variable:", floatVariable)  # Output: Float Variable: 3.14     
print("String Variable:", stringVariable)  # Output: String Variable: Hello, World!
print("Boolean Variable:", boolVariable)  # Output: Boolean Variable: True
print("List Variable:", listVariable)  # Output: List Variable: [1, 2, 3, 4, 5]
print("Tuple Variable:", tupleVariable)  # Output: Tuple Variable: (1, 2, 3)
print("Dictionary Variable:", dictVariable)  # Output: Dictionary Variable: {'name': 'Alice', 'age': 30, 'city': 'New York'}
print("Set Variable:", setVariable)  # Output: Set Variable: {1, 2, 3, 4, 5}
print("None Variable:", noneVariable)  # Output: None Variable: None


#-------------------------------------------------------------------------------------------------------------------------------


# Checking the types of the variables   
print("Type of Integer Variable:", type(intVeriable))  # Output: Type of Integer Variable: <class 'int'>
print("Type of Float Variable:", type(floatVariable))  # Output: Type of Float Variable: <class 'float'>
print("Type of String Variable:", type(stringVariable))  # Output: Type of String Variable: <class 'str'>
print("Type of Boolean Variable:", type(boolVariable))  # Output: Type of Boolean Variable: <class 'bool'>
print("Type of List Variable:", type(listVariable))  # Output: Type of List Variable: <class 'list'>
print("Type of Tuple Variable:", type(tupleVariable))  # Output: Type of Tuple Variable: <class 'tuple'>
print("Type of Dictionary Variable:", type(dictVariable))  # Output: Type of Dictionary Variable: <class 'dict'>
print("Type of Set Variable:", type(setVariable))  # Output: Type of Set Variable: <class 'set'>
print("Type of None Variable:", type(noneVariable))  # Output: Type of None Variable: <class 'NoneType'>


#-------------------------------------------------------------------------------------------------------------------------------

# Variable names can be changed by reassigning a new value to them
intVeriable = 42  # Reassigning a new value to the integer variable
print("Updated Integer Variable:", intVeriable)  # Output: Updated Integer Variable: 42

#-------------------------------------------------------------------------------------------------------------------------------


# Variable names can also be used in expressions
sumVariable = intVeriable + floatVariable  # Adding an integer and a float
print("Sum of Integer and Float Variable:", sumVariable)  # Output: Sum of Integer and Float Variable: 45.14

#-------------------------------------------------------------------------------------------------------------------------------

# Rules for variable names:
# 1. Variable names must start with a letter (a-z, A-Z) or an underscore (_).
# 2. Variable names can contain letters, numbers (0-9), and underscores (_).
# 3. Variable names cannot start with a number.     
# 4. Variable names are case-sensitive (e.g., myVariable and myvariable are different).
# 5. Variable names cannot be the same as Python keywords (e.g., if, else, for, while, etc.).
# 6. Variable names should be descriptive and meaningful to improve code readability.   
# 7. Variable names should not contain spaces or special characters (e.g., @, #, $, %, etc.).
# 8. Variable names should not be too long or too short; they should be concise yet descriptive.
# 9. Variable names should not use reserved words or built-in function names (e.g., print, input, str, int, etc.).
# 10. Variable names should be consistent with the naming conventions used in the codebase (e.g., camelCase, snake_case, etc.).


#-------------------------------------------------------------------------------------------------------------------------------

# Examples of Naming Conventions:
# 1. Camel Case: 
myVariableName = "Hello"  # First letter of each word is capitalized except the first word
# 2. Snake Case:
my_variable_name = "World"  # Words are separated by underscores
# 3. Pascal Case:
MyVariableName = "Python"  # First letter of each word is capitalized   
# 4. Kebab Case:
my-variable-name = "Programming"  # Words are separated by hyphens (not recommended for variable names in Python)
# 5. Upper Case:
MY_VARIABLE_NAME = "Constants"  # All letters are capitalized, often used for constants
# 6. Lower Case:
myvariablename = "lowercase"  # All letters are lowercase, often used for variables
# 7. Mixed Case:
myVariableName123 = "MixedCase"  # Combination of letters and numbers, often used for variables 
# 8. Underscore Prefix:
_myVariableName = "Private"  # Underscore prefix indicates that the variable is intended for internal use
# 9. Underscore Suffix:     
myVariableName_ = "Temporary"  # Underscore suffix indicates that the variable is temporary or for a specific purpose
# 10. Double Underscore Prefix:
__myVariableName = "Special"  # Double underscore prefix indicates that the variable is intended for special use or is a private variable


#-------------------------------------------------------------------------------------------------------------------------------
    