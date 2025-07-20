# Implement a program in Python that prompts the user for input and then outputs that same input in lowercase. 
# Punctuation and whitespace should be outputted unchanged

#--------------------------------------------------------

#taking user input
inputVar = input("Type your input: ")
# removing whitespace and in lower case
outputVar = inputVar.strip().lower()
# printing the output using the print function
print (f" Here's your modified output : {outputVar}")
