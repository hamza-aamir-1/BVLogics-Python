integerList = [23, 27, 25, 25]
stringList = ["hamza", "aamir"]

# create a list of numbers and find sum of all elements
sum = 0
for item in integerList:
    sum += item
print("Sum: ", sum)

# create a list of strings, concatenate them into a single string
singleString = ""
for item in stringList:
    singleString += item
print("Concatenate: ", singleString)

# find the maximum and minimum element in a list of numbers
print("Min: ", min(integerList), " --  Max: ", max(integerList))

# check if certain element exist in a list
print("hamza" in stringList)