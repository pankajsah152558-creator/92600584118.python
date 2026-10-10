import re

text = "Python is easy. Python is powerful. My age is 20."

# 1. Using match()
result1 = re.match("Python", text)
print("Match:", result1.group() if result1 else "Not found")

# 2. Using search()
result2 = re.search("easy", text)
print("Search:", result2.group() if result2 else "Not found")

# 3. Using findall()
result3 = re.findall("Python", text)
print("Find All:", result3)
