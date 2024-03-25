fruits_set = {"apple", "orange", "grapes", "cherry"}
fruits_list = ["apple", "orange", "grapes", "cherry"]

#    - Write a function to convert a set to a list. 
print("")
def set_to_list(my_set):
    return list(my_set)
converted_fruits_set = set_to_list(fruits_set)
print("Converted fruits set ", fruits_set, " to list ", converted_fruits_set)
print("")

#    - Write a function to convert a list to a set. 
def list_to_set(my_list):
    return set(my_list)
converted_fruits_list = list_to_set(fruits_list)
print("Converted fruits list ", fruits_list, " to set ", converted_fruits_list)
print("")