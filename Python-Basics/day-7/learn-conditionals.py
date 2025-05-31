# Conditional Statements
# Conditional statements allow you to execute certain blocks of code based on whether a condition is True or False.

#  Basic if Statement
#  Executes only if the condition is True.
age = 18
if age >= 18:
    print("You are eligible to vote.")

# if-else Statement
# Chooses between two paths.
age = 16
if age >= 18:
    print("Eligible")
else:
    print("Not eligible")

# if-elif-else Ladder
marks = 75
# For multiple conditions in a hierarchy.
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: D")

# Nested if
# if inside another if.
age = 25
citizen = True

if age >= 18:
    if citizen:
        print("You can vote.")
    else:
        print("You must be a citizen to vote.")

# Ternary (One-line if-else)
# Great for short decisions.
x = 5
result = "Even" if x % 2 == 0 else "Odd"
print(result)

# Logical Operators with if
age = 25
has_id = True

if age >= 18 and has_id:
    print("Allowed entry")

# Membership & Identity Operators
fruits = ["apple", "banana"]
if "apple" in fruits:
    print("Apple is available")

a = [1, 2, 3]
b = a
if a is b:
    print("Same object in memory")

# Truthy and Falsy Values
# When using if statements, Python doesn't require a condition to be explicitly True or False — it evaluates any expression for its "truthiness".
# So what is "Truthy" and "Falsy"?
# Python automatically interprets values as either:
# ✅ Truthy → Treated as True
# ❌ Falsy → Treated as False


# Falsy Values (These behave like False in conditionals):
# | Value   | Description                 |
# | ------- | --------------------------- |
# | `False` | The boolean value `False`   |
# | `None`  | Represents absence of value |
# | `0`     | Integer zero                |
# | `0.0`   | Float zero                  |
# | `''`    | Empty string                |
# | `[]`    | Empty list                  |
# | `{}`    | Empty dictionary            |
# | `()`    | Empty tuple                 |
# | `set()` | Empty set                   |
if 0:
    print("This won't run")

if "":
    print("This won't run either")

if []:
    print("Nope, not running")

# Truthy Values (These behave like True):
# Everything other than the falsy values above is truthy!
if 10:
    print("This will run")

if "Hello":
    print("This will run")

if [1, 2, 3]:
    print("List is not empty, so this runs")

# Example: Using Truthy/Falsy in Conditions
# If the user just presses Enter, name = "", which is falsy.
name = input("Enter name: ")

if name:
    print(f"Hello, {name}!")
else:
    print("You didn’t enter your name.")



# Chained Comparisons
x = 10
if 5 < x < 15:
    print("x is in range")

# Common Mistakes
# Using = instead of ==
# if x = 5:  # ❌ Wrong
# if x == 5: # ✅ Correct
# Indentation errors:
# if True:
# print("Hi")  # ❌

# Using pass as a Placeholder
if True:
    pass  # do nothing for now

# Summary Table
# | Keyword            | Use                              |
# | ------------------ | -------------------------------- |
# | `if`               | Check a condition                |
# | `else`             | Execute if `if` fails            |
# | `elif`             | Else-if, for multiple conditions |
# | `and`, `or`, `not` | Combine conditions               |
# | `in`, `is`         | Membership & identity            |
# | `pass`             | Placeholder                      |
