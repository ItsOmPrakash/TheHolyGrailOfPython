#Implement a program that prompts the user for a numeric value and two strings representing units, 
# for example, 'cm' and 'inch'. Define a function convert_units(value, from_unit, to_unit) that returns the converted value. 
# The function should support conversions between cm and inch (1 inch = 2.54 cm) and kg and lb (1 kg = 2.20462 lb). 
# If the units are not a valid conversion pair, the function should return None. 
# Your program should print the converted value or an error message.

#------------------------------------------------------------------------------------------------------------------


def main():
    units= ["cm","inch","lb","kg"]
    value= float(input("Enter the value: "))
    print("Converstion opetions avilable from these unit only \n-------cm,inch,lb,kg------")
    from_unit= input("enter the unit from you want to convert: ").lower().strip()
    to_unit= input("enter the unit in which you need to convert: ").lower().strip()
    if not units:
        from_unit= input("enter the right unit from you want to convert: ")
    else:
        get_convert(value, from_unit,to_unit)

def get_convert(value, from_unit,to_unit):
    if from_unit == "cm" or from_unit == "inch" : 
        if to_unit == "inch":
            print(f"Converted value is {value*2.54} {to_unit}")
        else: 
            print(f"Converted value is {value/2.54} {to_unit}")
    elif from_unit == "lb" or from_unit == "kg" : 
        if to_unit == "kg":
            print(f"Converted value is {value/2.204} {to_unit}")
        else :
            print(f"Converted value is {value*2.204} {to_unit}")
    else:
        print("Invalid Operations!!!! try again");


        
main()   

        