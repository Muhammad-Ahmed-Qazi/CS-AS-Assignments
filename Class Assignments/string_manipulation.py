count = 0
countAlph = 0
countNum = 0
countVowl = 0
occurCount = 0
index = 0

isValid = False

string1 = ""
string2 = ""
outString = ""
stringOrig = ""
truncChar = ""
truncString = ""
replChar = ""
replCharWith = ""
replString = ""
character = ""
strFormat = ""
status = ""

alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
vowels = ["a", "e", "i", "o", "u"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
strArray = []

def firstAndLast():
    string1 = input("Enter values for string one: ")
    string2 = input("Enter values for string two: ")
    outString = "First word of first string: " +  string1[:string1.find(" ")] + "\nLast word of second string: " + string2[(string2.rfind(" ") + 1):]
    print(outString)

def charTruncate():
    stringOrig = input("Enter the string to truncate: ")
    truncChar = input("Enter the character to truncate: (Case sensitive) ")
    truncString = stringOrig.replace(truncChar, "")
    print("Truncated string: ", truncString)

def charReplace():
    stringOrig = input("Enter a string to replace a character in: ")
    replChar = input("Enter the character to be replaced: (Case sensitive) ")
    replCharWith = input("Enter the character to replace: (Case sensitive) ")
    replString = stringOrig.replace(replChar, replCharWith)
    print("String with replaced character: ", replString)

def countAlphNum():
    global countAlph
    global countNum
    stringOrig = input("Enter a string to count alphabets and numbers in: ")
    for count in range(0, len(stringOrig)):
        if stringOrig[count] in alphabets:
            countAlph += 1
        elif stringOrig[count] in numbers:
            countNum += 1
    print("Number of alphabets:", countAlph, "and number of digits:", countNum)

def inverseStr():
    stringOrig = input("Enter a string to inverse it: ")
    print("Inverted string:", stringOrig[::-1])

def vowelCount():
    global countVowl
    stringOrig = input("Enter a string to count vowels in: ")
    for count in range(0, len(stringOrig)):
        if stringOrig[count] in vowels:
            countVowl += 1
    print("Number of vowels in the string:", countVowl)
def anagram():
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")
    strArray = list(string1)
    string2 = string2.replace(" ", "")
    if len(string1) == len(string2):
        for character in string2:
            if character in strArray:
                strArray.remove(character)
    
    if len(strArray) == 0:
        print("The two strings are anagrams.")
    else:
        print("The two strings are not anagrams.")

def pangram():
    global alphabets
    stringOrig = input("Enter the string to check for a pangram: ")
    stringOrig = list(set((stringOrig.replace(" ", "").lower())))
    for character in stringOrig:
        print(character, "#", alphabets)
        if character in alphabets:
            alphabets.pop(alphabets.index(character))

    if len(alphabets) == 0:
        print("The string is a pangram.")
    else:
        print("The string is not a pangram.")

def abbreviation():
    index = 0
    stringOrig = input("Enter a name (or string) to make an abbreviation of: ")
    occurCount = stringOrig.count(" ")
    outString = stringOrig[:1]
    for count in range(0, occurCount):
        index = stringOrig.index(" ", index, len(stringOrig))
        outString = outString + stringOrig[(index + 1):(index + 2)]
        index += 1
    print("Abbreviation of input string:", outString.upper())

# Work on it to allow variable lengths of characters amidst the format check identifiers

def formatCheck():
    stringOrig = input("Enter the string to format check: ")
    strFormat = input("Enter the format you want to check the string on: (Use x as placeholder text. E.g., xxxx/xx/xx) ")
    if len(stringOrig) == len(strFormat):
        for count in range(0, len(stringOrig)):
            if strFormat[count] == "x" and stringOrig[count] in alphabets:
                isValid = True
            elif strFormat[count] == "x" and stringOrig[count] in numbers:
                isValid = True
            elif strFormat[count] != "x" and stringOrig[count] == strFormat[count]:
                isValid = True
            else:
                isValid = False
            
            if isValid == False: 
                print("Loop broke!", count)
                break
        if isValid: 
            print("String matches the format!")
    else:
        print("String does not match the format!")

print("----\n1) Finding First word of one string and last word of another string.\n2) Finding and truncating a character from a string\n3) Finding and replacing a character from string\n4) Counting number of alphabets and digits in a string\n5) Inverse a string\n6) Finding the number of vowels (aeiou) in a string\n7) Finding if two strings are Anagram\n8) Find if a string is Pangram\n9) Find abbreviation of the given name\n10) String Validation (Format check.)\n----")

task = int(input("Enter the number of task you want to perform: "))

if task == 1: firstAndLast()
elif task == 2: charTruncate()
elif task == 3: charReplace()
elif task == 4: countAlphNum()
elif task == 5: inverseStr()
elif task == 6: vowelCount()
elif task == 7: anagram()
elif task == 8: pangram()
elif task == 9: abbreviation()
elif task == 10: formatCheck()