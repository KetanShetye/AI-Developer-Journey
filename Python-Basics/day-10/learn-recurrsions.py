
# Recursion 
# Recursion is a programming technique where a function calls itself to solve a smaller subproblem of the same type.

# Every recursive function has two main parts:
# 1. Base case – the condition when the function stops calling itself.
# 2. Recursive case – the part where the function calls itself.

#  Why Use Recursion?
# To break down complex problems into simpler sub-problems.

# syntax template 
# def function_name(parameters):
#     if base_case_condition:
#         return result
#     else:
#         return function_name(smaller_problem)

# Factorial of a Number
def factorial(n):
    if n == 1:
        return 1  # base case
    else:
        return n * factorial(n - 1)  # recursive call

print(factorial(5))  # Output: 120

# Fibonacci Sequence
def fibonacci(n):
    if n == 0:
        return 0  # base case
    elif n == 1:
        return 1  # base case
    else:
        return fibonacci(n-1) + fibonacci(n-2)  # recursive calls

print(fibonacci(6))  # Output: 8

# Dangers of Recursion
# 1.Stack Overflow / RecursionError
# If recursion goes too deep, Python throws an error.
# You can check recursion depth:
import sys
print(sys.getrecursionlimit())  # Default: 1000

# 2.Performance Issues
# Recursive Fibonacci is slow due to repeated calls.
# Use memoization to optimize.

# Tail Recursion (Not Supported Natively in Python)
# In some languages, tail recursion is optimized by the interpreter. Python does not do this.

# | Feature     | Recursion                         | Iteration               |
# | ----------- | --------------------------------- | ----------------------- |
# | Logic       | Function calls itself             | Loop (for/while)        |
# | Memory      | More memory (stack frames)        | Less memory             |
# | Readability | More readable (for some problems) | Less readable sometimes |
# | Speed       | Slower (due to call overhead)     | Faster                  |

