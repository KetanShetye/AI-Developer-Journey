# Exception Handling 
# Exception handling in Python is a core part of writing robust and fault-tolerant code. 

# Exception
# An exception is an error that occurs during program execution and interrupts the normal flow of the program.
a = 10 / 0  # ZeroDivisionError

# Basic try-except Block
try:
    x = int(input("Enter a number: "))
    result = 10 / x
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input, please enter a number.")

# Catching All Exceptions (Generic Exception)
try:
    # risky_code()
    pass
except Exception as e:
    print(f"An error occurred: {e}")
# NOTE :- Use generic Exception carefully; it's good for logging but bad for masking bugs.

# The else Clause
# Runs only if no exception occurs in the try block.
try:
    x = 5
    y = 2
    result = x / y
except ZeroDivisionError:
    print("Divide by zero error.")
else:
    print(f"Result is {result}")

# The finally Clause
# Always runs, whether or not an exception occurs.
try:
    f = open("data.txt")
    data = f.read()
except FileNotFoundError:
    print("File not found!")
finally:
    f.close()
    print("File closed.")

# Raising Exceptions Manually (raise)
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    return age

set_age(-1)  # Raises ValueError

# Custom Exceptions
# Create your own error types by subclassing Exception.
class NegativeAgeError(Exception):
    pass

def check_age(age):
    if age < 0:
        raise NegativeAgeError("Age cannot be negative.")

try:
    check_age(-5)
except NegativeAgeError as e:
    print(e)

# Exception Hierarchy
# All exceptions inherit from BaseException, and commonly from Exception.
# Most used built-in exceptions
ArithmeticError
ZeroDivisionError
ValueError
TypeError
IndexError
KeyError
IOError
ImportError
AttributeError

# Nested try-except Blocks
try:
    try:
        x = int(input("Enter number: "))
        print(10 / x)
    except ZeroDivisionError:
        print("Can't divide by zero.")
except ValueError:
    print("Invalid input.")

# Using with Statement for Resource Management
# This is not strictly exception handling, but helps avoid errors related to resources.
try:
    with open("file.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found.")

# Logging Instead of Printing
# For real-world apps, log exceptions:
import logging

try:
    1 / 0
except ZeroDivisionError as e:
    logging.exception("Division by zero occurred")

# | Concept           | Keyword               | Purpose                          |
# | ----------------- | --------------------- | -------------------------------- |
# | Try Block         | `try:`                | Code that might raise error      |
# | Catch Error       | `except:`             | Handle specific or all errors    |
# | No Error Handling | `else:`               | Executes if `try` block succeeds |
# | Cleanup Code      | `finally:`            | Executes no matter what          |
# | Raise Error       | `raise`               | Trigger exceptions manually      |
# | Define New Error  | `class ... Exception` | Custom error types               |

