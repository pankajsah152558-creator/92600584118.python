string = input("Input String: ")
char = input("Input a character: ")
n = int(input("Input number of times: "))

result = ""

for i in range(n):
    result = result + string + char

print("Output:", result)
