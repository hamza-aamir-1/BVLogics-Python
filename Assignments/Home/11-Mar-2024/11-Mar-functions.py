import math

# - Task: Write a Python function called `greet` that prints "Hello, World!" when called
def greet():
    print("Hello, World!")
greet()

# Task: Write a Python function called `add_numbers` that takes two integers as parameters and returns their sum
def add_numbers(num1, num2):
    return (num1 + num2)
print(add_numbers(3, 5))

# Task: Write a Python function called `power` that takes two parameters: a number and an exponent (with a default value of 2). The function should return the result of raising the number to the given exponent
def power(num1, num2=2):
    return num1 ** num2
print(power(4, 3))

# Task: Write a Python function called `average` that takes any number of arguments and returns the average of those numbers
def average(num1, num2, num3):
    return (num1 + num2 + num3) / 3
print(average(9, 8, 7))

# Task: Write a Python function called `create_person` that takes the parameters `name`, `age`, and `city` as keyword arguments and returns a dictionary representing a person with those attributes
def create_person(name, age, city):
    return {'name': name, 'age': age, 'city': city}
print(create_person("Hamza", 22, "Multan"))

# Task: Write a Python function called `factorial` that calculates the factorial of a given non-negative integer using recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

# - Task: Write a Python function called `sum_list` that takes a list of integers as a parameter and returns the sum of all the elements in the list
def sum_list(sumList):
    sum = 0
    for i in sumList:
        sum += i
    return sum
print(sum_list([5, 10, 15]))

#  Task: Write a Python function called `min_max` that takes a list of integers as a parameter and returns the minimum and maximum values in the list as a tuple
def min_max(intList):
    return tuple((min(intList),  max(intList)))
print(min_max([5, 10, 15, 20, 25]))

# Task: Write a Python function called `square_list` that takes a list of numbers as a parameter and returns a new list where each element is the square of the corresponding element in the input list, using a lambda expression
def square_list(intList):
    return list(map(lambda x: x ** 2, intList))
print(square_list([1, 2, 3, 4, 5]))

# Task: Write a Python function named `calculate_area` that takes the radius of a circle as input and returns the area of the circle
def calculate_area(r):
    return math.pi * (r ** 2)
radius = int(input("\nEnter radius of a circle: "))
print(calculate_area(radius))

# Task: Define a function called `is_even` that takes an integer as input and returns `True` if the number is even, otherwise `False`
def is_even(n):
    if (n % 2 == 0):
        return True
    else:
        return False
num = int(input("\nEnter a number: "))
if (is_even(num)):
    print("Number is even")
else:
    print("Number is odd")

# Task: Create a function named `count_vowels` that takes a string as input and returns the count of vowels (a, e, i, o, u) in the string
def count_vowels(word):
    vowels = 'aeiou'
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count
word = input("\nEnter a word: ")
print(count_vowels(word.lower()))

#  Task: Implement a function called `reverse_string` that takes a string as input and returns the reverse of the input string
def reverse_string(s):
    return s[::-1]
print(reverse_string(input("\nEnter a string: ")))

# Task: Define a function called `find_max` that takes a list of numbers as input and returns the maximum value in the list
print("")
myList = []
for i in range(5):
    myList.append(int(input("Enter a number: ")))
def find_max(myList):
    return max(myList)
print(find_max(myList))

# Task: Define a function called `merge_lists` that takes two lists as input and returns a new list containing all the elements from both input lists
print("")
def merge_lists(list1, list2):
    return list1 + list2
list1 = []
list2 = []
for i in range(5):
    list1.append(input("Enter something in list 1: "))
for i in range(5):
    list2.append(input("Enter something in list 2: "))
print(merge_lists(list1, list2))
