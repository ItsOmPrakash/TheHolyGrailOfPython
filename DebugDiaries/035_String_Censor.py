#Implement a program that prompts the user for a sentence and a single "bad word" to be censored. 
# Define a function censor_text(sentence, bad_word) that returns a new string 
# where every occurrence of the bad_word is replaced with asterisks (*) of the same length. 
# The check should be case-insensitive. For example, censor_text("The bad words are bad.", "bad") should return "The *** words are ***.". 
# Your program should print the censored sentence.


#--------------------------------------------------------------------------------------------

def main () :
    user_input= input("Enter a sentence: ").lower().strip()
    bad_word= input("Enter the Bad word: ").lower().strip()
    sentence=censor_text(user_input, bad_word)
    print(sentence)

def numofstar(bad_word):
    length = len(bad_word)
    return "*" * length

def censor_text(user_input, bad_word):
    star= numofstar(bad_word)
    censored_text=user_input.replace(bad_word,star)
    return censored_text

main()


