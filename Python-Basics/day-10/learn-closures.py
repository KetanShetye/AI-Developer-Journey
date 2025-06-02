# Closure
# A closure is a function object that remembers values from its enclosing lexical scope, even when the outer function has finished execution.
# A closure "remembers" the environment in which it was created.

# Requirements for a Closure:
# A closure happens when:
# There is a nested function (a function inside another function).
# The inner function uses a variable from the outer function.
# The outer function returns the inner function.
# eg-
def outer(msg):
    def inner():
        print("Message:", msg)  # uses outer's variable
    return inner

my_func = outer("Hello from closure")
my_func()  # Output: Message: Hello from closure
# Here, inner() remembers the value of msg even after outer() has finished.
# This is a closure.

#  What Happens Behind the Scenes?
# outer() returns inner (not calls it).
# inner has a reference to msg from outer.
# When you call my_func(), it still has access to msg.

# Closures Retain State
# Closures are often used to retain data across function calls without using global variables or classes.
def counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner

count_up = counter()

print(count_up())  # 1
print(count_up())  # 2
print(count_up())  # 3
# Each call to count_up() remembers and updates count.

# Closures as Function Factories
# Closures can be used to create customized functions.
def multiplier(x):
    def multiply(n):
        return x * n
    return multiply

times3 = multiplier(3)
times5 = multiplier(5)

print(times3(10))  # 30
print(times5(10))  # 50

# Why Use Closures?
# Hide internal details (data hiding)
# Avoid global variables
# Maintain private states
# Build function factories (custom function creators)

# | Feature       | Closure                           | Class                                    |
# | ------------- | --------------------------------- | ---------------------------------------- |
# | Syntax        | Functional                        | Object-oriented                          |
# | State Storage | Maintains state via enclosed vars | Maintains state via attributes           |
# | Use When      | You need lightweight memory/state | You need multiple methods or inheritance |

# Common Misunderstanding
# People expect the inner function to be recalculated fresh every time.
# But it remembers the last state because it's closed over the environment.

#  Inspecting Closure Internals (Optional)
# You can see the closure variables with:
print(my_func.__closure__)
print(my_func.__closure__[0].cell_contents)

# A closure is:
# A function defined inside another function
# That uses variables from the outer function
# And remembers those values after the outer function is done
