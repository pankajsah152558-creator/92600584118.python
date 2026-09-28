def calculate_total(marks):
    return sum(marks)

def calculate_percentage(marks):
    return (calculate_total(marks) / 500) * 100

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


import result_utils

from result_utils import calculate_percentage, calculate_grade

student_name = "pankaj"
marks = [85, 78, 92, 88, 80]

total = result_utils.calculate_total(marks)
percentage = calculate_percentage(marks)
grade = calculate_grade(percentage)

print("=" * 35)
print("       STUDENT RESULT")
print("=" * 35)
print("Student Name :", student_name)
print("Marks        :", marks)
print("Total Marks  :", total, "/500")
print("Percentage   :", f"{percentage:.2f}%")
print("Grade        :", grade)
print("=" * 35)
