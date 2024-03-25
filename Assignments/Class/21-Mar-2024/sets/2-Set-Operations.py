print("")

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Set 1: ", set1)
print("Set 2: ", set2)

#    - Write a function to check if a set is a subset of another set. 
print("")
def check_subset(set1, set2):
    return set1 <= set2
sebset_set = check_subset(set1, set2)
print("Checking if set 1 is a subset of set 2: ", sebset_set)
print("")

#    - Write a function to check if two sets are disjoint. 
def check_disjoint(set1, set2):
    return set1.isdisjoint(set2)
disjoint_set = check_disjoint(set1, set2)
print("Checking if set 1 and set 2 are disjoint: ", disjoint_set)
print("")

#    - Write a function to check if two sets are equal. 
def check_equal_set(set1, set2):
    return set1 == set2
equal_set = check_equal_set(set1, set2)
print("Checking if set 1 and set 2 are equal: ", equal_set)
print("")

#    - Write a function to find the length of a set. 
def len_of_set(my_set):
    return len(my_set)
print("Length of set 1 is: ", len_of_set(set1))
print("Length of set 2 is: ", len_of_set(set2))
print("")