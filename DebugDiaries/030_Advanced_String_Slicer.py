#Implement a Python program that prompts the user for a sentence. Define a function create_summary(text) that does the following:
    # First, it removes any leading/trailing whitespace from the text.
    # It then checks the length of the cleaned text. If the length is 20 characters or less, it should return the text unchanged.
    # If the length is greater than 20, it should return a summary string created by concatenating the 
    # first 10 characters of the text and the last 10 characters of the text, separated by "...". For example, 
    # "This is a very long sentence for testing" would become "This is a ...r testing".

#-----------------------------------------------------------------------------------------------------

def main():
    userText= input("Write a string: ")
    create_summary(userText)

def create_summary(text) :
    if len(text) <= 20:
        print("text")
    else:
        summeryText= text[:10]+ "..." + text[-10:]
        print(summeryText)
        

main()
