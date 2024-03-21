# 1- Create a function that takes a list of numbers as input and returns the sum of all the numbers
sumList = []
for i in range(5):
    sumList.append(int(input("Enter a number: ")))
def sum_list(sumList):
    return sum(sumList)
print("Sum of ", sumList, " is ", sum_list(sumList))


# 2- Write a function that takes two lists as input and returns a new list containing elements that are common to both input lists
commonItems1 = []
for i in range(5):
    commonItems1.append(input("Enter something in list 1: "))
commonItems2 = []
for i in range(5):
    commonItems2.append(input("Enter something in list 2: "))
def commonElements(list1, list2):
    return list(set(list1).intersection(set(list2)))
print("Common elements in ", commonItems1, " and ", commonItems2,
      " are ", commonElements(commonItems1, commonItems2))


# 3- Implement a function that takes a list of strings as input and returns the longest string in the list
def findLongestString(words):
    longestWord = ""
    for word in words:
        if len(word) > len(longestWord):
            longestWord = word
    return longestWord
strList = []
for i in range(5):
    strList.append(input("Enter a word: "))
print("The longest word in ", strList, " is ", findLongestString(strList))


# 4- Create a function that takes a list of integers as input and returns a new list with only the even numbers from the input list
evenIntList = []
for i in range(5):
    evenIntList.append(int(input("Enter a number: ")))
def countEvenNumbers(evenList):
    newList = []
    for i in evenList:
        if i % 2 == 0:
            newList.append(i)
    return newList
print("Even numbers from ", evenIntList, " are ", countEvenNumbers(evenIntList))


# 5- Write a function that takes a list of strings as input and returns a new list with the strings sorted alphabetically
def sortStringList(strList):
    strList.sort()
    return strList
sortStrList = []
for i in range(5):
    sortStrList.append(input("Enter a word: "))
print("The sorted list is ", sortStringList(sortStrList))


# 6- Implement a function that takes a list of numbers as input and returns the average of all the numbers in the list
avgIntList = []
for i in range(5):
    avgIntList.append(int(input("Enter a number: ")))
def findAvgList (intList):
    return sum(intList) / len(intList)
print ("The average of ", avgIntList, " is ", findAvgList(avgIntList))


# 7- Create a function that takes a list of numbers as input and returns a new list with the square of each number in the input list
sqrIntList = []
for i in range(5):
    sqrIntList.append(int(input("Enter a number: ")))
def square_list(intList):
    return list(map(lambda x: x ** 2, intList))
print("The square of ", sqrIntList, " is ", square_list(sqrIntList))


# 8- Write a function that takes a list of strings as input and returns a new list with the length of each string in the input list
def findLengthStringList(strList):
    newList = []
    for i in strList:
        newList.append(len(i))
    return newList
lenStrList = []
for i in range(5):
    lenStrList.append(input("Enter a word: "))
print("The length of ", lenStrList, " is ", findLengthStringList(lenStrList))


# 9- Implement a function that takes a list of integers as input and returns the largest number in the list
largestNum = []
for i in range(5):
    largestNum.append(int(input("Enter a number: ")))
def findLargestNum(numbers):
    return max(numbers)
print("The largest number from ", largestNum, " is ", findLargestNum(largestNum))


# 10- Create a function that takes two lists of equal length as input and returns a new list where each element is the sum of the corresponding elements from the input lists
sumList1 = []
sumList2 = []
for i in range(5):
    sumList1.append(int(input("Enter a number in list 1: ")))
for i in range(5):
    sumList2.append(int(input("Enter a number in list 2: ")))
def sumTwoList (sumList1, sumList2):
    newList = []
    for i in range(5):
        newList.append(sumList1[i] + sumList2[i])
    return newList
print("Sum of ", sumList1, " and ", sumList2, " is ", sumTwoList(sumList1, sumList2))