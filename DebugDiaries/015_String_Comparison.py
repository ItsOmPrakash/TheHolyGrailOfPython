# Implement a Python program that prompts the user for two words. Define a function are_words_same(word1, word2) 
# that returns True if the two words are identical, ignoring their case (e.g., "Python" and "python" should be considered the same). 
# Otherwise, it should return False. Use appropriate string methods to achieve case-insensitivity. 
# Your program should print "The words are the same (case-insensitive)." or "The words are different."

#----------------------------------------------------------------------------------

def main ():
    word1 = input("Whats your first word: ").lower().strip()
    word2 = input("Whats your second word: ").lower().strip()
    value= are_words_same(word1, word2)
    if value == True :
        print("The words are the same")
    else :
        print("The words are different.")

def are_words_same(word1, word2):
    if word1 == word2 :
       return True
    else :
       return False

main()
