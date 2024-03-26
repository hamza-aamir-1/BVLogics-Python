# - Write a function to test if a given tuple is a subset of another tuple. 
print("")
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3, 4, 5)
def is_subset(subset, superset):
    return set(subset).issubset(set(superset))
print("Is ", tuple1, " a subset of ", tuple2, " ? ", is_subset(tuple1, tuple2))
print("")

# - Write a function to test if all elements of a tuple satisfy a condition.
def all_elements_satisfy_condition(t, condition):
    for element in t:
        if not condition(element):
            return False
    return True
tuple3 = (1, 2, 3, 4, 5)
print("Do all elements of ", tuple3, " satisfy the condition (even)? ", 
      all_elements_satisfy_condition(tuple3, lambda x: x % 2 == 0))
print("")