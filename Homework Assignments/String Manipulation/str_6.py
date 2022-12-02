# doughnuts:
#  - INPUT an INT count of a number of doughnuts, OUTPUT a string of the form 'Number of doughnuts: <count>', where <count> is the number input. 
#  - However, if the count is 10 or more, then use the word 'many' instead of the actual count.
#  - So doughnuts(5) outputs 'Number of doughnuts: 5' and doughnuts(23) outputs 'Number of doughnuts: many'

donCount = 0

donCount = int(input("Enter the number of doughnuts: "))

if donCount >= 10:
    print("Number of doughnuts: many")
else:
    print("Number of doughnuts: ", donCount)

