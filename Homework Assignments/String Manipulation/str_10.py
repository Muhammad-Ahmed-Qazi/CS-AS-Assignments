# Verbing:
#  - Given a string, if its length is at least 3, add 'ing' to its end.
#  - Unless it already ends in 'ing', in which case add 'ly' instead.
#  - If the string length is less than 3, leave it unchanged.
#  - Return the resulting string.
#  - Examples: input 'end' --> 'ending', input 'ending' --> 'endingly', input 'go' --> 'go'

strOrig = ""
strNew = ""

strOrig = input("Enter a string: ")

if len(strOrig) >= 3:
    if strOrig[-3:] == "ing":
        strNew = strOrig + "ly"
    else:
        strNew = strOrig + "ing"
else:
    strNew = strOrig

print("Altered string: ", strNew)