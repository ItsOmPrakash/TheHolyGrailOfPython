# Implement a Python function named calculate_discount that takes two arguments: 
# price (a float) and discount_percentage (a float, e.g., 0.10 for 10%). 
# The function should return the final price after applying the discount. In your program, 
# prompt the user for an original price and a discount percentage, call the function, and print the final discounted price.

#-------------------------------------------------------------
def main() :
    price= float(input("Enter the product price: "))
    discount_percentage= float(input ("Enter the product discount: "))
    totalDiscount = calculate_discount(price, discount_percentage )
    discountedPrice = price - totalDiscount
    print(f"The final discounted price is {discountedPrice}")

    
def calculate_discount(price,discount_percentage) :
    return price * discount_percentage


main()