# Implement a Python program that simulates a basic ATM. Define a function perform_transaction(balance, action, amount) 
# where balance is the current account balance, action is a string ('withdraw' or 'deposit'), 
# and amount is the transaction amount. The function should return the new balance after the transaction. 
# Add the following validation:
    # For a 'withdraw' action, check if the amount is positive and if it does not exceed the balance. 
    # If either check fails, return the original balance and print an error message (e.g., "Insufficient funds" or "Invalid amount").
    # For a 'deposit' action, check if the amount is positive. 
    # If not, return the original balance and print an error message.
# Your main program should start with a balance of 1000, prompt the user for an action and amount, call the function,
# and print the new balance.

#-------------------------------------------------------------------------





def main(): 
    balance = 1000
    action= input("What do you want to perform: ").strip().lower()
    amount= int(input("whats the amount: "))
    if action =="withdraw" or action =="deposit" :
        perform_transaction(balance, action , amount)
    else :
        print("Transaction failed")


def perform_transaction(balance, action, amount):
    if action =="withdraw" and balance > 0:
        if balance > amount :
            balance = balance - amount 
            print(f"New Balance is: {balance}")
        else :
            print("Insufficient funds")
    else :
        balance = balance + amount
        print(f"New Balance is {balance}")


main()


