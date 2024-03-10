# Task 1: Write a Python program that takes a number as input and prints "Positive" if it's greater than zero
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")

# Task 2: Write a Python program that takes a user's input as a password. If the password is "password123", print "Access granted". Otherwise, print "Access denied"
password = input("Enter password: ")
if password == "password123":
    print("Access granted!")
else:
    print("Access denied!")

# Task 3: Write a Python program that takes a year as input and prints "Leap year" if it's divisible by 4 and not divisible by 100, or if it's divisible by 400
year = int(input("Enter year: "))
if (year % 400 == 0) and (year % 100 == 0):
    print("Leap year!")
elif (year % 4 == 0) and (year % 100 != 0):
    print("Leap year!")
else:
    print("Not a leap year")
