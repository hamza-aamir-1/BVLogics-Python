# - Write a function to create a tuple from user input.
print("")
def create_tuple_user_input():
    my_tuple = ()
    items_in_tuple = int(input("How many items you want in tuple (1 to 9): "))
    if items_in_tuple < 1 or items_in_tuple > 9:
        create_tuple_user_input()
    else:
        for i in range(items_in_tuple):
            item = input("Enter item to place in tuple: ")
            my_tuple += (item,)
    return my_tuple
my_tuple = create_tuple_user_input()
print("Tuple created from your input is ", my_tuple)

# - Write a function to add an element to an existing tuple and return the new tuple.
print("")
cars = ("Volvo", "BMW", "Toyota")
def add_tuple(cars, item):
    cars += (item,)
    return cars
print("Adding element to existing tuple ", cars, " -> ", add_tuple(cars, "Honda"))

# - Write a function to remove an element from a tuple and return the new tuple.
print("")
def remove_tuple(fruits, item):
    new_fruits = tuple(x for x in fruits if x != item)
    return new_fruits
fruits = ("Apple", "Orange", "Cherry", "Grapes")
print("Removing element \"Cherry\" from fruits tuple ", fruits, " -> ", remove_tuple(fruits, "Cherry"))

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
