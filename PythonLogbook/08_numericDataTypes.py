# Numbers in python is generrally used to represented useing the int, float, and complex data types.
# Numbric data types are immutable, meaning that once a number is created, it cannot be changed and has verious operations that can be performed on them.

# 1. Integer: Represents whole numbers, both positive and negative.
# Integers can be used for counting, indexing, and performing arithmetic operations.
# Integer values can be positive or negative and can be of any length, limited only by the available memory.
integerNumber = 42  # This is an integer
print("Integer number:", integerNumber)  # Output: Integer number: 42

#----------------------------------------------------------------------------------------------------------------------------------------
# 2. Float: Represents decimal numbers (floating-point numbers).
# Float numbers are used to represent real numbers and can be used in mathematical calculations.
# Foat values can be positive or negative and can have a fractional part.
# Floating point numbers has limits on how long they can be, which is determined by the system's architecture.
floatNumber = 3.14  # This is a float
print("Float number:", floatNumber)  # Output: Float number: 3.14

#----------------------------------------------------------------------------------------------------------------------------------------

# 3. Complex: Represents complex numbers with a real and imaginary part.
# complex numbers are represented using the `j` suffix for the imaginary part.
# complex numbers are used in various fields such as engineering, physics, and mathematics.
complexNumber = 2 + 3j  # This is a complex number (2 is the real part, 3 is the imaginary part)
print("Complex number:", complexNumber)  # Output: Complex number: (2+3j)

#----------------------------------------------------------------------------------------------------------------------------------------
# Type Conversion: Converting between different numeric types can be done using built-in functions.
intNumber = int(floatNumber)  # Convert float to int
print("Converted float to int:", intNumber)  # Output: Converted float to int: 3
floatFromInt = float(integerNumber)  # Convert int to float
print("Converted int to float:", floatFromInt)  # Output: Converted int to float: 42.0

# In python you can also use the `complex()` function to convert a number to a complex number.
complexFromInt = complex(integerNumber)  # Convert int to complex   
print("Converted int to complex:", complexFromInt)  # Output: Converted int to complex: (42+0j)

# In Python, you can convert a number to a string using the `str()` function and vice versa.
# But when converting a string to a number, you need to ensure that the string represents a valid number otherwise it will raise a ValueError. 
strFromInt = str(integerNumber)  # Convert int to string
print("Converted int to string:", strFromInt)  # Output: Converted int to string : '42'


#----------------------------------------------------------------------------------------------------------------------------------------
# Operations on numbers can be performed using verious arithmetic operators such as "+","-","*","/","%","**", and "//".
# Other Various operation can also be ferormed using verious built-in functions such as `abs()`, `round()`, and `pow()`.

# abs(): Returns the absolute value of a number meaning it returns the number without its sign.
absoluteValue = abs(-10)  # This will return 10
print("Absolute value of -10:", absoluteValue)  # Output: Absolute value of -10: 10

# round(): Rounds a floating-point number to the nearest integer or to a specified number of decimal places.
roundedValue = round(floatNumber)  # This will round 3.14 to 3
print("Rounded value of 3.14:", roundedValue)  # Output: Rounded value of 3.14: 3
# we can also specify the number of decimal places to round to, e.g., round(floatNumber, 1) will return 3.1
anotherRoundedValue = round(floatNumber, 1)  # This will round 3.14 to 3.1
print("Rounded value of 3.14 to 1 decimal place:", anotherRoundedValue)  # Output: Rounded value of 3.14 to 1 decimal place: 3.1

# pow(): Raises a number to the power of another number.
powerValue = pow(2, 3)  # This will return 2 raised to the power of 3, which is 8
print("2 raised to the power of 3:", powerValue)  # Output: 2 raised to the power of 3: 8

# min() and max(): Returns the minimum and maximum value from a set of numbers.
minValue = min(1, 2, 3, 4, 5)  # This will return 1
print("Minimum value from 1, 2, 3, 4, 5:", minValue)  # Output: Minimum value from 1, 2, 3, 4, 5: 1
maxValue = max(1, 2, 3, 4, 5)  # This will return 5
print("Maximum value from 1, 2, 3, 4, 5:", maxValue)  # Output: Maximum value from 1, 2, 3, 4, 5: 5

# sum(): Returns the sum of a set of numbers.
sumValue = sum([1, 2, 3, 4, 5])
print("Sum of 1, 2, 3, 4, 5:", sumValue)  # Output: Sum of 1, 2, 3, 4, 5: 15

# divmod(): Returns a tuple containing the quotient and remainder of dividing two numbers.
divmodValue = divmod(10, 3)  # This will return (3, 1) meaning 10 divided by 3 is 3 with a remainder of 1
print("Divmod of 10 and 3:", divmodValue)  # Output: Divmod of 10 and 3: (3, 1)

#----------------------------------------------------------------------------------------------------------------------------------------

# In Python we can also converts numbers into binary, octal, and hexadecimal representations using the built-in functions `bin()`, `oct()`, and `hex()` respectively.

# bin() - Converts an integer to its binary representation.
# bin() function returns a string representation of the binary value prefixed with '0b'.
# The binary representation uses digits 0 and 1 to represent values.
binaryRepresentation = bin(integerNumber)  # Convert integer to binary
print("Binary representation of 42:", binaryRepresentation)  # Output: Binary representation of 42: 0b101010

# oct() - Converts an integer to its octal representation.
# oct() function returns a string representation of the octal value prefixed with '0o'.
# The octal representation uses digits 0-7 to represent values.
octalRepresentation = oct(integerNumber)  # Convert integer to octal
print("Octal representation of 42:", octalRepresentation)  # Output: Octal representation of 42: 0o52

# hex() - Converts an integer to its hexadecimal representation.
# hex() function returns a string representation of the hexadecimal value prefixed with '0x'.
# The hexadecimal representation uses digits 0-9 and letters a-f to represent values.
hexadecimalRepresentation = hex(integerNumber)  # Convert integer to hexadecimal
print("Hexadecimal representation of 42:", hexadecimalRepresentation)  # Output: Hexadecimal representation of 42: 0x2a

#----------------------------------------------------------------------------------------------------------------------------------------
# Number formatting: Formatting numbers for display can be done using formatted string literals (f-strings) or the `format()` method.
formattedNumber = f"The value of pi is approximately {floatNumber:.2f}"  # Format float to 2 decimal places
print(formattedNumber)  # Output: The value of pi is approximately 3.14

# Alternatively, using the format() method
formattedNumberMethod = "The value of pi is approximately {:.2f}".format(floatNumber)
print(formattedNumberMethod)  # Output: The value of pi is approximately 3.14

