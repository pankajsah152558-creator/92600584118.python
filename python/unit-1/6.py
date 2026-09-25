# Program to find maximum of two numbers

# Input values
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Find maximum
if num1 > num2:
    print(f"The maximum number is: {num1}")
elif num2 > num1:
    print(f"The maximum number is: {num2}")
else:
    print("Both numbers are equal.")
