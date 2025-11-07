# Implement a program that prompts the user for their age (as an integer) and whether they are attending a matinee showing. 
# Define a function get_ticket_price(age, is_matinee) that returns the ticket price (as a float) based on these conditions:
    # Base Price: $10.00
    # Senior Discount: If the age is 65 or older, the price is $7.00.
    # Child Discount: If the age is 12 or younger, the price is $5.00.
    # Matinee Discount: If is_matinee is True, an additional $2.00 discount is applied to the final price, after any age-based discounts.
# Your program should print the final ticket price.
import time

def main():
   
    age= int(input("enter your age : "))
    current_time= int(time.strftime("%H"))

    is_martinee= is_Martinee(current_time)
    ticket_price= price_cal(age,is_martinee)
    display_price(ticket_price, is_martinee)

def is_Martinee(time):
    if time>12:
        return False
    elif time<17:
        return True
    elif 17<time>24:
        return False
    else :
        return "Invalid Input"

def price_cal(age, is_martinee):
    
    if not is_martinee:
        if age > 65:
            return 7.00 
        elif age<=12 :
            return 5.00
        else :
            return 10.00
    else:
        if age > 65:
            return 7.00-2.00 
        elif age<=12:
            return 5.00-2.00
        else:
            return 10.00-2.00
        
def display_price(price, is_martinee):
    if not is_martinee:
        print(f"Your total price is {price}")
    else :
        print(f"Your total Price is {price} with $2.00 discount ")



main()

