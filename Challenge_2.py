number = int(input("Please enter a number : "))

if number%4 == 0:
    print("Divisible by 4")
elif number%2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# Extras :
num_check = int(input("Please enter a number to check : "))
divider = int(input("Please a number as the divisor : "))

if num_check%divider == 0:
    print(str(num_check) + " divided evenly by " + str(divider))
else:
    print(str(num_check) + " does not divided evenly by " + str(divider))