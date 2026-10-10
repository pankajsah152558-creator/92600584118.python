# Program to generate a sequence of numbers

def generate_numbers(n):
    for i in range(1, n + 1):
        yield i

# Calling the generator function
num = int(input("Enter the limit: "))

print("Sequence of numbers:")
for number in generate_numbers(num):
    print(number)
