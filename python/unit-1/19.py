numbers = []

for i in range(10):
    num = int(input("Enter number: "))
    numbers.append(num)

numbers.sort()

min1 = numbers[0]
min2 = numbers[1]
min3 = numbers[2]

max1 = numbers[9]
max2 = numbers[8]
max3 = numbers[7]

print("Max1 =", max1)
print("Max2 =", max2)
print("Max3 =", max3)

print("Min1 =", min1)
print("Min2 =", min2)
print("Min3 =", min3)
