# Implement a Python program that prompts for a user's weight in kilograms and height in meters. 
# Define a function calculate_bmi(weight, height) that returns the calculated BMI value ​Then, 
# define a second function get_bmi_category(bmi) that takes the BMI value and 
# returns a more detailed category string based on these ranges:
    # Less than 18.5: "Underweight"
    # 18.5 to 24.9: "Normal weight"
    # 25.0 to 29.9: "Overweight"
    # 30.0 or greater: "Obesity"

# Your program should calculate the BMI, format it to one decimal place, and print both the BMI value and its corresponding category.
#-----------------------------------------------------------------------------


def main() :

    weight = float(input("Whats your weight in kilogram: "))
    height = float(input("whats your height in meters: "))
    bmi = calculate_bmi(weight, height)
    get_bmi_category(bmi)

    
def calculate_bmi(weight, height):
    BMI = weight/ pow(height , 2)   
    return BMI


def get_bmi_category(bmi) :
    
    if bmi <18.5 :
        print("Underweight")
    elif bmi <24.5 :
        print("Normal weight")
    elif bmi < 29.9 :
        print("Overweight")
    else :
        print("Obesity")
    

    
main()