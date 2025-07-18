
# Python provides a rich set of built-in functions and methods for manipulating strings
# and performing various operations on them. Here are some common string operations:

# 1. String Concatenation: Joining two or more strings together using the `+` operator.
str1 = "Hello"
str2 = "World"
concatenatedString = str1 + " " + str2  # This will result in "Hello World"
print(concatenatedString)  # Output: Hello World

#----------------------------------------------------------------------------------------------------------------------------------------

# 2. String Repetition: Repeating a string multiple times using the `*` operator.
repeatedString = str1 * 3  # This will result in "HelloHelloHello
print(repeatedString)  # Output: HelloHelloHello

#----------------------------------------------------------------------------------------------------------------------------------------

# 3. String Length: Getting the length of a string using the `len()` function.
lengthOfString = len(concatenatedString)  # This will return the length of
print("Length of concatenated string:", lengthOfString)  # Output: Length of concatenated string: 11

#----------------------------------------------------------------------------------------------------------------------------------------

# 4. String Indexing: Accessing individual characters in a string using indexing.
firstCharacter = concatenatedString[0]  # This will return 'H'
print("First character of concatenated string:", firstCharacter)  # Output: First character of concatenated string: H
# Note: Indexing starts at 0 in Python, so the first character is at index 0.
# Negative indexing can also be used to access characters from the end of the string.
lastCharacter = concatenatedString[-1]  # This will return 'd'
print("Last character of concatenated string:", lastCharacter)  # Output: Last character of concatenated string: d

#----------------------------------------------------------------------------------------------------------------------------------------


# 5. String Slicing: Extracting a substring from a string using slicing.
substring = concatenatedString[0:5]  # This will return "Hello" 
print("Substring of concatenated string:", substring)  # Output: Substring of concatenated string: Hello
# Slicing can also be done with a step value, e.g., concatenatedString[0:11:2] will return "Hlo ol"
# Note: Slicing allows you to specify a start index, an end index, and an optional step value.
print("Last character of concatenated string:", lastCharacter)  # Output: Last character of concatenated string: d
# Negative indexing can also be used to access characters from the end of the string.
# Slicing can also be done with a step value, e.g., concatenatedString[0:11:2] will return "Hlo ol"
# Note: Slicing allows you to specify a start index, an end index, and an optional step value.
print("Last character of concatenated string:", lastCharacter)  # Output: Last character of concatenated string: d
# Negative indexing can also be used to access characters from the end of the string.

#----------------------------------------------------------------------------------------------------------------------------------------

# 6. String Methods: Python provides various built-in methods for strings, such as:

#    - `upper()`: Converts a string to uppercase.
uppercaseString = concatenatedString.upper()  # This will result in "HELLO WORLD"print("Uppercase string:", uppercaseString)  # Output: Uppercase string: HELLO WORLD


#    - `lower()`: Converts a string to lowercase.
lowercaseString = concatenatedString.lower()  # This will result in "hello world"
print("Lowercase string:", lowercaseString)  # Output: Lowercase string: hello world


#    - `strip()`: Removes leading and trailing whitespace from a string.
strWithSpaces = "   Hello World   "
strippedString = strWithSpaces.strip()  # This will result in "Hello World"
print("Stripped string:", strippedString)  # Output: Stripped string: Hello World

#    - `replace()`: Replaces a substring with another substring.
replacedString = concatenatedString.replace("World", "Python")  # This will result in "Hello Python"
print("Replaced string:", replacedString)  # Output: Replaced string: Hello Python

#    - `split()`: Splits a string into a list of substrings based on a delimiter.
splitString = concatenatedString.split(" ")  # This will result in ['Hello', 'World']
print("Split string:", splitString)  # Output: Split string: ['Hello', 'World']

#    - `join()`: Joins a list of strings into a single string with a specified delimiter.
joinedString = ", ".join(splitString)  # This will result in "Hello, World"
print("Joined string:", joinedString)  # Output: Joined string: Hello, World

#    - `find()`: Returns the index of the first occurrence of a substring in a string.
indexOfWorld = concatenatedString.find("World")  # This will return 6
print("Index of 'World' in concatenated string:", indexOfWorld)  # Output: Index of 'World' in concatenated string: 6

#    - `count()`: Returns the number of occurrences of a substring in a string.
countOfO = concatenatedString.count("o")  # This will return 2
print("Count of 'o' in concatenated string:", countOfO)  # Output
# Output: Count of 'o' in concatenated string: 2

#    - `startswith()`: Checks if a string starts with a specified substring.
startsWithHello = concatenatedString.startswith("Hello")  # This will return True
print("Does concatenated string start with 'Hello'? :", startsWithHello)  # Output: Does concatenated string start with 'Hello'? : True

#    - `endswith()`: Checks if a string ends with a specified substring.    
endswithWorld = concatenatedString.endswith("world") # This will return False
print("Does concatenated string end with 'World'? :", endswithWorld)  # Output: Does concatenated string end with 'World'? : False

#   - `capitalize()`: Capitalizes the first character of a string.
capitalizedString = concatenatedString.capitalize()  # This will result in "Hello world"
print("Capitalized string:", capitalizedString)  # Output: Capitalized string: Hello

#   - `title()`: Converts the first character of each word to uppercase.
titleString = concatenatedString.title()  # This will result in "Hello World"   
print("Title case string:", titleString)  # Output: Title case string: Hello World




