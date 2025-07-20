# Implement a program in Python that prompts the user for mass as an integer (in kilograms) and 
# then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.

#--------------------------------------------------------

# taking user input for mass
mass = int(input("What should be the mass ?? "))
# assigning variable  "c" = speed of light
c = 300000000
# applying the formula
Energy = mass*pow(c , 2)
#printing the value
print(f"Value of Energy {Energy}")


