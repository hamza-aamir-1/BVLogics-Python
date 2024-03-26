myTuple = ("hello", 45, "world", 100)
cars = ("jeep", "bmw", "volvo")
mobiles = ("vivo", "apple", "samsung", "infinix")

# create tuple of mixed data types and access individual elements
print("Access individual elements: ", myTuple[1])

# concatenate two tuples and create a new tuple
twoTuples = cars + mobiles
print("Concatenate two tuples: ", twoTuples)

# check if an element exist in a tuple
print("Check if an element exist in tuple: bmw", "bmw" in cars)

# convert tuple into a list
print("Convert tuple into list: ", type(list(cars)))