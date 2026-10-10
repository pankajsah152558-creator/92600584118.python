# 1. List Comprehension
squares = [x * x for x in range(1, 6)]
print("List Comprehension:", squares)

# 2. Dictionary Comprehension
squares_dict = {x: x * x for x in range(1, 6)}
print("Dictionary Comprehension:", squares_dict)

# 3. Set Comprehension
squares_set = {x * x for x in range(1, 6)}
print("Set Comprehension:", squares_set)
