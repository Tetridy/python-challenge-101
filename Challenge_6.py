# Exercise 6 (String Lists)
# Ask the user for a string and print out whether this string is a palindrome or not. 
# (A palindrome is a string that reads the same forwards and backwards.)

# Main Code
string = str(input("Please enter a word : "))
print("Input    : " + string)
print("Reversed : " + string[::-1])
if string == string[::-1]:
    print("The word is palindrome")
else:
    print("It is just a normal word")
