string = input("Enter a string: ")
char = input("Character to find: ")

count = 0

for ch in string:
    if ch == char:
        count = count + 1

print("Output:", count)
