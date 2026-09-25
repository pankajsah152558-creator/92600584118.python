string = input("Enter a string: ")

vowels = 0
consonants = 0

for ch in string:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels = vowels + 1
        else:
            consonants = consonants + 1

total = vowels + consonants

vowel_percentage = (vowels / total) * 100
consonant_percentage = (consonants / total) * 100

print("Number of Vowels =", vowels)
print("Number of Consonants =", consonants)
print("Percentage of Vowels =", vowel_percentage, "%")
print("Percentage of Consonants =", consonant_percentage, "%")
