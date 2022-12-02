# Replace selected character with another in entered string.

strOrig = ""
strNew = ""

charCurr = ''
charRepl = ''
charNew = ''

count = 0

strOrig = input("Enter a string: ")
charRepl = input("Enter a character to replace: ")
charNew = input("Enter a character to replace with: ")

for count in range(0, len(strOrig)):
    charCurr = strOrig[count]
    if charCurr == charRepl:
        strNew = strNew + charNew
    else:
        strNew = strNew + charCurr

print("The new string is: ", strNew)