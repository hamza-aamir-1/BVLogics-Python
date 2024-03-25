# - Write a function to convert a tuple to a list. 
print("")
cars_tuple = ("Volvo", "BMW", "Toyota")
def tuple_to_list(my_tuple):
    return list(my_tuple)
print("Converting cars tuple ", cars_tuple, " to list ", tuple_to_list(cars_tuple))
print("")

# - Write a function to convert a list to a tuple.
cars_list = ["Volvo", "BMW", "Toyota"]
def list_to_tuple(my_list):
    return tuple(my_list)
print("Converting cars list ", cars_list, " to tuple ", list_to_tuple(cars_list))
print("")