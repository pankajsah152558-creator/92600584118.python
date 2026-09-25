p = float(input("Enter Principal Amount: "))
r = float(input("Enter Rate of Interest: "))
n = int(input("Enter Number of Years: "))

# Simple Interest
SI = (p * r * n) / 100

# Compound Interest
CI = p * (1 + r / 100) ** n - p

print("Simple Interest =", SI)
print("Compound Interest =", CI)
