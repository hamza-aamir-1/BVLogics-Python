# Task 1: Write a Python program that takes three numbers as input and prints the highest value
# Task 2: Write a Python program that takes four numbers as input and prints the lowest value
numbers = []
print("Enter 4 numbers")
for i in range(0, 4):
    numbers.append(int(input("Enter number: ")))
highest = numbers[0]
lowest = numbers[0]
for num in numbers:
    if num > highest:
        highest = num
    if num < lowest:
        lowest = num
print("Highest number is ", highest)
print("Lowest number is ", lowest)

# Task Write a Python program that takes a number as input and checks if it's within the range of 10 to 20, 30 to 40, or 50 to 60. Print the corresponding range if true, otherwise print "Out of range"
num = int(input("Enter a number: "))
if num >= 10 and num <= 20:
    print("Number within the range of 10 to 20")
elif num >= 30 and num <= 40:
    print("Number within the range of 30 to 40")
elif num >= 50 and num <= 60:
    print("Number within the range of 50 to 60")
else:
    print("Out of range")

# Task: Write a Python program that takes three strings as input and compares their lengths. Print the longest string
names = []
print("Enter 3 names")
for i in range(0, 3):
    names.append(input("Enter name: "))
longest_name = max(names, key=len)
print("The longest name is:", longest_name)
