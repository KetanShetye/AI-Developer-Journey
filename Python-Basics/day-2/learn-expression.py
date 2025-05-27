# Expression (Code that returns a value)
# An expression is any piece of code that produces a value. 
# It can be as simple as a single literal, a variable, or more complex involving operators, function calls, and combinations thereof.
42                 # integer literal → value 42
3.14               # float literal → value 3.14
"Hello, world!"    # string literal → value "Hello, world!"
# x                  # variable (assuming x=5) → value of x
# x + 10             # arithmetic expression → value of x + 10
# NOTE :- Every expression can be evaluated and results in some value.

# -> Arithmetic Expressions
# using arithmetic operators
# eg:-
a = 10
b = 3
c = a * (b + 2) ** 2 / 4

# -> Boolean Expressions 
# Use comparison and logical operators
x = 5
y = 10
result = (x < y) and (y != 0)

# -> String Expressions
# Concatenation and repetition:
greeting = "Hello" + ", " + "World!"  # "Hello, World!"
repeat = "ha" * 3                     # "hahaha"

# -> Function Calls 
# Function calls return a value and so are expressions.
len("hello")    # returns 5
max(1, 5, 3)    # returns 5

# -> Container Expressions
# Expressions that create containers
[1, 2, 3]         # list expression
{'a': 1, 'b': 2}  # dict expression
(1, 2, 3)         # tuple expression
{1, 2, 3}         # set expression 

# -> Operator Precedence 
# Python evaluates operators according to precedence rules
# | Operator Type                                | Example             | Precedence (High → Low) |   |
# | -------------------------------------------- | ------------------- | ----------------------- | - |
# | Parentheses                                  | `(a + b)`           | Highest                 |   |
# | Exponentiation                               | `**`                |                         |   |
# | Unary plus, minus, not                       | `-a`, `+a`, `not a` |                         |   |
# | Multiplication, Division, Floor Div, Modulus | `*`, `/`, `//`, `%` |                         |   |
# | Addition, Subtraction                        | `+`, `-`            |                         |   |
# | Bitwise Shifts                               | `<<`, `>>`          |                         |   |
# | Bitwise AND                                  | `&`                 |                         |   |
# | Bitwise XOR                                  | `^`                 |                         |   |
# | Bitwise OR                                   | \`                  | \`                      |   |
# | Comparisons                                  | `<`, `>`, `==`, etc |                         |   |
# | Boolean AND                                  | `and`               |                         |   |
# | Boolean OR                                   | `or`                | Lowest                  |   |
result = 2 + 3 * 4

# You might think:
# Add 2 + 3 → get 5
# Multiply 5 * 4 → get 20 ❌

# But Python does:
# First: 3 * 4 = 12 ✅
# Then: 2 + 12 = 14 ✅

# Why? - Because Python follows precedence rules (order of operations):
2 + 3 * 4
# is treated as
2 + (3 * 4)
# To change the order, you use parentheses
(2 + 3) * 4  

# Python goes left to right when precedence is the same.
10 - 3 - 2

# Python does
10 - 3 = 7
7 - 2 = 5

# If it went right to left
3 - 2 = 1
10 - 1 = 9 #❌ (but this is not what Python does)





# Expressions vs Statements
# Expressions return values.
# Statements perform an action.
x = 5       # assignment is a statement, not an expression
x + 1       # expression, evaluates to 6
print(x + 1) # statement (function call) that does something

# -> List Comprehensions (Expressions that build lists)
squares = [x**2 for x in range(10)]

# -> Generator Expressions (Lazy evaluation)
gen = (x**2 for x in range(10))

# -> Lambda Expressions (Anonymous functions)
f = lambda x: x + 1
print(f(4))  # outputs 5

# -> Conditional Expressions (Ternary)
max_val = a if a > b else b

# -> Python internally compiles source code to an AST(Abstract Syntax Trees) where expressions are nodes with subnodes.
import ast
tree = ast.parse("a + b * c", mode='eval')
print(ast.dump(tree, indent=4)) # This outputs a tree representing the expression structure.

# -> Short-circuit evaluation
# It’s efficient: avoids extra computation
# Used in conditions with side effects or safety
# For boolean expressions, `and` and `or` evaluate lazily
# and — Stops if the first value is False
# or — Stops if the first value is True
def foo():
    print("foo called")
    return True

result = foo() or False
# 'foo called' is printed, result is True

name = None
if name is not None and len(name) > 0:
    print("Valid name")
# If name is None, Python won’t check len(name) (avoids error).

# | Operator | Stops If...      | Example              | Result  |
# | -------- | ---------------- | -------------------- | ------- |
# | `and`    | first is `False` | `False and anything` | `False` |
# | `or`     | first is `True`  | `True or anything`   | `True`  |

