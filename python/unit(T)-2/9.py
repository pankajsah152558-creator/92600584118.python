# Demonstration of Iterable and Iterator

# Creating an iterable (list)
numbers = [10, 20, 30, 40, 50]

print("Iterable:")
print(numbers)

# Creating an iterator from the iterable
it = iter(numbers)

print("\nIterator:")
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
