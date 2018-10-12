# name = input("Please tell me your name : ")
# age  = input("Please enter your age : ")
# print("Your name is " + name) 
# print("Your age is " + age)

# copies = int(input("Please tell me how many copies do you want : "))
# print(copies * ("Your name is " + name + "\n" + "Your age is " + age))

name = input("Please tell me your name : ")
age  = input("Please enter your age : ")
name_display = "Your name is " + name 
age_display = "Your age is " + age
print(name_display)
print(age_display)

copies = int(input("Please tell me how many copies do you want : "))
print(copies * (name_display + "\n" + age_display + "\n"))