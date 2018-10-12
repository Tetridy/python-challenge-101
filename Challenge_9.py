# Exercise 9 (Guessing Game One)
# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

# Extras:
# 1. Keep the game going until the user types “exit”
# 2. Keep track of how many guesses the user has taken, and when the game ends, print this out.

# Main Code
import random
target = random.randint(1,9)
print(target)

count = 0
guess = 0

while guess != "exit":
    guess = str(input("Guess the number : "))
    if str(guess) == 'exit':
        print("Awwww, you quit after " + str(count) + " attempts :(")
        break
    count += 1
    if int(guess) == target:
        print("Congratulations, it only take you " + str(count) + " attempts to guess the correct number")
        break
    elif int(guess) < target:
        print("Whoops, you guess is too low")
    elif int(guess) > target:
        print("Whoops, you guess is too high")

   