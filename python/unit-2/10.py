string = input("Enter a string: ")

count = 0
sum = 0

for ch in string:
    if ch.isdigit():
        count = count + 1
        sum = sum + int(ch)

if count == 0:
    print("0")
else:
    print("No. of digits:", count)
    print("Sum of digits:", sum)
