# Decorator 
# A decorator is a function that takes another function as input, adds some functionality to it, and returns the modified function — without changing the original function’s code.

# Why Use Decorators?
# Code Reusability – Wrap common behavior across multiple functions
# Separation of Concerns – Keep logic like logging, authentication, etc. separate
# Cleaner Code – Use @ syntax for neatness

#  Functions Are First-Class Citizens
# In Python, functions can:
# Be passed as arguments
# Be returned from other functions
# Be assigned to variables
# This is the foundation for decorators.

# Building a Simple Decorator (Step-by-Step)
# A basic function    
def greet():
    print("Hello!")
# A decorator that adds behavior    
def decorator_function(original_function):
    def wrapper_function():
        print("Before the function runs")
        original_function()
        print("After the function runs")
    return wrapper_function
# Apply the decorator manually
decorated = decorator_function(greet)
decorated()
# Use @decorator_name (syntactic sugar)
@decorator_function
def greet():
    print("Hello!")

greet()

# Realistic Use Case: Logging
def log_decorator(func):
    def wrapper():
        print(f"Calling function: {func.__name__}")
        func()
        print("Function call finished")
    return wrapper

@log_decorator
def say_hello():
    print("Hello there!")

say_hello()

# Decorators with Arguments
# If your original function takes arguments, wrapper must accept them too.
def log_args(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments: {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_args
def add(a, b):
    print("Result:", a + b)

add(5, 10)

# Nested Decorators
# You can stack decorators:
def bold(func):
    def wrapper():
        return "<b>" + func() + "</b>"
    return wrapper

def italic(func):
    def wrapper():
        return "<i>" + func() + "</i>"
    return wrapper

@bold
@italic
def text():
    return "Hello"

print(text())  # Output: <b><i>Hello</i></b>

# Preserving Metadata (Using functools.wraps)
# Without this, decorator hides the original function’s name and docstring.
from functools import wraps

def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

# Decorator Use Cases
# | Use Case       | Description              |
# | -------------- | ------------------------ |
# | Logging        | Record function calls    |
# | Authentication | Check user permissions   |
# | Timing         | Benchmark execution time |
# | Caching        | Store expensive results  |
# | Validation     | Validate input/output    |

#  Summary
# A decorator is a wrapper around a function.
# It allows you to extend the behavior of a function without modifying it.
# Built on the power of first-class functions and closures.

