# Both_ends:
#  - Input a string s, output a string made of the first 2 and the last 2 chars of the original string, so 'spring' yields 'spng'. 
#  - However, if the string length is less than 2, return string s instead the empty string.

strOrig = ""
strNew = ""

strOrig = input("Enter a string: ")

if len(strOrig) < 2:
    print(strOrig)
else:
    strNew = strOrig[0:2] + strOrig[-2:]
    print(strNew)