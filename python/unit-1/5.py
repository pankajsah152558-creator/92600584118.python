# Program to find Total, Percentage, Result and Class

m1 = float(input("Enter marks of Subject 1: "))
m2 = float(input("Enter marks of Subject 2: "))
m3 = float(input("Enter marks of Subject 3: "))

total = m1 + m2 + m3
percentage = total / 3

print("Total Marks =", total)
print("Percentage =", percentage, "%")

# Result and Class
if m1 < 35 or m2 < 35 or m3 < 35:
    print("Result = Fail")
    print("Class = No Class")
elif percentage >= 70:
    print("Result = Pass")
    print("Class = Distinction")
elif percentage >= 60:
    print("Result = Pass")
    print("Class = First Class")
elif percentage >= 50:
    print("Result = Pass")
    print("Class = Second Class")
elif percentage >= 35:
    print("Result = Pass")
    print("Class = Pass Class")
