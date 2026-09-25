# Program to find sum and average of 10 numbers

# Initialize sum
total = 0

# Loop to take 10 inputs
for i in range(1, 11):
    num = float(input(f"Enter number {i}: "))
    total += num

# Calculate average
average = total / 10

# Display results
print("\n--- Results ---")
print(f"Sum of 10 numbers = {total}")
print(f"Average of 10 numbers = {average}")
