
# Creating a Dictionary
student = {
    "name": "Rahul",
    "age": 18,
    "course": "BCA",
    "marks": 85
}

print("Original Dictionary:", student)

# Dictionary Methods
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# Accessing a Value
print("Student Name:", student.get("name"))

# Adding and Updating Elements
student["city"] = "Saharsa"
student["marks"] = 90
print("After Adding and Updating:", student)

# Removing an Element
student.pop("age")
print("After Removing Age:", student)

# Iteration Through Dictionary
print("\nIterating Through Dictionary:")
for key, value in student.items():
    print(key, ":", value)
