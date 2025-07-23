# In python, Data Types are used to define the type of data that a variable can hold.
# python supports various data types, including integers, floats, strings, lists, tuples, sets, and dictionaries.
# Data types are important because they determine the operations that can be performed on the data. 

#-----------------------------------------------------------------------------------------------------------------------------

# 1. Numeric types: Numeric types are used to represent numbers in Python.
#    There are three numeric types in Python: int, float, and complex.

#   - int: Represents integers, which are whole numbers without a decimal point.
intVariable = 10
#   - float: Represents floating-point numbers, which are numbers with a decimal point.     
floatVariable = 10.5
#   - complex: Represents complex numbers, which are numbers with a real and imaginary part.
complexVariable = 10 + 2j


#-------------------------------------------------------------------------------------------------------------------------------

# 2. Text type: These type used to represent text in Python. 
# There is one text type in Python:
#   - str: Represents strings, which are sequences of characters enclosed in single or double quotes.
stringVariable = "Hello, World!"


#-------------------------------------------------------------------------------------------------------------------------------

# 3. Sequence types: Sequence types are used to represent ordered collections of items.
#    There are three sequence types in Python: list, tuple, and range.  

#   - list: Represents a mutable ordered collection of items, which can be of different data types.
listVariable = [1, 2, 3, "four", 5.0 ]  # A list can contain mixed data types.
#   - tuple: Represents an immutable ordered collection of items, which can also be of different data types.
tupleVariable = (1, 2, 3, "four", 5.0)  # A tuple can also contain mixed data types.
#   - range: Represents a sequence of numbers, commonly used in loops.  
rangeVariable = range(1, 10)  # A range object representing numbers from 1 to 9

#-------------------------------------------------------------------------------------------------------------------------------

# 4. Mapping type: Mapping types are used to represent key-value pairs.
#    There is one mapping type in Python:   
#   - dict: Represents a mutable collection of key-value pairs, where each key is unique.
dictVariable = {"name": "Alice", "age": 30, "city": "New York"}  # A dictionary with string keys and mixed value types

#-------------------------------------------------------------------------------------------------------------------------------

# 5. Set types: Set types are used to represent unordered collections of unique items.
#    There are two set types in Python: set and frozenset.  
#   - set: Represents a mutable unordered collection of unique items it means it can be modified after creation.
setVariable = {1, 2, 3, 4, 5}
#   - frozenset: Represents an immutable unordered collection of unique items meaning it cannot be modified after creation.
frozensetVariable = frozenset([1, 2, 3, 4, 5])

#-------------------------------------------------------------------------------------------------------------------------------

# 6. Boolean type: The boolean type is used to represent truth values.
#    There is one boolean type in Python:
#   - bool: Represents two values: True and False.
boolVariable = True  # A boolean variable can be either True or False
# Boolean variables are often used in conditional statements and loops to control the flow of the program.

#-------------------------------------------------------------------------------------------------------------------------------

# 7. None type: The None type is used to represent the absence of a value or a null value.
#    There is one None type in Python: 
#   - NoneType: Represents the absence of a value, often used to indicate that a variable has no value assigned.
noneVariable = None  # A variable with no value assigned is of NoneType
# None is often used as a default value for function arguments or to indicate that a variable has not been initialized.

#-------------------------------------------------------------------------------------------------------------------------------

# 8. Binary types: Binary types are used to represent binary data.
#    There are two binary types in Python:  
#   - bytes: Represents an immutable sequence of bytes, often used for binary data.
bytesVariable = b"Hello, World!"  # A bytes object representing binary data
#   - bytearray: Represents a mutable sequence of bytes, allowing modification of binary data.  
bytearrayVariable = bytearray(b"Hello, World!")  # A bytearray object representing mutable binary data
#   - memoryview: Represents a view of a memory buffer, allowing access to the underlying binary data without copying it.
memoryviewVariable = memoryview(bytesVariable)  # A memoryview object representing a view of the bytes object 
# meaning it allows access to the underlying binary data without copying it.

#-------------------------------------------------------------------------------------------------------------------------------
