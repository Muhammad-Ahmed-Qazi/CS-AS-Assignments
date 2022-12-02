# Not_bad:
#  - Given a string, find the first appearance of the substring 'not' and 'bad'. If the 'bad' follows the 'not', replace the whole 'not'...'bad' substring with 'good'.
#  - Return the resulting string.
#  - Input: 'This dinner is not that bad!' 
#  - Outputs: This dinner is good!

strOrig = ""
strNew = ""

strOrig = input("Enter a string: ")

if strOrig.find("not") < strOrig.find("bad"):
    strNew = strOrig[:strOrig.find("not")] + "good" + strOrig[strOrig.find("bad") + 3:]
else:
    strNew = strOrig

print("Altered string: ", strNew)