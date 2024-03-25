# - Write a function to slice a tuple based on start and end indices. 
print("")
my_integers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
def slice_tuple(tuple1):
    return tuple1[2:7]
print("Slicing tuple ", my_integers, " from indices 2 to 7 ", slice_tuple(my_integers))
print("")

# - Write a function to return the first n elements of a tuple.
def slice_n_items(tuple1, n):
    return tuple1[:n]
print("Slicing first 5 elements of tuple ", my_integers, " -> ", slice_n_items(my_integers, 5))
print("")