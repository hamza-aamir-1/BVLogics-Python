# - Write a function to unpack a tuple into individual variables.
print("")
def unpack_tuple(my_tuple):
    var1, var2, var3 = my_tuple
    return var1, var2, var3
my_tuple = (1, 2, 3)
var1, var2, var3 = unpack_tuple(my_tuple)
print("Unpacked variables from ", my_tuple, " are ", var1, var2, var3)
print("")

# - Write a function to zip two tuples and return a list of tuples.
fruits = ("Apple", "Orange", "Cherry", "Grapes")
cars = ("Volvo", "BMW", "Toyota")
def zip_tuples(tuple1, tuple2):
    return list(zip(tuple1, tuple2))
print("Zip two tuples ", fruits, ", ", cars, " and return list of tuples ", zip_tuples(fruits, cars))
print("")
