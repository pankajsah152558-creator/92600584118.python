# 1. Import the entire module
import math
print("Square root:", math.sqrt(25))

# 2. Import a specific function
from math import factorial
print("Factorial:", factorial(5))

# 3. Import multiple functions
from math import ceil, floor
print("Ceiling:", ceil(4.3))
print("Floor:", floor(4.8))

# 4. Import a module with an alias
import math as m
print("Power:", m.pow(2, 3))

# 5. Import a function with an alias
from math import sqrt as s
print("Square root:", s(36))
