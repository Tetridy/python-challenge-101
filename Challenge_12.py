# Exercise 12 (List Ends)
# Write a program that takes a list of numbers 
# (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. 
# For practice, write this code inside a function.

# Functions
def new_list(array):
    listnew = []
    last=len(array)-1
    listnew.append(array[0])
    listnew.append(array[last])
    print("New list : " + str(listnew))

# Main Code
a = [5, 10, 15, 20, 25]
new_list(a)
