# Conditional Statements in Python is used to control the flow of execution based on certain conditions.
# They allow the program to execute different blocks of code based on whether a condition is true or false.
# Conditional statements allow the program to execute certain blocks of code only when specific conditions are met.
# In Python, the main types of conditional statements are if, if-else, and if-elif-else.

#--------------------------------------------------------------

# If statement - Executes a block of code if the condition is true.
# For example:
x = 10
if x > 5:
    print("x is greater than 5")  # Output: x is greater than 5

#--------------------------------------------------------------

# If-Else statement - Executes one block of code if the condition is true, and another block if it is false.
# For example:
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")
# Output: x is not greater than 5

#--------------------------------------------------------------

# If-Elif-Else statement - Checks multiple conditions in sequence.
# For example:
x = 7
if x > 10:
    print("x is greater than 10")
elif x > 5:
    print("x is greater than 5 but less than or equal to 10")   
else:
    print("x is 5 or less") 
# Output: x is greater than 5 but less than or equal to 10

#--------------------------------------------------------------
# Nested If statement - An if statement inside another if statement.
# This allows for more complex conditions to be checked.
# It can be used to check multiple conditions in a hierarchical manner.

# For example:
x = 10
if x > 5:
    print("x is greater than 5")
    if x < 15:
        print("x is also less than 15")
# Output: x is greater than 5
# x is also less than 15

#--------------------------------------------------------------

# Using iF statements instead of a elif and else can lead to more complex code, but it can also be useful in certain situations.
# For example:
x = 10
if x > 5:
  print("x is greater than 5")
if x < 15:
 print("x is less than 15")
# Output:
# x is greater than 5
# x is less than 15
# In this case, both conditions are checked independently, and both messages are printed if both conditions are true. 

#---------------------------------------------------------------

# matching multiple conditions with if statements can be done using logical operators like and, or, and not.
# For example:
x = 10
if x > 5 and x < 15:
    print("x is between 5 and 15")  # Output: x is between 5 and 15
# You can also use or to check if at least one condition is true:
if x < 5 or x > 15:
    print("x is either less than 5 or greater than 15")  # This will not print since x is 10
# You can use not to negate a condition:
if not (x < 5):
    print("x is not less than 5")  # Output: x is not less than 5

#--------------------------------------------------------------

# Match keyword - Introduced in Python 3.10, the match statement allows for pattern matching, similar to switch-case statements in other languages.
# It can be used to match values against patterns and execute code based on the match.  
# For example:
def match_example(value):
    match value:
        case 1:
            return "Value is 1"
        case 2:
            return "Value is 2"
        case _:
            return "Value is something else"
# Example usage:
print(match_example(1))  # Output: Value is 1
# in this example, the match statement checks the value and executes the corresponding case block.
# The match statement is useful for more complex data structures and can simplify code that would otherwise require multiple if-elif statements.

#--------------------------------------------------------------

