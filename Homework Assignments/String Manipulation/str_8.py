# Fix_start:
#  - Given a string s, return a string where all occurences of its first char have been changed to '*', except do not change the first char itself.
#  - E.g., 'babble' yields 'ba**le' or 'alpha' outputs 'alph*'.
#  - Assume that the string is length 1 or more.

s = ""
strNew = ""

charFirst = ''

count = 0

flag = False

s = input("Enter a string: ")
s = s.lower()
charFirst = s[0]

for count in range(0, len(s)):
    if flag and s[count] == charFirst:
        strNew = strNew + '*'
    elif flag == False:
        strNew = strNew + s[count]
        flag = True
    else:
        strNew = strNew + s[count]

print("Altered string: ", strNew)