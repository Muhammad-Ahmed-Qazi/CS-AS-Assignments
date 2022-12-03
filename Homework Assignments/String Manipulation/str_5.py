# Find the count of vowels characters in an entered string separately. 

strOrig = ""

charCurr = ''

count = 0

a = 0
e = 0
i = 0
o = 0
u = 0

strOrig = input("Enter a string: ")
strOrig = strOrig.lower()

for count in range(0, len(strOrig)):
    charCurr = strOrig[count]
    if charCurr == 'a':
        a = a + 1
    elif charCurr == 'e':
        e = e + 1
    elif charCurr == 'i':
        i = i + 1
    elif charCurr == 'o':
        o = o + 1
    elif charCurr == 'u':
        u = u + 1

print("The count of vowels in the string is: \na: ", a, "\ne: ", e, "\ni: ", i, "\no: ", o, "\nu: ", u)