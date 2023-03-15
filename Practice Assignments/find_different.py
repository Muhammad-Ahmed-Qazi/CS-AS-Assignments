# Importing random module
import random

# Creating a list of 10 random numbers
oddOrEven = random.randint(0, 1)

if oddOrEven == 1:
    print("Odd + 1 Even")
    numList = [random.randint(0, 100) * 2]
    for i in range(1, 10):
        numList.insert(i, (random.randint(0, 100) * 2) + 1)
else:
    print("Even + 1 Odd")
    numList = [(random.randint(0, 100) * 2) + 1]
    for i in range(1, 10):
        numList.insert(i, random.randint(0, 100) * 2)

random.shuffle(numList)
print(numList, "\n")

# Finding the different number
different = list(filter(lambda item: item % 2 == 1, numList))

# Output
if len(different) == 1:
    print("The list is of even numbers with one odd number: " + str(different[0]), "at position", numList.index(different[0]) + 1)
else:
    [print("The list is of odd numbers with one even number: " + str(item) + " at position", numList.index(item) + 1) for item in numList if item not in different]