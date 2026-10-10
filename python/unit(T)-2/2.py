# Check whether a number is positive, negative, or zero

num = int(input("Enter a number: "))

if num >= 0:
    if num == 0:
        print("The number is zero")
    else:
        print("The number is positive")
else:
    print("The number is negative")
