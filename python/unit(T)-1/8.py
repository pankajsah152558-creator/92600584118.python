
# Demonstration of Mutable and Immutable Objects

# Mutable Object (List)
my_list = [10, 20, 30]
print("Original List:", my_list)

my_list[0] = 100
print("Modified List:", my_list)

# Immutable Object (String)
my_string = "Hello"
print("\nOriginal String:", my_string)

my_string = my_string + " Python"
print("Modified String:", my_string)

# Immutable Object (Tuple)
my_tuple = (1, 2, 3)
print("\nOriginal Tuple:", my_tuple)

# Creating a new tuple instead of modifying it
my_tuple = my_tuple + (4,)
print("New Tuple:", my_tuple)
