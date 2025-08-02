#Implement a Python program for a single round of Rock, Paper, Scissors. 
# Prompt the user for their choice (rock, paper, or scissors). For this exercise, hardcode the computer's choice to be paper. 
# Define a function determine_winner(player_choice, computer_choice) that takes both choices as arguments 
# (after converting the player's choice to lowercase). 
# The function should return one of three strings: "Player wins!", "Computer wins!", or "It's a tie!". 
# Your program should then print the result.

def main():
    computersChoice = "paper "
    usersChoice = input("Whats your choice (rock, paper, or scissors): ").strip().lower()
    determine_winner(usersChoice)
    
def determine_winner(player_choice) :
    if player_choice == "rock" :
        print("Computer wins!")
    elif player_choice == "paper" :
        print("It's a tie!")
    else :
        print("Player wins!")

main()