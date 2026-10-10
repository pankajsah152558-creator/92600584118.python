import re

text = "My phone number is 9876543210"

# Search for a pattern
result = re.search(r"\d{10}", text)

if result:
    print("Pattern found:", result.group())
else:
    print("Pattern not found")

# Check whether the text starts with a word
print(re.match(r"My", text).group())

# Find all digits
print(re.findall(r"\d", "Python 123"))

# Replace a word
print(re.sub(r"phone", "mobile", text))
