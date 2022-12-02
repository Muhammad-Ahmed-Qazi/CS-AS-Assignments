count = 0
countVowl = 0

stringOrig = ""
character = ""

vowels = ["a", "e", "i", "o", "u"]

stringOrig = input("Enter a string to count vowels in: ")
stringOrig = stringOrig.lower()

for count in range(0, len(stringOrig)):
    character = stringOrig[count]
    if character in vowels:
        countVowl = countVowl + 1

print("Number of vowels in the string:", countVowl)