# Both_ends:
#  - Input a string s, output a string made of the first 2 and the last 2 chars of the original string, so 'spring' yields 'spng'. 
#  - However, if the string length is less than 2, return string s instead the empty string.

s = ""
strNew = ""

s = input("Enter a string: ")

if len(s) < 2:
    print(s)
else:
    strNew = s[0:2] + s[-2:]
    print(strNew)