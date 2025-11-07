# Implement a program that prompts the user for the subtotal of a bill (as a float). 
# Define a function calculate_final_bill(subtotal, tax_rate=0.08, tip_rate=0.15) that calculates and returns the final bill, 
# including an 8% tax and a 15% tip. The tax and tip percentages should be optional function parameters with default values. 
# Your program should print a formatted output showing the subtotal, tax amount, tip amount, and total, all rounded to two decimal places.

#--------------------------------------------------------------

def main():
    subbill= float(input("Whats the bill amount: "))
    tax= input("how much for the tax in percentage: ")
    tip= input("what the total tip ammount in percentage: ")

    calculate_finalbill(subbill,tax, tip)

def calculate_finalbill(subbill, tax=8, tip=15) :
    finalbill= subbill + (tax/100 * subbill) + (tip/100 * subbill)
    print(f" your final bill amount is {finalbill: .2f}")

main()