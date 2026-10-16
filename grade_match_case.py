# Get user grade
letter_grade = input("Enter your letter grade: ")

letter_grade = letter_grade.upper() # making use of a method/function of the str class

match letter_grade:
    case "A":
        gpa = 4.0
    case "B":
        gpa = 3.3
    case "C":
        gpa = 2.5
    case "D":
        gpa = 2.0
    case "F":
        gpa = 1.0
    case _:
        print("Could not determine gpa")
        gpa = 0.0

print(f"Your GPA is: {gpa}")

# Note: case can check for multiple values by using the "or" operator which is the | symbol

