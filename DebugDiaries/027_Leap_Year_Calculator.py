# Implement a Python program that prompts the user to enter a year. Define a function is_leap_year(year) 
# that returns True if the year is a leap year and False otherwise. The rules for a leap year are:
    # The year must be divisible by 4.
    # However, if the year is divisible by 100, it is NOT a leap year, unless...
    # The year is also divisible by 400.
    # Your program should print whether the entered year is a leap year or not.

#------------------------------------------------------------------------------------------------

def main():
    year = int(input("Enter a year:"))
    is_leap_year(year)

def is_leap_year(year) :
    if year % 4== 0 :
        if year % 100== 0 :
            if year % 400 == 0 :
                print("entered year is a leap year")
            else :
                print("entered year is not a leap year")
        else : 
            print("entered year is a leap year")
    else :
     print("entered year is not a leap year")

main()
