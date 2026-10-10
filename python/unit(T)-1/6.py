
# Demonstration of Tuples

t = (10, 20, 30, 40, 50)

print("Original Tuple:", t)
print("First Element:", t[0])
print("Last Element:", t[-1])
print("Tuple Slicing:", t[1:4])
print("Length of Tuple:", len(t))
print("Count of 20:", t.count(20))
print("Index of 30:", t.index(30))

# Demonstration of Sets

s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60}

print("\nSet 1:", s1)
print("Set 2:", s2)

# Set Operations
print("Union:", s1 | s2)
print("Intersection:", s1 & s2)
print("Difference:", s1 - s2)

# Adding and Removing Elements
s1.add(50)
print("After Adding 50:", s1)

s1.remove(20)
print("After Removing 20:", s1)
