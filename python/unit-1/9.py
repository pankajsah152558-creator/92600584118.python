# Program to find maximum of 10 numbers without using array

# Input first number
max_num = float(input("Enter number 1: "))

# Loop for remaining 9 numbers
for i in range(2, 11):
    num = float(input(f"Enter number {i}: "))
    if num > max_num:
        max_num = num

# Display result
print("\n--- Result ---")
print(f"The maximum number is: {max_num}")
