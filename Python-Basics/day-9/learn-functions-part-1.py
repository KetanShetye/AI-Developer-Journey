# Funtions
# A block of code that performs a specific task.
# Reusable 
# modular - (Modular means breaking down a large program into smaller, manageable, and independent pieces (modules). Each piece does a specific task and can be reused anywhere.).
def greet():
    print("Hello!")

# Types of Functions
#-> Built-in Functions eg:- print(), len(), range()
#-> User-defined Functions: Created by the programmer.

# Defining a Function
def function_name():
    # Code block
    pass

# Calling a Function
def say_hello():
    print("Hello")

say_hello()

# Function with Parameters
def greet(name):
    print(f"Hello, {name}!")

# Function with Multiple Parameters
def add(a, b):
    return a + b

# Default Parameters
def greet(name="Guest"):
    print(f"Hello, {name}")

# Return Statement
def square(x):
    return x * x

#  Keyword vs Positional Arguments
def details(name, age):
    print(name, age)

details("Alice", 25)            # Positional
details(age=25, name="Alice")   # Keyword

# Variable-Length Arguments
# Python allows functions to accept a variable number of arguments using:

# *args → Positional arguments (Tuple)
# Used when you don’t know how many values will be pass
def add_numbers(*args):
    print(args)         # Just to see what's inside
    return sum(args)

print(add_numbers(1, 2, 3))          # Output: 6
print(add_numbers(5, 10, 15, 20))    # Output: 50
# args is a tuple: (1, 2, 3)
# You can loop through it, apply sum(), etc.

#  **kwargs → Keyword arguments (Dictionary)
# Used when you don’t know how many named arguments will be passed.
def print_details(**kwargs):
    print(kwargs)  # Just to show the dictionary
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Ketan", age=24, skill="React")
print_details(name="Ketan", age=24, skill="React",hobby="football")

#  You can combine *args and **kwargs:
def demo(a, *args, **kwargs):
    print("a:", a)
    print("args:", args)
    print("kwargs:", kwargs)

demo(10, 20, 30, name="Ketan", age=24)
# a = 10
# args = (20, 30)
# kwargs = {'name': 'Ketan', 'age': 24}


