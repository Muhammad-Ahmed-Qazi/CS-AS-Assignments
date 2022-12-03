# Find the character that appears most number of times in an entered string and output it.

strOrig = ""
strNew = ""

charCurr = ''


count = 0
searchCount = 0
charCountSta = 0
charCountEnd = 0
high = 0

strOrig = input("Enter a string: ")
strOrig = strOrig.lower()

for count in range(0, len(strOrig)):

    charCurr = strOrig[count]

    if ord(charCurr) >= 97 and ord(charCurr) <= 122:
        if charCurr not in strNew:
            strNew = strNew + charCurr + '1' + ' '
        else:
            charCountSta = strNew.find(charCurr) + 1
            for searchCount in range(charCountSta, len(strNew)):
                if strNew[searchCount] == ' ':
                    charCountEnd = searchCount
                    break
            strNew = strNew[:charCountSta] + str(int(strNew[charCountSta:charCountEnd]) + 1) + strNew[charCountEnd:]
    
    print(strNew)

count = 0

for count in range(0, len(strNew)):
    charCurr = strNew[count]
    if ord(charCurr) >= 48 and ord(charCurr) <= 57:
        if int(charCurr) > high:
            high = int(charCurr)

print("The character that appears most number of times is: ", strNew[strNew.find(str(high)) - 1])