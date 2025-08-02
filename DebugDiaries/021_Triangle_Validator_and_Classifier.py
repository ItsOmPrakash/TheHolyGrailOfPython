# Implement a Python program that prompts the user for three side lengths of a triangle (as integers or floats). 
# Define a function classify_triangle(a, b, c) that first checks if the given sides can form a valid triangle 
# (the sum of the lengths of any two sides must be greater than the length of the third side). 
# If it's a valid triangle, the function should return its type: "Equilateral" (all three sides are equal), 
# "Isosceles" (exactly two sides are equal), or "Scalene" (no sides are equal). 
# If the sides cannot form a triangle, it should return "Invalid Triangle". 
# Your program should then print the result.

#-----------------------------------------------------------

def main(): 
    firstSide= int (input("whats the length of the first side: "))
    secondSide= int(input("Whats the length of the second side: "))
    thirdSide= int(input("Whats the length of the third side: "))
    if firstSide+secondSide+thirdSide ==180 :
        classify_triangle(firstSide,secondSide,thirdSide)
    else :
        print("Invalid Triangle")


def classify_triangle(a, b, c) :
    if a == b == c :
        print("Equilateral")
    elif a == b or b==c or a==c :
        print("Isosceles")
    else :
        print("Scalene")
    

main()