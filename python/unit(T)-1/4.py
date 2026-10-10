
# Demonstration of String Operations

s = "Hello Python"

# String Slicing
print("Original String:", s)
print("First 5 characters:", s[0:5])
print("Characters from index 6:", s[6:])
print("Reverse String:", s[::-1])

# String Formatting
name = "Rahul"
age = 18
print("My name is {} and I am {} years old.".format(name, age))
print(f"My name is {name} and I am {age} years old.")

# Built-in String Functions
text = "  hello python  "
print("Uppercase:", s.upper())
print("Lowercase:", s.lower())
print("Title Case:", s.title())
print("Length:", len(s))
print("Replace:", s.replace("Python", "World"))
print("Strip:", text.strip())
print("Count of 'o':", s.count("o"))
print("Find 'Python':", s.find("Python"))
print("Starts with Hello:", s.startswith("Hello"))
