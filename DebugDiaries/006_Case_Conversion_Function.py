# Implement a Python function called to_uppercase that takes a string argument and returns the string converted entirely to uppercase. 
# Prompt the user for a word or phrase, pass it to your function, and print the uppercase result.

#-------------------------------------------------------------
def main ():
    userStr=input("What do you have to say?? : ")
    upperCase=to_uppercase(userStr)
    print(f"Here's your string converted entirely to uppercase {upperCase}")


def to_uppercase(strValue):
    return strValue.upper()

main()