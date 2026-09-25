num = int(input("Enter a number: "))

original = num
sum = 0
digits = len(str(num))

while num > 0:
    digit = num % 10
    sum = sum + digit ** digits
    num = num // 10

if original == sum:
    print("Number is Armstrong")
else:
    print("Number is Not Armstrong")
