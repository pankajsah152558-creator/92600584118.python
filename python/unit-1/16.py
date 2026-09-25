num = int(input("Enter a number: "))

original = num
sum = 0

while num > 0:
    digit = num % 10
    
    fact = 1
    for i in range(1, digit + 1):
        fact = fact * i
    
    sum = sum + fact
    num = num // 10

if original == sum:
    print("Number is KrishnaMurthy")
else:
    print("Number is Not KrishnaMurthy")
