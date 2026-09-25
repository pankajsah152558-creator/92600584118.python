for i in range(1, 11):
    print(i, end=" ")
    
    for i in range(2, 21, 2):
        print(i, end=" ")
    
    for i in range(1, 20, 2):
        print(i, end=" ")
    
    for i in range(100, 89, -1):
        print(i, end=" ")
    
    for i in range(200, 179, -2):
        print(i, end=" ")
    
    n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    
    sum = 0

for i in range(1, 11):
    sum = sum + i

print("1 + 2 + ... + 10 =", sum)

sum = 0

for i in range(1, 10):
    sum = sum + i / (i + 1)

print("Answer =", sum)

sum = 0

for i in range(1, 11):
    sum = sum + i / (i * 10)

print("Answer =", sum)
