# Functions in Python are defined as reusable blocks of organized code designed to perform a specific task.
# They promote code reusability, improve modularity, and enhance readability within an application.
# Functions can take inputs (arguments) and return outputs (return values).
# function can be defined using the `def` keyword followed by the function name and parentheses.
# while Defining functions, always follow the indentation rules in Python to ensure the code block is recognized as part of the function.

#----------------------------------------------------------------------------------------------------------


def hello():
    print("Hello, World!")  # This function prints a greeting message
# Calling the function to execute its code
hello()

#----------------------------------------------------------------------------------------------------------


# Functions can also accept parameters to perform operations based on the input provided.
def helloAgain(name):
    print(f"Hello, {name}!")  # This function prints a personalized greeting message
# Calling the function with an argument
helloAgain("Alice")  # Output: Hello, Alice!   

#----------------------------------------------------------------------------------------------------------

# Functions can be called within other functions, allowing for nested functionality
def main():
    name= input("Enter your name: ")  # Prompting user for input
    hello_with_name(name)  # Calling another function with the input


# Agrument names can be different in the function definition and the call, as long as the order is maintained.
def hello_with_name(to): # instead of `name`, we use `to` as the parameter name
    print(f"Hello, {to}!")  # This function prints a personalized greeting message
# Calling the main function to start the program
main()  # Output: Hello, [user's name]!
# main() is called at the bottom of the file because it is a common practice to define functions first and call them later.
# if we call main() before defining other called functions, it will result in an error because those functions are not defined yet.


#----------------------------------------------------------------------------------------------------------

# Functions can return values using the `return` statement, allowing the result to be used later in the code.
def add(a, b):
    return a + b  # This function returns the sum of two numbers
# Calling the function and storing the result in a variable
result = add(5, 3)  # Output: 8
print(f"The sum of 5 and 3 is: {result}")  # Output: The sum of 5 and 3 is: 8


#----------------------------------------------------------------------------------------------------------

# Functions can also have default parameter values, which are used if no argument is provided during the function call.
def greet(name="Guest"):
    print(f"Hello, {name}!")  # This function prints a greeting message with a default name
# Calling the function without an argument, using the default value
greet()  # Output: Hello, Guest!
# Calling the function with an argument, overriding the default value
greet("Bob")  # Output: Hello, Bob!

#----------------------------------------------------------------------------------------------------------
