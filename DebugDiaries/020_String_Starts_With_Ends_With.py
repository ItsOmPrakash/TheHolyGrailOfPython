# Implement a Python program that prompts the user for a main_word and two single characters: 
# start_char and end_char. Define a function check_word_ends(word, start, end) that returns a string:
    # "Starts and ends correctly" if the main_word starts with start_char AND ends with end_char (case-insensitive).
    # "Starts correctly but not ends" if it only starts correctly.
    # "Ends correctly but not starts" if it only ends correctly.
    # "Neither strts nor ends correctly" otherwise.

# Use appropriate string methods like .lower(), .startswith(), and .endswith(). Your program should print the result.

#------------------------------------------------------------------------

def main():
    main_word= input("which word do you want to check: ").lower().strip()
    start_char= input("what should be the starting character: ").lower()
    end_char= input("what should be the ending character: ").lower()
    check_word_ends(main_word, start_char, end_char)

def check_word_ends(word, start, end) :
    if word.startswith(start) :  
        if word.endswith(end) :
            print("Starts and ends correctly")
        else :
            print("Starts correctly but not ends")
    else :
        if word.endswith(end) :
            print("Ends correctly but not starts")
        else:
            print("Neither strts nor ends correctly")
    
main()

