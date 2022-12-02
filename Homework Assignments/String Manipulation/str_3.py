# Count and output the NUMBER of an entered character in a string. Also output separate counts for alphabets (cap & small together), digits and other characters in same entered string. 

strOrig = ""

charCurr = ''
charEntered = ''

count = 0

charCount = 0
alphaCount = 0
digitCount = 0
otherCount = 0

strOrig = input("Enter a string: ")
charEntered = input("Enter a character to count: ")

strOrig = strOrig.lower()

for count in range(0, len(strOrig)):

    charCurr = strOrig[count]
    
    if charCurr == charEntered:
        charCount = charCount + 1
    
    if ord(charCurr) >= 97 and ord(charCurr) <= 122:
        alphaCount = alphaCount + 1
    elif ord(charCurr) >= 48 and ord(charCurr) <= 57:
        digitCount = digitCount + 1
    else:
        otherCount = otherCount + 1

print("The entered character appears ", charCount, " times.")
print("The entered string has ", alphaCount, " alphabets.")
print("The entered string has ", digitCount, " digits.")
print("The entered string has ", otherCount, " other characters.")