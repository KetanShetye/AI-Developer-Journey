# Higher-Order Function?
# A higher-order function is a function that:
# Takes one or more functions as arguments, OR
# Returns a function as its result,
# Or both
# In short: Functions that work with other functions.

# Powerful?
# Because in Python:
# Functions are first-class objects (can be passed around like variables),
# You can write concise, expressive, reusable logic.

# Function as Argument/
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def speak(func, msg):
    return func(msg)

print(speak(shout, "Hello"))   # Output: HELLO
print(speak(whisper, "Hello")) # Output: hello
# Here, speak is a higher-order function because it takes another function (shout or whisper) as a parameter.

# Function Returning Another Function
def multiplier(x):
    def multiply(n):
        return x * n
    return multiply

double = multiplier(2)
print(double(10))  # Output: 20
# Here, multiplier is a higher-order function because it returns another function.

# HOFs in Built-in Functions
# Python comes with powerful HOFs:

# map(function, iterable)
# Applies a function to each item in the iterable.

nums = [1, 2, 3, 4]
squared = list(map(lambda x: x*x, nums))
print(squared)  # [1, 4, 9, 16]

# filter(function, iterable)
# Filters items where the function returns True.
nums = [1, 2, 3, 4, 5]
even = list(filter(lambda x: x % 2 == 0, nums))
print(even)  # [2, 4]

# reduce(function, iterable) from functools
# Applies a function cumulatively to reduce to a single value.
from functools import reduce

nums = [1, 2, 3, 4]
total = reduce(lambda x, y: x + y, nums)
print(total)  # 10

# sorted(iterable, key=function)
# Sorts based on the function’s return value.
words = ['banana', 'apple', 'cherry']
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)  # ['apple', 'banana', 'cherry']

# | Feature     | Benefit                                   |
# | ----------- | ----------------------------------------- |
# | Reusability | Write logic once, reuse with any function |
# | Flexibility | Functions behave like variables           |
# | Readability | Express more with less code               |

#  Summary
# A Higher-Order Function takes/returns functions.
# Python’s built-in map(), filter(), reduce() are practical examples.
# Essential for functional-style programming and creating flexible APIs.
