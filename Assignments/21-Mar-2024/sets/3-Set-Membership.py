print("")

fruits_set = {"apple", "orange", "grapes", "cherry"}

#    - Write a function to test if an element exists in a set. 
print("")
print("Fruits set: ", fruits_set)
def test_item(my_set, item):
    return item in my_set
print("Check if cherry is in fruits set: ", test_item(fruits_set, "cherry"))
print("Check if banana is in fruits set: ", test_item(fruits_set, "banana"))
print("")

#    - Write a function to test if all elements of a set satisfy a condition.
def all_elements_satisfy_condition(my_set, condition):
    for element in my_set:
        if not condition(element):
            return False
    return True
my_set = {2, 2, 8, 4, 6}
print("Do all elements of ", my_set, " satisfy the condition (even)? ", 
      all_elements_satisfy_condition(my_set, lambda x: x % 2 == 0))
print("")