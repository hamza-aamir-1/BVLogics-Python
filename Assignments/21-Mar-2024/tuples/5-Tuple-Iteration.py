# - Write a function to iterate over a tuple and print its elements. 
print("")
fruits = ("Apple", "Orange", "Cherry", "Grapes")
def iterate_tuple(my_tuple):
    for i in my_tuple:
        print(i)
print("Iterating fruits tuple ", fruits)
iterate_tuple(fruits)
print("")

# - Write a function to find the index of a specific element in a tuple.
def find_index(my_tuple, item):
    return my_tuple.index(item)
print("Finding the index of \"Cherry\" in tuple ", fruits, " -> ", find_index(fruits, "Cherry"))
print("")