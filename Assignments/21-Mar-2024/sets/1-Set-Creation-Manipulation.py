#    - Write a function to create a set from user input. 
print("")
def create_set_user_input():
    my_set = set()
    how_many_items = int(input("How many items you want to add in set (0 to 9): "))
    if how_many_items < 1 or how_many_items > 9:
        print("Invalid number of items, please enter again")
        return create_set_user_input()
    else:
        for i in range(how_many_items):
            my_set.add(input("Enter something to add in set: "))
    return my_set
my_set = create_set_user_input()
print("Set created from your input is ", my_set)
print("")

#    - Write a function to add an element to an existing set. 
fruits = {"apple", "orange", "grapes", "cherry"}
print("Fruits set: ", fruits)
def add_element_to_existing_set(my_set, item):
    my_set.add(item)
    return my_set
user_input = input("Enter something to add in fruits set: ")
new_set = add_element_to_existing_set(fruits, user_input)
print("New set after adding element is: ", new_set)
print("")

#    - Write a function to remove an element from a set. 
def remove_item(my_set, item):
    my_set.discard(item)
    return my_set
remove_item(fruits, "cherry")
print("Removing cherry from fruits set: ", fruits)
print("")

#    - Write a function to perform union of two sets. 
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
def union_sets(set1, set2):
    return set1 | set2
unioned_set = union_sets(set1, set2)
print("Union of set1 ", set1, " and set2 ", set2, " is: ", unioned_set)
print("")

#    - Write a function to perform intersection of two sets. 
def intersection_sets(set1, set2):
    return set1 & set2
intersectioned_set = intersection_sets(set1, set2)
print("Intersection of set1 ", set1, " and set2 ", set2, " is: ", intersectioned_set)
print("")

#    - Write a function to perform difference between two sets. 
def difference_sets(set1, set2):
    return set1 - set2
difference_set = difference_sets(set1, set2)
print("Difference of set1 ", set1, " and set2 ", set2, " is: ", difference_set)
print("")

#    - Write a function to perform symmetric difference between two sets.
def difference_sets(set1, set2):
    return set1 ^ set2
difference_set = difference_sets(set1, set2)
print("Difference of set1 ", set1, " and set2 ", set2, " is: ", difference_set)
print("")