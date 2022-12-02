# Find if the input string has all the alphabets; capital or small alike.

strOrig = ""
strNew = ""

charAsc = ''

total = 0
count = 0

strOrig = input("Enter a string: ")
strOrig = strOrig.lower()

for count in range(0, len(strOrig)):
    
    charAsc = strOrig[count]
    
    if ord(charAsc) >= 97 and ord(charAsc) <= 122:
        if charAsc not in strNew:
            strNew = strNew + charAsc
            total = total + ord(charAsc)

if total == 2847:
    print("The string has all the alphabets.")
else:
    print("The string does not have all the alphabets.")