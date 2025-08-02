# Implement a Python program that prompts the user for a single word (with no spaces).
# Define a function count_vowels_consonants(word) that counts the number of vowels (a, e, i, o, u) and 
# consonants in the word (case-insensitively). You can achieve this without loops by using the .lower() and .count() 
# string methods for each vowel and summing them up. The number of consonants will be the total length of the word minus the number of vowels. 
# The function should return a formatted string, for example: "Vowels: 2, Consonants: 5".

#-------------------------------------------------------------------
def main():
    userInput= input("what word do you want to check: ").lower().strip()
    count_vowels_consonants(userInput)

def count_vowels_consonants(word):
    vowels_count= word.count("a") + word.count("e") +  word.count("i") + word.count("o") + word.count("u")
    consonants_count= len(word) - vowels_count
    print(f"Vowels: {vowels_count}, Consonants: {consonants_count}")


main()