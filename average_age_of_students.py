# average_age_of_students.py

print("Average age of students calculator")

total_age = 0
student_count = 0
average_age = 0

while True:
    age = input("Enter the age of a student or 'stop' to finish: ")

    if age.lower() == "stop":
        break

    total_age += int(age)
    student_count += 1
    average_age = total_age / student_count

print("The average age of the students is", average_age)
