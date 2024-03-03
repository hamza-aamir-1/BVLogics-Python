import math

myNumber = 9

# find square root of a given number
print("Square Root: ", myNumber, " -- ", math.sqrt(myNumber))

# check if the number is prime
if(myNumber % 2 == 0):
    print("Check if number is prime: yes")
else:
    print("Check if number is prime: no")

# generate a list of prime numbers within a given range of 99
myList = []
i = 0
while i < 100:
    if(i % 2 == 0):
        myList.append(i)
    i+=1
print("Prime number from 0 to 99: ", myList)

# calculate factorial of a number
print("Calculate factorial: ", math.factorial(myNumber))