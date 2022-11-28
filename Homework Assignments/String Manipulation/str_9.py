count = 0

stringOrig = ""
character = ""
outString = ""

stringOrig = input("Enter a name (or string) to make an abbreviation of: ")

for count in range(0, len(stringOrig)):
    character = stringOrig[count]
    if character == " ":
        outString = outString + stringOrig[count + 1]
    elif count == 0:
        outString = outString + stringOrig[count]

outString = outString.upper()

print("Abbreviation of input string:", outString)