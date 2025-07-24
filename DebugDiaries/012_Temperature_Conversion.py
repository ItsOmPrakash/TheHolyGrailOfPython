# Implement a Python program that prompts the user to enter a temperature in Fahrenheit. 
# Define a function convert_f_to_c(fahrenheit) that takes the Fahrenheit temperature (as a float) and returns its equivalent in Celsius. 
# The conversion formula is C=(F−32)∗5/9. 
# Your program should print the original Fahrenheit temperature and its calculated Celsius equivalent, formatted to two decimal places.

#----------------------------------------------------------------
def main():
    temp = float(input ("whats the temperature: "))
    celsius = convert_f_to_c(temp)
    print(f"the original Fahrenheit temperature is {temp:.2f} and its calculated Celsius equivalent is {celsius:.2f}")
    

def convert_f_to_c(fahrenheit) :
    calsius = (fahrenheit - 32) * 5/9
    return calsius

main()
