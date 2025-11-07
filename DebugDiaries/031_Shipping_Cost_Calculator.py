# Implement a program that prompts the user for a package's weight (as a float) and a destination zone (e.g., 'A', 'B', or 'C'). 
# Define a function calculate_shipping(weight, zone) that returns the total shipping cost based on the following rules:
    # Zone 'A': $5 flat fee for weights up to 10kg. Over 10kg, the fee is $5 plus $1.50 for each extra kg.
    # Zone 'B': $7 flat fee for weights up to 10kg. Over 10kg, the fee is $7 plus $2.00 for each extra kg.
    # Zone 'C': $10 flat fee for all weights.
    # If the zone is invalid, return None and print an error.
# Your program should then print the calculated shipping cost or an error message.

#--------------------------------------------------------------------------------------

def main(): 
    weight = float(input("Enter package's weight: "))
    destination_zone = input("Enter the destination zone for the package: ")
    calculated_fee = calculate_shipping(weight,destination_zone)
    
    if calculated_fee is None :
        print("Invlid input")
    else :
        print(f"Shipping cost is going to be {calculated_fee}")
    
def calculate_shipping(weight, zone): 
    if zone =='A' :
        if weight<=10 :
            fee = 5.00
            return fee 
        else :
            fee= 5.00+((weight-10)*1.5)
            return fee 
    elif zone =='B':
        if weight<=10 :
            fee = 7.00
            return fee 
        else :
            fee= 7.00+((weight-10)*2.5)
            return fee 
    elif zone=='C':
        fee = 10.00
        return fee 
    else :
        return None
    


main()
    