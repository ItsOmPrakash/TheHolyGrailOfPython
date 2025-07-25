# Implement a Python program that prompts the user for their age. Define a function get_age_category(age) 
# that returns a string indicating the age category:
    # "Child" (0-12)
    # "Teenager" (13-19)
    # "Adult" (20-64)
    # "Senior" (65 and above)
# Handle invalid ages (negative or unreasonably high, e.g., >120) by returning "Invalid Age". Your program should print the age category.

#-----------------------------------------------------------------------

def main():
   age=int(input("Whats your age: "))
   if age >= 0 and age <=120 :
      get_age_category(age)
   else :
      print("Invalid Age")

def get_age_category(age) :
    match age:
        case age if age <= 12:
          print("Child")
        case age if age <= 19:
          print("Teenager")
        case age if age <= 64:
          print("Adult")
        case age if age <= 120:
          print("Senior")

main()

    

   