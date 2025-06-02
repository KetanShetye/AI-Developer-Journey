# Lambda Function?
# A lambda function is a small anonymous function (i.e., no name) used for simple operations.
# It is defined using the lambda keyword instead of def.
# Syntax :- lambda arguments: expression
# Can take any number of arguments
# Must have only one expression
# Automatically returns the result of the expression

# Why Use Lambda?
# For short, throwaway functions
# Often used with map(), filter(), and sorted()
# Keeps code concise

#  Basic Lambda Function
square = lambda x: x * x
print(square(5))  # Output: 25

# Lambda with Multiple Arguments
add = lambda x, y: x + y
print(add(3, 4))  # Output: 7

#  Use Inside map()
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x * x, nums))
print(squares)  # Output: [1, 4, 9, 16]

#  Use Inside filter()
nums = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, nums))
print(even)  # Output: [2, 4, 6]

# Use Inside sorted()
data = [(1, 'a'), (3, 'c'), (2, 'b')]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]

# Limitation of Lambda:
# Can only contain a single expression (no loops or multiple lines)
# Less readable for complex logic
# No name unless assigned to a variable (unlike regular functions)

# | Use Case               | Use `lambda` | Use `def` |
# | ---------------------- | ------------ | --------- |
# | Short, one-liner logic | ✅            | ❌         |
# | Complex logic          | ❌            | ✅         |
# | Reusability needed     | ❌            | ✅         |
# | Anonymous needed       | ✅            | ❌         |
