print("")

'''
Write a Python function that takes an integer as input and doubles its value inside the function. Call this function with an integer variable as an argument and print the original and updated values of the variable before and after the function call
'''
def int_double(num):
    return num**num
num = 5
print("Number before function call: ", num)
int_double(num)
print("Number after function call: ", num)

print("")

'''
Write a Python function that takes a list as input and appends an element to the list inside the function. Call this function with a list variable as an argument and print the original and updated values of the list before and after the function call
'''
def list_append(myList):
    return myList.append(4)
myList = [1, 2, 3]
print("List before append using function: ", myList)
list_append(myList)
print("List after append using function: ", myList)

print("")

'''
Write a Python program that demonstrates the difference between pass by value and pass by reference. This could involve creating a function that modifies a variable passed by value and another function that modifies a variable passed by reference. Call both functions with appropriate variables and observe the changes
'''
def pass_by_value(x):
    x = 10
    print("Value of x inside pass_by_value function:", x)
def pass_by_reference(lst):
    lst.append(4)
    print("Value of lst inside pass_by_reference function:", lst)
a = 5
b = [1, 2, 3]
print("Initial values -> ", "a:", a, ", b:", b)
pass_by_value(a)
pass_by_reference(b)
print("Values after calling functions -> ", "a:", a, ", b:", b)

print("")

'''
Write a Python program that declares a variable outside a function and another variable inside the function with the same name. Inside the function, modify the variable. Print both variables before and after the function call to understand how variable scope affects pass by value and pass by reference
'''
def myFun():
    myVar = "World"
    print("Variable inside function: ", myVar)
myVar = "Hello"
print("Variable before function call: ", myVar)
myFun()
print("Variable after function call: ", myVar)

print('')

'''
Write a Python program that declares a variable in the global scope and another variable with the same name inside a function. Attempt to access both variables from within the function. Print the values of both variables before and after the function call to observe the scope differences
'''
global_variable = 10
def function_scope():
    global_variable = 20
    print("Value of global_variable inside function: ", global_variable)
print("Value of global_variable before function call: ", global_variable)
function_scope()
print("Value of global_variable after function call: ", global_variable)

print("")

'''
Define a function `outer_function` that declares a variable `x` and another function `inner_function` inside it. The inner function should access the variable `x` from the enclosing scope and print its value. Call `outer_function` and then call `inner_function` to observe how the inner function can access variables from the enclosing scope
'''
def outer_function():
    x = 10
    def inner_function():
        print("Value of x from inner_function:", x)
    inner_function()
outer_function()

print('')

'''
Write a Python program that defines a function `change_global_variable` which attempts to modify a global variable `count`. Declare the `count` variable outside the function. Inside the function, use the `global` keyword to modify the value of `count`. Print the value of `count` before and after calling the function to see the effect of the `global` keyword
'''
count = 5
def change_global_variable():
    global count
    count += 1
    return count
print("Value of count before functiion: ", count)
change_global_variable()
print("Value of count after functiion: ", count)

print('')

'''
Define a function `outer_function` that declares a variable `x` and defines another function `inner_function` inside it. The inner function should modify the variable `x` from the enclosing scope using the `nonlocal` keyword. Print the value of `x` before and after calling the inner function to observe the effect of the `nonlocal` keyword
'''
def outer_function():
    x = 10
    def inner_function():
        nonlocal x
        x = 20
    print("Value of x before calling inner_function:", x)
    inner_function()
    print("Value of x after calling inner_function:", x)
outer_function()