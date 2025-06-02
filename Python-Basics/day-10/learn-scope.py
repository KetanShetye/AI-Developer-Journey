# Scope
# Scope refers to the region of the program where a variable is recognized/accessible.
# | Scope Type        | Description                                          |
# | ----------------- | ---------------------------------------------------- |
# | **L** – Local     | Inside the current function                          |
# | **E** – Enclosing | Inside enclosing functions (nested functions)        |
# | **G** – Global    | At the top-level of the script/module                |
# | **B** – Built-in  | Python’s built-in names (like `len`, `sum`, `print`) |

#  1. Local Scope
# A variable declared inside a function is local to that function.
def greet():
    name = "Ketan"  # Local variable
    print("Hello", name)

greet()
# print(name)  # Error: name is not defined outside the function
# name exists only within greet().
# Outside it, name doesn’t exist.


#  2. Global Scope
# A variable defined outside all functions is a global variable.
name = "Ketan"  # Global variable

def greet():
    print("Hello", name)

greet()  # Output: Hello Ketan
# The function can read the global variable.
# But cannot modify it unless declared with global.

# 3. Modifying Global Variable Inside Function
# To change a global variable inside a function, use the global keyword.
count = 0  # Global variable

def increment():
    global count
    count += 1

increment()
print(count)  # Output: 1
# Without global, Python would treat count as a new local variable, and this would raise an error.

#  4. Enclosing Scope (Nested Functions)
# This is the scope of outer functions in nested functions.
def outer():
    name = "Ketan"
    def inner():
        print("Hello", name)  # 'name' is not local, but in enclosing scope
    inner()

outer()

# NOTE :- Python checks scopes in LEGB order:
# Local → Enclosing → Global → Built-in

# 5. Built-in Scope
# Functions like print(), len(), type() are built-in.
print(len("Ketan"))  # Uses built-in len function

# Common Confusions
#  If local and global variables have same name?
x = 10  # Global

def func():
    x = 5  # Local
    print(x)

func()     # 5 (local)
print(x)   # 10 (global unchanged)

# NOTE :-
# You can read global variables inside functions.
# You cannot assign to global variables unless you use global.
# Use global carefully — overuse can make code hard to maintain.
# For nested functions, use nonlocal to modify variables from the enclosing function.

# nonlocal Keyword
def outer():
    x = 10
    def inner():
        nonlocal x
        x += 5
        print(x)
    inner()
    print(x)

outer()  # Output: 15, 15


# | Keyword    | Scope Affected                           | Use Case                              |
# | ---------- | ---------------------------------------- | ------------------------------------- |
# | `global`   | Refers to module-level variable          | Modify global inside function         |
# | `nonlocal` | Refers to variable in enclosing function | Modify outer function var from nested |
