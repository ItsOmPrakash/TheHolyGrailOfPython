# Implement a Python program that prompts the user for a student's score (an integer between 0 and 100). 
# Define a function assign_grade(score) that uses if-elif-else statements to return a letter grade based on these rules:
    # 90-100: 'A'
    # 80-89: 'B'
    # 70-79: 'C'
    # 60-69: 'D'
    # Below 60: 'F'
# Your program should print the assigned grade for the entered score.

#------------------------------------------------------------------------
def main():
    student_score= int(input ("Whats student's score: "))
    if student_score <= 100 :
        assign_grade(student_score)
    else :
        print("Enter a valid score !!")


def assign_grade(score):
    if score >=90 :
        print("A")
    elif score >=80 :
        print("B")
    elif score >=70 :
        print("C")
    elif score >= 60:
        print("D")
    else :
        print("F")
     

main()