# Exercise 5 (List Overlap)
# Take two lists, say for example these two:

#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.

# Extras:
# 1. Randomly generate two lists to test this
# 2. Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

# Main Code
import random
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
overlap = []
list_1 = []
list_2 = []

for x in range(random.randint(8,20)):
    list_1.append(random.randint(0,100))
list_1.sort()
print ("List 1  : " + str(list_1))

for x in range(random.randint(8,20)):
    list_2.append(random.randint(0,100))
list_2.sort()
print ("List 2  : " + str(list_2))

# overlap = [element for element in a if element in b not in overlap]
# overlap.sort()

for element in list_1:
    if element in list_2:
        if element not in overlap:
            overlap.append(element)

print ("Overlap : " + str(overlap))

