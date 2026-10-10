
# Demonstration of Conditional Statements

# 1. if statement
num = int(input("Enter a number: "))

if num > 0:
    print("The number is positive")

# 2. if-else statement
if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

# 3. if-elif-else statement
if num > 0:
    print("The number is positive")
elif num < 0:
    print("The number is negative")
else:
    print("The number is zero")
