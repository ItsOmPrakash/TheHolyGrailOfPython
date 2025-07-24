
# Operator in Python  is a symbol that performs an operation on one or more operands.
# Operators can be arithmetic, comparison, logical, assignment, bitwise, identity, or membership    
# Operators are used to manipulate data and variables.
#-------------------------------------------------------------

# Arithmetic Operators - These operators are used to perform mathematical operations like addition, subtraction, multiplication, and division.
# types of arithmetic operators are +, -, *, /, //, %, **
# for example:
a = 10
b = 3
print("Addition:", a + b)        # Output: 13
print("Subtraction:", a - b)     # Output: 7
print("Multiplication:", a * b)  # Output: 30
print("Division:", a / b)        # Output: 3.3333
print("Floor Division:", a // b)  # Output: 3
print("Modulus:", a % b)         # Output: 1
print("Exponentiation:", a ** b)  # Output: 1000

#-------------------------------------------------------------

# # Comparison Operators - These operators are used to compare two values and return a boolean result (True or False).
# types of comparison operators are ==, !=, >, <, >=, <=   
# for example:
x = 5
y = 10
print("Equal:", x == y)          # Output: False
print("Not Equal:", x != y)      # Output: True
print("Greater than:", x > y)     # Output: False
print("Less than:", x < y)        # Output: True
print("Greater than or equal to:", x >= y)  # Output: False
print("Less than or equal to:", x <= y)     # Output: True

#-------------------------------------------------------------

# Logical Operators - These operators are used to combine conditional statements.
# types of logical operators are and, or, not
# for example:
a = True
b = False
print("And:", a and b)  # Output: False
print("Or:", a or b)    # Output: True
print("Not:", not a)     # Output: False

#-------------------------------------------------------------

# Assignment Operators - These operators are used to assign values to variables.
# types of assignment operators are =, +=, -=, *=, /=, //=, %=, **=
# for example:
x = 5
x += 3  # Equivalent to x = x + 3
print("Assignment:", x)  # Output: 8
x -= 2  # Equivalent to x = x - 2
print("Subtraction Assignment:", x)  # Output: 6
x *= 2  # Equivalent to x = x * 2
print("Multiplication Assignment:", x)  # Output: 12
x /= 3  # Equivalent to x = x / 3
print("Division Assignment:", x)  # Output: 4.0
x //= 2  # Equivalent to x = x // 2
print("Floor Division Assignment:", x)  # Output: 2.0
x %= 2  # Equivalent to x = x % 2
print("Modulus Assignment:", x)  # Output: 0.0
x **= 3  # Equivalent to x = x ** 3
print("Exponentiation Assignment:", x)  # Output: 0.0

#-------------------------------------------------------------

# Bitwise Operators - These operators are used to perform bit-level operations on integers.
# types of bitwise operators are &, |, ^, ~, <<, >>
# for example:
a = 5  # Binary: 0101
b = 3  # Binary: 0011
print("Bitwise AND:", a & b)  # Output: 1 (Binary: 0001)
print("Bitwise OR:", a | b)   # Output: 7 (Binary: 0111)
print("Bitwise XOR:", a ^ b)  # Output: 6 (Binary: 0110)
print("Bitwise NOT:", ~a)      # Output: -6 (Binary: 1010 in two's complement)
print("Left Shift:", a << 1)   # Output: 10 (Binary: 1010)
print("Right Shift:", a >> 1)  # Output: 2 (Binary: 0010)

#-------------------------------------------------------------

# Identity Operators - These operators are used to check if two variables point to the same object in memory.
# types of identity operators are is, is not
# for example:
a = [1, 2, 3]
b = a
c = a[:]
print("Is a b?", a is b)        # Output: True (b is the same object as a)
print("Is a c?", a is c)        # Output: False (c is a different object with the same content)
print("Is not a c?", a is not c)  # Output: True (c is a different object)
print("Is not a b?", a is not b)  # Output: False (b is the same object as a)

#-------------------------------------------------------------

# Membership Operators - These operators are used to check if a value is present in a sequence (like a list, tuple, or string).
# types of membership operators are in, not in
# for example:
a = [1, 2, 3, 4, 5]
print("Is 3 in a?", 3 in a)        # Output: True
print("Is 6 in a?", 6 in a)        # Output: False
print("Is 3 not in a?", 3 not in a)  # Output: False
print("Is 6 not in a?", 6 not in a)  # Output: True

#-------------------------------------------------------------

# Operators Precedence - Operators have a defined order of precedence, which determines the order in which operations are performed.
# For example, multiplication and division have higher precedence than addition and subtraction.    
# The order of precedence is as follows (from highest to lowest):
# 1. Parentheses ()
# 2. Exponentiation **
# 3. Unary plus and minus +, -
# 4. Multiplication *, Division /, Floor Division //, Modulus %
# 5. Addition +, Subtraction -
# 6. Bitwise Shift <<, >>
# 7. Bitwise AND &
# 8. Bitwise XOR ^
# 9. Bitwise OR |
# 10. Comparison operators <, <=, >, >=, ==, !=
# 11. Identity operators is, is not
# 12. Membership operators in, not in
# 13. Logical NOT not
# 14. Logical AND and
# 15. Logical OR or

# For example:
x = 10
y = 5
z = 2
result = x + y * z  # Multiplication has higher precedence than addition
print("Result:", result)  # Output: 20 (5 * 2 = 10, then 10 + 10 = 20)
# To change the order of operations, you can use parentheses:
result = (x + y) * z  # Parentheses change the order of operations 
print("Result with parentheses:", result)  # Output: 30 ((10 + 5) * 2 = 30)

#-------------------------------------------------------------
