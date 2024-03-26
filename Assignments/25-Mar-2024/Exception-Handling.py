print("")
'''
Task 1: Division with Error Handling 
    Write a function `divide (a, b) ` that takes two numbers as input and returns the 
    result of dividing `a` by `b`. Handle any `ZeroDivisionError` exceptions by printing 
    a suitable error message. 
'''
def divide(a, b):
    try:
        return int(a) / int(b)
    except ZeroDivisionError:
        return "You divided something by zero"
    except ValueError:
        return "Please enter a valid integer"
    except:
        return  "Something went wrong"
num1 = input("Enter a number: ")
num2 = input("Enter 2nd number: ")
print("Dividing ", num1, " by ", num2, ": ", divide(num1, num2))


print("")
'''
Task 2: Type Conversion with Error Handling 
    Write a function `convert_to_int(string)` that takes a string as input and 
    converts it to an integer. Handle any `ValueError` exceptions that occur during the 
    conversion by printing an appropriate error message.
'''
def convert_to_int(my_string):
    try:
        return int(my_string)
    except ValueError:
        return "The provided value cannot be converted to an integer."
    except:
        return "Oops! something went wrong"
my_string = input("Enter something to convert to integer: ")
print("Converting ", my_string, " to integer: ", convert_to_int(my_string))


print("")
'''
Task 3: List Element Access with Error Handling 
    Write a function `get_element(lst, index)` that takes a list `lst` and an index 
    `index` as input and returns the element at the specified index. Handle any 
    `IndexError` exceptions by printing a message indicating that the index is out of 
range.
'''
def get_element(lst, index):
    try:
        return lst[int(index)]
    except IndexError:
        return "The index is out of range."
    except ValueError:
        return "Please enter a valid integer in index."
    except:
        return "Oops! Something went wrong"
lst = input("Enter something to add to the list (space to enter next value): ").split()
my_index = input("Enter index to get specific value from list: ")
print("The value at index ", my_index, " in list ", lst, " is: ", get_element(lst, my_index))


print("")
'''
Task 4: Dictionary Key Access with Error Handling 
    Write a function `get_value(dictionary, key)` that takes a dictionary `dictionary` 
    and a key `key` as input and returns the value associated with the key. Handle any
    `KeyError` exceptions by printing a message indicating that the key is not present 
    in the dictionary. 
'''
def get_value(dictionary, key):
    try:
        return dictionary[key]
    except KeyError:
        return "The key you provided does not exist in the dictionary."
    except:
        return "Oops! Something went wrong"
my_keys = input("Enter dictionary keys (space to enter next): ").split()
my_values = input("Enter dictionary values (space to enter next): ").split()
my_key = input("Enter a key to get specific value from dictionary: ")
my_dict = dict(zip(my_keys, my_values))
print("The value of key ", my_key, " in dictionary ", my_dict, "is: ", get_value(my_dict, my_key))


print("")
'''
Task 5: Incorrect Function Definition 
    Write a program with a function definition that should accept two parameters, 
    but mistakenly doesn't. Introduce an `IndentationError` or `SyntaxError` by 
    improperly defining the function. Handle this error by printing a message 
    indicating the incorrect function definition. 
'''
try:
    def add(a, b):
        return a + b
except IndentationError:
    print("There's an Indentation Error due to incorrect function definition.")
except SyntaxError:
    print("There's a Syntax Error due to incorrect function definition.")
except Exception as e:
    print(e)
else:
    print(add(5, 10))