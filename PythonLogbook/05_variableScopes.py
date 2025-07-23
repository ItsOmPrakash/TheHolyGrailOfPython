# Variable scopes refer to the visibility and lifetime of variables in different parts of a program.
# In Python, there are four types of variable scopes: local, enclosing, global, and built-in.
# Variable scopes determine where a variable can be accessed and how long it exists in memory.
# Understanding variable scopes is crucial for writing clean and efficient code.
# Variable scopes in Python can be categorized into four main types:

#-----------------------------------------------------------------------------------------------------------------------------

# 1. Local Scope: Variables defined inside a function are in the local scope of that function.
#    They can only be accessed within that function and are destroyed when the function exits.
#    Local variables are created when the function is called and destroyed when the function exits.
#    They are not accessible outside the function.  
def localScopeExample():
    localVar = "I am a local variable"
    print(localVar)  # This will print: I am a local variable
localScopeExample()  # Calling the function to see the local variable in action

# By default, variables defined inside a function are local to that function.
# If you try to access `localVar` outside of `localScopeExample`, it will raise a NameError.    
# print(localVar)  # Uncommenting this line will raise a NameError: name 'localVar' is not defined


#-----------------------------------------------------------------------------------------------------------------------------

# 2. Enclosing Scope: Variables defined in the enclosing function (if any) can be accessed by nested functions.
#    This is also known as a nonlocal scope.
#    Enclosing variables are those that are defined in the outer function but not in the local function.
#    They can be accessed by nested functions, but they are not local to the nested function
#    They are created when the outer function is called and destroyed when the outer function exits.      
def enclosingScopeExample():
    enclosingVar = "I am an enclosing variable"
    
    def nestedFunction():
        print(enclosingVar)  # This will print: I am an enclosing variable
    nestedFunction()  # Calling the nested function to see the enclosing variable in action

# by default, variables defined in the enclosing function are not local to the nested function.
# If you try to access `enclosingVar` outside of `enclosingScopeExample`,it will raise a NameError.
# print(enclosingVar)  # Uncommenting this line will raise a NameError: name 'enclosingVar' is not defined

# If we want to modify the enclosing variable inside the nested function, we can use the `nonlocal` keyword.
def enclosingScopeModificationExample():
    enclosingVar = "I am an enclosing variable"
    
    def nestedFunction():
        nonlocal enclosingVar  # This allows us to modify the enclosing variable
        enclosingVar = "I have been modified"
        print(enclosingVar)  # This will print: I have been modified
    nestedFunction()  # Calling the nested function to see the modification in action
enclosingScopeModificationExample()  # Calling the function to see the enclosing variable modification
# The `nonlocal` keyword allows us to modify the variable from the enclosing scope.
# Note: The `nonlocal` keyword is used to indicate that we want to work with the variable from the enclosing scope,
#       not create a new local variable with the same name.


#-----------------------------------------------------------------------------------------------------------------------------

# 3. Global Scope: Variables defined at the top level of a script or module are in the global scope.
#    They can be accessed from any function within the same module or script.   
globalVar = "I am a global variable"  # This is a global variable
def globalScopeExample():
    print(globalVar)  # This will print: I am a global variable
globalScopeExample()  # Calling the function to see the global variable in action


# If you want to modify a global variable inside a function, you need to use the `global` keyword.
def globalScopeModificationExample():  
    global globalVar  # This allows us to modify the global variable
    globalVar = "I have been modified globally"
    print(globalVar)  # This will print: I have been modified globally
globalScopeModificationExample()  # Calling the function to see the global variable modification
# The `global` keyword allows us to modify the variable from the global scope.
# Note: Global variables should be used sparingly, as they can lead to code that is difficult to understand and maintain.


#-----------------------------------------------------------------------------------------------------------------------------

# 4. Built-in Scope: These are the names that are pre-defined in Python, such as `print()`, `len()`, etc.
#    They are always available in any Python program and can be accessed from anywhere.
#    Built-in variables are those that are defined by Python itself and are always available.
import builtins  # Importing the builtins module to access built-in variables
def builtInScopeExample():
    print(builtins.print)  # This will print: <built-in function print>
    print(builtins.len)    # This will print: <built-in function len>
builtInScopeExample()  # Calling the function to see the built-in variables in action
# Built-in variables are always available in Python and can be accessed from anywhere.  


