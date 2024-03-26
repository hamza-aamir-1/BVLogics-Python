# - Write a function to find the maximum and minimum elements of a tuple. 
print("")
int_tuple = (5, 26, -30, 74, 7)
def find_max_min(int_tuple):
    min_val = min(int_tuple)
    max_val = max(int_tuple)
    return (min_val, max_val)
print("Minimum & maximum elements from tuple ", int_tuple, " are ", find_max_min(int_tuple))
print("")

# - Write a function to check if an element exists in a tuple. 
def check_element(fruits, item):
    return item in fruits
fruits = ("Apple", "Orange", "Cherry", "Grapes")
print("Checking element \"Cherry\" in tuple ", fruits, " -> ", check_element(fruits, "Cherry"))
print("")

# - Write a function to count the occurrences of an element in a tuple.
my_integers = (1, 2, 5, 7, 9, 2, 3, 7, 11)
def count_items(my_integers, item):
    return my_integers.count(item)
print("Counting how many times item 7 exist in tuple ", my_integers, " -> ", count_items(my_integers, 7))
print("")

# - Write a function to reverse a tuple. 
def reverse_tuple(fruits):
    return fruits[::-1]
print("Reversing fruits tuple ", fruits, " -> ", reverse_tuple(fruits))
print("")

# - Write a function to sort a tuple.
def sort_tuple(my_integers):
    return tuple(sorted(my_integers))
print("Sorting integers tuple ", my_integers, " -> ", sort_tuple(my_integers))
print("")