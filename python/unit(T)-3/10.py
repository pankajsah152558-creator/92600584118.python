import re

# Read data from a text file
with open("data.txt", "r") as file:
    text = file.read()

# Extract email addresses
emails = re.findall(r'[\w.-]+@[\w.-]+\.\w+', text)

# Extract phone numbers (10 digits)
phones = re.findall(r'\b\d{10}\b', text)

# Extract numbers
numbers = re.findall(r'\b\d+\b', text)

print("Email Addresses:", emails)
print("Phone Numbers:", phones)
print("Numbers:", numbers)
