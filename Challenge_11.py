# Exercise 11 (Check Primality Functions )
# Ask the user for a number and determine whether the number is prime or not. 
# (For those who have forgotten, a prime number is a number that has no divisors.). 
# You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below.

# Functions
def get_integer():
    return int(input("Please enter a number : "))

def check_prime(num):
    x = range(2,num)
    for elem in x:
        if (num%elem == 0):
            return print("This is not a prime number")
    print("This is a prime number")

# Main Code
number = get_integer()

check_prime(number)





