# Task 1: Write a Python program that checks if a given number is both even and divisible by 3
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 2 == 0:
    print("Number is even and divisible by 3")
elif num % 2 == 0:
    print("Number is not divisible by 3")
elif num % 3 == 0:
    print("Number is not even")
else:
    print("Neither the number is even nor it is divisible by 3")

# Task 2: Write a Python program that checks if a given number is a natural number
if num > 1:
    print("You entered a natural number")
else:
    print("Number is not a natural number")

# Task 3: Write a Python program that checks if a given character is a vowel (a, e, i, o, u)
vowel = input("Enter an alphabet: ")
chk = vowel.lower()
if chk == "a" or chk == "e" or chk == "i" or chk == "o" or chk == "u":
    print("You entered a vowel")
else:
    print("It is not a vowel")
