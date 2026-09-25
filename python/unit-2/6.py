str1 = input("Input String one: ")
str2 = input("Input String two: ")

new_string = ""

for i in range(len(str1)):
    new_string = new_string + str1[i] + str2[i]

print("Output:", new_string)
