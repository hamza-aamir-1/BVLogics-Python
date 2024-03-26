# Task 1: Write a Python program that takes two numbers as input and prints the larger number
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if(num1 > num2):
    print("Larger number is ", num1)
else:
    print("Larger number is ", num2)
    
# Task 2: Write a Python program that takes two strings as input and prints "Equal" if they are the same, otherwise print "Not Equal"
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
if str1.lower() != str2.lower():
    print("Not Equal")
else:
    print("Equal")