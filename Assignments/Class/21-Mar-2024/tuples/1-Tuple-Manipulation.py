# - Write a function to create a tuple from user input.


# - Write a function to add an element to an existing tuple and return the new tuple.


# - Write a function to remove an element from a tuple and return the new tuple.


# - Write a function to concatenate two tuples and return the result.
print("")
def concat_tuples(tuple1, tuple2):
    return tuple1 + tuple2
tuple1 = (1, 2, 3, 4)
tuple2 = (5, 6, 7, 8)
print("New tuple after concatenating tuple 1 ", tuple1, "and tuple 2 ", tuple2, " is ", concat_tuples(tuple1, tuple2))

# - Write a function to find the length of a tuple.
print("")
def find_tuple_length(myTuple):
    return len(myTuple)
tuple5 = ("hello", "world", "lorem", "ipsum")
print("Length of tuple ", tuple5, " is ", find_tuple_length(tuple5))
print("")
