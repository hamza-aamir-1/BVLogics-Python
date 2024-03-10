# Task 1: Write a Python program that takes a month number as input and prints the corresponding month name
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
userMonth = int(input("Enter any month number (1-12): "))
if userMonth <= 0 or userMonth > 12:
    print("Please enter a valid month number")
else:
    print(months[userMonth - 1])
