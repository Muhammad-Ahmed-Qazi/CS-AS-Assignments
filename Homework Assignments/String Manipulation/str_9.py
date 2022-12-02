# MixUp:
#  - Given strings a and b, return a single string with a and b separated by a space '<a> <b>', except swap the first 2 chars of each string.
#  - E.g. 'mix', pod' -> 'pox mid', 'dog', 'dinner' -> 'dig donner'
#  - Assume a and b are length 2 or more.

a = ""
b = ""
strNew = ""

a = input("Enter a string: ")
b = input("Enter another string: ")

strNew = b[0:2] + a[2:] + " " + a[0:2] + b[2:]

print("Altered string: ", strNew)